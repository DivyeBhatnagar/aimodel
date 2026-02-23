require('dotenv').config();
const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 5000;
const OLLAMA_URL = process.env.OLLAMA_URL || 'http://localhost:11434';

// Middleware
app.use(cors());
app.use(express.json());

// System prompt for CodePilot AI
const SYSTEM_PROMPT = `You are CodePilot AI, a professional full-stack development assistant. You provide clear, accurate, and production-ready code solutions. You understand modern web technologies, best practices, and clean code principles.`;

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'ok', message: 'CodePilot AI Backend is running' });
});

// Main generation endpoint
app.post('/generate', async (req, res) => {
  try {
    const { prompt, model = 'llama3', temperature = 0.7, max_tokens } = req.body;

    // Validate input
    if (!prompt) {
      return res.status(400).json({ 
        error: 'Prompt is required',
        success: false 
      });
    }

    // Construct full prompt with system context
    const fullPrompt = `${SYSTEM_PROMPT}\n\nUser Request: ${prompt}`;

    // Prepare request to Ollama
    const ollamaRequest = {
      model: model,
      prompt: fullPrompt,
      stream: false,
      options: {
        temperature: temperature
      }
    };

    if (max_tokens) {
      ollamaRequest.options.num_predict = max_tokens;
    }

    console.log(`[${new Date().toISOString()}] Generating response for prompt...`);

    // Send request to Ollama
    const response = await axios.post(
      `${OLLAMA_URL}/api/generate`,
      ollamaRequest,
      {
        timeout: 120000 // 2 minute timeout
      }
    );

    // Return structured response
    res.json({
      success: true,
      response: response.data.response,
      model: response.data.model,
      created_at: response.data.created_at,
      done: response.data.done,
      context: response.data.context,
      total_duration: response.data.total_duration,
      load_duration: response.data.load_duration,
      prompt_eval_count: response.data.prompt_eval_count,
      eval_count: response.data.eval_count
    });

  } catch (error) {
    console.error('Error generating response:', error.message);
    
    // Handle specific error cases
    if (error.code === 'ECONNREFUSED') {
      return res.status(503).json({
        success: false,
        error: 'Cannot connect to Ollama. Make sure Ollama is running (ollama serve)',
        details: 'Connection refused to ' + OLLAMA_URL
      });
    }

    if (error.response) {
      return res.status(error.response.status).json({
        success: false,
        error: 'Ollama API error',
        details: error.response.data
      });
    }

    res.status(500).json({
      success: false,
      error: 'Internal server error',
      details: error.message
    });
  }
});

// Start server
app.listen(PORT, () => {
  console.log('='.repeat(50));
  console.log(`🚀 CodePilot AI Backend running on port ${PORT}`);
  console.log(`📡 Ollama URL: ${OLLAMA_URL}`);
  console.log(`🔗 API Endpoint: http://localhost:${PORT}/generate`);
  console.log('='.repeat(50));
});
