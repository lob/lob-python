"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> Looking for our [previous documentation](https://lob.github.io/legacy-docs/)?   # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: lob-openapi@lob.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import warnings

import lob_python
import os
from dotenv import load_dotenv
from lob_python.api.zip_lookups_api import ZipLookupsApi  # noqa: E501
from lob_python.model.zip_editable import ZipEditable


class TestZipLookupsApi(unittest.TestCase):
    """ZipLookupsApi unit test stubs"""

    @classmethod
    def setUpClass(self):
        load_dotenv()
        warnings.simplefilter("ignore", ResourceWarning)
        self.configuration = lob_python.Configuration(
            username = os.getenv('LOB_API_LIVE_KEY')
        )
        with lob_python.ApiClient(self.configuration) as self.api_client:
            self.api = ZipLookupsApi(self.api_client)  # noqa: E501

        self.zip = ZipEditable(
            zip_code = "94107"
        )

    @classmethod
    def tearDownClass(self):
        del self.api
        del self.configuration

    def test_401(self):
        """Test case for random op with status code 401"""
        configuration = lob_python.Configuration(
            username = "Totally fake key"
        )
        with lob_python.ApiClient(configuration) as api_client:
            invalid_api = ZipLookupsApi(api_client)  # noqa: E501

        with self.assertRaises(Exception) as context:
            invalid_api.lookup(self.zip)
        self.assertTrue("Your API key is not valid" in context.exception.__str__())

    def test_lookup(self):
        """Test case for zip_lookup

        lookup  # noqa: E501
        """
        zl = self.api.lookup(self.zip)
        self.assertGreaterEqual(len(zl.cities), 1)
        self.assertIn("us_zip", zl.id)

    def test_lookup_error(self):
        """Test case for zip_lookup

        lookup  # noqa: E501
        """
        zip = ZipEditable(
            zip_code = "00000"
        )

        with self.assertRaises(Exception) as context:
            self.api.lookup(zip)
        self.assertTrue("invalid zip code" in context.exception.__str__())


if __name__ == '__main__':
    unittest.main()
