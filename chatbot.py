from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample responses for the chatbot
responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! How can I assist you?",
    "how are you": "I'm a bot, but I'm here to help you!",
    "what is your name": "I'm your friendly chatbot!",
    "bye": "Goodbye! Have a great day!",
    "help": "I'm here to assist you with any questions you have.",
}

# Function to get a response from the chatbot
def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I don't understand that. Can you please rephrase?")

# Route for the chatbot
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message')
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
