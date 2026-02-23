// CodePilot AI Demo Examples
// Run these examples to see the AI in action

const axios = require('axios');

const API_URL = 'http://localhost:5001/generate';

// Helper function to make API calls
async function askAI(prompt, temperature = 0.7, maxTokens = null) {
  console.log('\n' + '='.repeat(80));
  console.log('PROMPT:', prompt);
  console.log('='.repeat(80));
  
  try {
    const response = await axios.post(API_URL, {
      prompt,
      temperature,
      max_tokens: maxTokens
    });
    
    console.log('\nRESPONSE:');
    console.log(response.data.response);
    console.log('\n📊 Stats:');
    console.log(`- Model: ${response.data.model}`);
    console.log(`- Tokens: ${response.data.eval_count}`);
    console.log(`- Time: ${(response.data.total_duration / 1000000000).toFixed(2)}s`);
    
    return response.data;
  } catch (error) {
    console.error('❌ Error:', error.message);
  }
}

// Demo Examples
async function runDemos() {
  console.log('🚀 CodePilot AI Demo - Showcasing Capabilities\n');
  
  // Example 1: Code Generation
  await askAI(
    'Create a Node.js Express middleware for logging HTTP requests',
    0.7
  );
  
  // Example 2: Bug Finding
  await askAI(
    'What is wrong with this SQL query? SELECT * FROM users WHERE id = "5" AND status = active',
    0.3
  );
  
  // Example 3: Code Explanation
  await askAI(
    'Explain what this regex does: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/',
    0.5
  );
  
  // Example 4: Algorithm Implementation
  await askAI(
    'Write a function to find the longest palindrome substring in a string',
    0.6
  );
  
  // Example 5: Best Practices
  await askAI(
    'What are the security best practices for storing passwords in a database?',
    0.5,
    200
  );
  
  console.log('\n' + '='.repeat(80));
  console.log('✅ Demo Complete!');
  console.log('='.repeat(80));
}

// Run the demos
runDemos().catch(console.error);
