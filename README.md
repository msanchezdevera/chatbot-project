# Simple Chatbot Project

This is a simple chatbot project built with Python and Flask. The chatbot can respond to basic greetings and FAQs.

## Setup Instructions

1. Create and activate a virtual environment:
   ```bash
   python -m venv chatbot-env
   .\chatbot-env\Scripts\activate
   
2. Install the required packages:
   ```bash
   pip install -r requirements.txt

3. Run the Flask app:
   ```bash
   python chatbot.py


## Testing the Chatbot with Postman

1. Import the Postman collection from the `postman` directory.

2. Test the chatbot by sending a POST request to the `/chat` endpoint with the following JSON payload:
   ```json
   {
       "message": "Hello"
   }