// In static/js/chatbot.js - USE THIS ENDPOINT:
fetch('/api/chat', {  // This calls the EXTERNAL endpoint
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    query: userMessage,
    api_key: botApiKey  // From the script tag
  })
})