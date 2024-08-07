# test_chatbot.py
import unittest
from flask import json
from chatbot import app

class ChatbotTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hi_response(self):
        response = self.app.post('/chatbot', json={"message": "hi"})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['response'], "Hello! How can I help you today?")

    def test_hello_response(self):
        response = self.app.post('/chatbot', json={"message": "hello"})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['response'], "Hi there! How can I assist you?")

    def test_unknown_response(self):
        response = self.app.post('/chatbot', json={"message": "unknown"})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['response'], "I'm sorry, I don't understand that. Can you please rephrase?")

if __name__ == '__main__':
    unittest.main()