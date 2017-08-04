import unittest
import lob

class TestUSZipLookupFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'

    def test_us_zip_lookup(self):
        zip_lookup = lob.USZipLookup.create(
            zip_code='94107'
        )

        self.assertEqual(zip_lookup.zip_code, '94107')
        self.assertEqual(zip_lookup.zip_code_type, 'standard')
