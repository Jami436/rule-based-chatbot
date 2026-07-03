import unittest

from app.normalizer import normalize_input

class TestNormalizer(unittest.TestCase):

    def test_lowercase(self):
        self.assertEqual(
            normalize_input("HELLO"),
            "hello"
        )

    def test_strip_whitespace(self):
        self.assertEqual(
            normalize_input("   hello   "),
            "hello"
        )

    def test_empty_string(self):
        self.assertEqual(
            normalize_input(""),
            ""
        )

if __name__ == "__main__":
    unittest.main()