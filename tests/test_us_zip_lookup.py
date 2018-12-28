import unittest
import os
import lob


class TestUSZipLookupFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = os.environ.get('LOB_API_KEY')

    def test_us_zip_lookup(self):
        zip_lookup = lob.USZipLookup.create(
            zip_code='94107'
        )

        self.assertEqual(zip_lookup.zip_code, '94107')
        self.assertEqual(zip_lookup.zip_code_type, 'standard')
