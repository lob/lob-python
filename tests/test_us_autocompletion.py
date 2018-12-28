import unittest
import os
import lob


class TestUSAutocompletionFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = os.environ.get('LOB_API_KEY')

    def test_us_autocompletion(self):
        autocompletion = lob.USAutocompletion.create(
            address_prefix='185 BER',
            city='SAN FRANCISCO',
            state='CA'
        )

        self.assertEqual('suggestions' in autocompletion, True)
        self.assertEqual(autocompletion.suggestions[0].primary_line, 'TEST KEYS DO NOT AUTOCOMPLETE US ADDRESSES')
