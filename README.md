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
   
## Running Unit Tests

To run the unit tests for the chatbot, follow these steps:

### Using PyCharm

1. Open the `test_chatbot.py` file in PyCharm.
2. Right-click anywhere inside the `test_chatbot.py` file.
3. Select **"Run 'Unittests in test_chatbot.py'"** from the context menu.

Alternatively, you can:

1. Open the `test_chatbot.py` file in PyCharm.
2. Click on the green play button next to the class or method you want to test.
3. Select **"Run 'Unittests in test_chatbot.py'"** from the context menu.

### Using the Command Line

1. Navigate to the project directory.
2. Run the following command:

    ```sh
    python -m unittest discover
    ```

This will discover and run all the unit tests in the project.