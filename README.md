# CodePilot Local LLM Backend

A production-ready local AI backend using LLaMA 3 via Ollama. Runs completely offline and exposes a REST API for AI code generation.

## Tech Stack

- **Node.js** - Runtime environment
- **Express** - Web framework
- **Axios** - HTTP client
- **Ollama** - Local LLM engine
- **LLaMA 3** - AI model

## Prerequisites

- Node.js 16+ installed
- macOS, Linux, or Windows
- At least 8GB RAM (16GB recommended)

---

## Installation Guide

### Step 1: Install Ollama

**macOS:**
```bash
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Download from https://ollama.com/download

### Step 2: Start Ollama Service

Open a terminal and run:
```bash
ollama serve
```

Keep this terminal running. Ollama will run on `http://localhost:11434`

### Step 3: Pull LLaMA 3 Model

Open a new terminal and run:
```bash
ollama pull llama3
```

This downloads the LLaMA 3 model (~4.7GB). Wait for completion.

**Optional: Pull CodeLlama for better code generation:**
```bash
ollama pull codellama
```

### Step 4: Test Ollama

```bash
ollama run llama3
```

Type a test prompt. Press `Ctrl+D` to exit.

### Step 5: Setup Backend Project

```bash
# Clone or create project directory
mkdir codepilot-local-llm
cd codepilot-local-llm

# Install dependencies
npm install
```

---

## Running the Server

### Development Mode (with auto-reload):
```bash
npm run dev
```

### Production Mode:
```bash
npm start
```

The server will start on `http://localhost:5000`

---

## API Documentation

### Health Check

**Endpoint:** `GET /health`

**Response:**
```json
{
  "status": "ok",
  "message": "CodePilot AI Backend is running"
}
```

### Generate AI Response

**Endpoint:** `POST /generate`

**Request Body:**
```json
{
  "prompt": "Write a function to reverse a string in JavaScript",
  "model": "llama3",
  "temperature": 0.7,
  "max_tokens": 500
}
```

**Parameters:**
- `prompt` (required): Your question or request
- `model` (optional): Model name (default: "llama3")
- `temperature` (optional): Creativity level 0-1 (default: 0.7)
- `max_tokens` (optional): Max response length

**Response:**
```json
{
  "success": true,
  "response": "Here's a function to reverse a string...",
  "model": "llama3",
  "created_at": "2024-01-01T12:00:00Z",
  "done": true,
  "total_duration": 1234567890,
  "prompt_eval_count": 25,
  "eval_count": 150
}
```

---

## Testing the API

### Using cURL:

```bash
curl -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Explain async/await in JavaScript"
  }'
```

### Using JavaScript (fetch):

```javascript
const response = await fetch('http://localhost:5000/generate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    prompt: 'Write a React component for a login form'
  })
});

const data = await response.json();
console.log(data.response);
```

### Using Postman:

1. Method: POST
2. URL: `http://localhost:5000/generate`
3. Headers: `Content-Type: application/json`
4. Body (raw JSON):
```json
{
  "prompt": "Create a Python function to sort a list"
}
```

---

## Configuration

Edit `.env` file to customize:

```env
PORT=5000
OLLAMA_URL=http://localhost:11434
```

---

## Available Models

List installed models:
```bash
ollama list
```

Pull additional models:
```bash
ollama pull codellama        # Best for code
ollama pull llama3:70b       # Larger, more capable
ollama pull mistral          # Fast alternative
```

Change model in API request:
```json
{
  "prompt": "Your prompt",
  "model": "codellama"
}
```

---

## Error Handling

The API returns structured errors:

**Missing prompt:**
```json
{
  "error": "Prompt is required",
  "success": false
}
```

**Ollama not running:**
```json
{
  "success": false,
  "error": "Cannot connect to Ollama. Make sure Ollama is running (ollama serve)",
  "details": "Connection refused to http://localhost:11434"
}
```

---

## Production Deployment

### Using PM2:

```bash
npm install -g pm2
pm2 start server.js --name codepilot-ai
pm2 save
pm2 startup
```

### Using Docker:

Create `Dockerfile`:
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install --production
COPY . .
EXPOSE 5000
CMD ["npm", "start"]
```

Build and run:
```bash
docker build -t codepilot-ai .
docker run -p 5000:5000 codepilot-ai
```

---

## System Prompt

The system includes a built-in prompt that shapes AI behavior:

> "You are CodePilot AI, a professional full-stack development assistant. You provide clear, accurate, and production-ready code solutions. You understand modern web technologies, best practices, and clean code principles."

Modify in `server.js` to customize AI personality.

---

## Troubleshooting

**Issue: "Cannot connect to Ollama"**
- Solution: Run `ollama serve` in a separate terminal

**Issue: "Model not found"**
- Solution: Run `ollama pull llama3`

**Issue: Slow responses**
- Solution: Use smaller models or increase RAM
- Try: `ollama pull llama3:8b` (smaller variant)

**Issue: Port already in use**
- Solution: Change PORT in `.env` file

---

## Performance Tips

1. **Use CodeLlama for code tasks** - Better at programming
2. **Adjust temperature** - Lower (0.3) for factual, higher (0.9) for creative
3. **Limit max_tokens** - Faster responses with token limits
4. **Keep Ollama running** - Avoid cold starts

---

## Next Steps for SaaS Integration

1. Add authentication (JWT tokens)
2. Implement rate limiting
3. Add request logging and analytics
4. Create user session management
5. Add streaming responses for real-time output
6. Implement caching layer
7. Add multiple model support
8. Create admin dashboard

---

## License

MIT

---

## Support

For issues with:
- **Ollama**: https://github.com/ollama/ollama
- **This backend**: Create an issue in the repository
