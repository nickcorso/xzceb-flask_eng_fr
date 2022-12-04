import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        # Hello doesn't return Bonjour
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        # None string returns empty strings
        self.assertNotEqual(english_to_french('None'), '')
        # Empty string returns empty strings
        self.assertNotEqual(english_to_french(0), 0)
        # Hello returns Bonjour
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_french_to_english(self):
        # Bonjour doesn't return Hello
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
        # Empty string returns empty strings
        self.assertNotEqual(french_to_english('None'), '')
        # Empty string returns empty strings
        self.assertNotEqual(french_to_french(0), 0)
        # Bonjour returns Hello
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()