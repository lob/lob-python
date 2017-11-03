import unittest
import lob


class TestLob(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'asdf'
        lob.api_version = 'apiVersion'

    def test_bad_auth(self):
        self.assertRaises(lob.error.AuthenticationError, lob.Address.list)

    def test_set_version(self):
        self.assertEqual(lob.api_version, 'apiVersion')

    def tearDown(self):
        del lob.api_version
