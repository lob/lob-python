import unittest
import lob


class TestUSAutocompletionFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'

    def test_us_autocompletion(self):
        autocompletion = lob.USAutocompletion.create(
            address_prefix='185 BER',
            city='SAN FRANCISCO',
            state='CA'
        )

        self.assertEqual('suggestions' in autocompletion, True)
        self.assertEqual(autocompletion.suggestions[0].primary_line, 'TEST KEYS DO NOT AUTOCOMPLETE US ADDRESSES')
