import unittest
import lob

class TestLob(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'asdf'

    def test_bad_auth(self):
        self.assertRaises(lob.error.AuthenticationError, lob.Address.list)
