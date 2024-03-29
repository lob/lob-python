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
from lob_python.api.reverse_geocode_lookups_api import ReverseGeocodeLookupsApi  # noqa: E501
from lob_python.model.location import Location


class TestReverseGeocodeLookupsApi(unittest.TestCase):
    """ReverseGeocodeLookupsApi unit test stubs"""

    @classmethod
    def setUpClass(self):
        load_dotenv()
        warnings.simplefilter("ignore", ResourceWarning)
        self.configuration = lob_python.Configuration(
            username = os.getenv('LOB_API_LIVE_KEY')
        )
        with lob_python.ApiClient(self.configuration) as self.api_client:
            self.api = ReverseGeocodeLookupsApi(self.api_client)  # noqa: E501

        self.location = Location(
            latitude = 37.777456,
            longitude = -122.393039,
        )

    @classmethod
    def tearDownClass(self):
        del self.location
        del self.api
        del self.configuration

    def test_401(self):
        """Test case for lookup with status code 401"""
        configuration = lob_python.Configuration(
            username = "Totally fake key"
        )

        with self.assertRaises(Exception) as context:
            with lob_python.ApiClient(configuration) as api_client:
                invalid_api = ReverseGeocodeLookupsApi(api_client)  # noqa: E501
                invalid_api.lookup(self.location, size = 3)
        self.assertTrue("Your API key is not valid. Please sign up on lob.com" in context.exception.__str__())

    def test_lookup(self):
        """Test case for reverse_geocode_lookup

        lookup  # noqa: E501
        """
        size = 3

        rgl = self.api.lookup(self.location, size = size)
        self.assertGreaterEqual(len(rgl.addresses), 1)
        self.assertIn("us_reverse_geocode", rgl.id)

    def test_lookup_error(self):
        """Test case for reverse_geocode_lookup

        lookup  # noqa: E501
        """
        size = 51

        with self.assertRaises(Exception) as context:
            self.api.lookup(self.location, size = size)
        self.assertTrue("Invalid value for `size`, must be a value less than or equal to `50`" in context.exception.__str__())


if __name__ == '__main__':
    unittest.main()
