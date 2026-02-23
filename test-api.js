// Simple test script to verify the API works
const axios = require('axios');

const API_URL = 'http://localhost:5001';

async function testAPI() {
  console.log('🧪 Testing CodePilot AI Backend...\n');

  try {
    // Test 1: Health check
    console.log('Test 1: Health Check');
    const healthResponse = await axios.get(`${API_URL}/health`);
    console.log('✅ Health check passed:', healthResponse.data);
    console.log('');

    // Test 2: Simple generation
    console.log('Test 2: AI Generation');
    const genResponse = await axios.post(`${API_URL}/generate`, {
      prompt: 'Write a simple hello world function in JavaScript',
      temperature: 0.7
    });
    
    console.log('✅ Generation successful!');
    console.log('Response:', genResponse.data.response.substring(0, 200) + '...');
    console.log('Model:', genResponse.data.model);
    console.log('Tokens generated:', genResponse.data.eval_count);
    console.log('');

    console.log('🎉 All tests passed!');

  } catch (error) {
    console.error('❌ Test failed:', error.message);
    if (error.response) {
      console.error('Error details:', error.response.data);
    }
  }
}

testAPI();
