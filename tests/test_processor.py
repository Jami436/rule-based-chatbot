import unittest

from app.processor import process_intent
from app.constants import FALLBACK_RESPONSE


class TestProcessor(unittest.TestCase):

    def test_known_intent(self):
        self.assertEqual(
            process_intent("hello"),
            "Hello! How can I help you today?"
        )

    def test_unknown_intent(self):
        self.assertEqual(
            process_intent("random_text"),
            FALLBACK_RESPONSE
        )

    def test_help_command(self):
        response = process_intent("help")
        self.assertIn("Available commands", response)

    def test_hi_alias(self):
        self.assertEqual(
            process_intent("hi"),
            "Hello! How can I help you today?"
        )

    def test_hey_alias(self):
        self.assertEqual(
            process_intent("hey"),
            "Hello! How can I help you today?"
        )

    def test_commands_alias(self):
        response = process_intent("commands")
        self.assertIn("Available commands", response)

    def test_capabilities_intent(self):
        response = process_intent("what can you do")
        self.assertIn("guardrails", response)

    def test_capabilities_alias(self):
        response = process_intent("what do you do")
        self.assertIn("guardrails", response)


if __name__ == "__main__":
    unittest.main()