import unittest

from app.guardrails import validate_input


class TestGuardrails(unittest.TestCase):

    def test_empty_input(self):
        valid, _ = validate_input("")
        self.assertFalse(valid)

    def test_whitespace_input(self):
        valid, _ = validate_input("      ")
        self.assertFalse(valid)

    def test_valid_input(self):
        valid, _ = validate_input("hello")
        self.assertTrue(valid)

    def test_long_input(self):
        valid, _ = validate_input("a" * 101)
        self.assertFalse(valid)


if __name__ == "__main__":
    unittest.main()