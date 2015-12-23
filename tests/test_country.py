import unittest
import lob

class CountryFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'

    def test_countries(self):
        countries = lob.Country.list()
        self.assertTrue(isinstance(countries.data, list))
