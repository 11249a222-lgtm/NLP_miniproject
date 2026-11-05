"""Basic tests for the chatbot matching logic. Run: python -m unittest"""
import unittest
from chatbot import CollegeChatbot
from knowledge_base import COLLEGE_FAQS

class TestCollegeChatbot(unittest.TestCase):
    def setUp(self):
        self.bot = CollegeChatbot(COLLEGE_FAQS)

    def test_greeting(self):
        self.assertIn("Hello", self.bot.get_response("Hi"))

    def test_admission_question(self):
        answer = self.bot.get_response("How can I apply for admission?")
        self.assertIn("admission", answer.lower())

    def test_empty_question(self):
        self.assertEqual(self.bot.get_response(""), "Please type a question.")

if __name__ == "__main__":
    unittest.main()
