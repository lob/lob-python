"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> Looking for our [previous documentation](https://lob.github.io/legacy-docs/)?   # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: lob-openapi@lob.com
    Generated by: https://openapi-generator.tech
"""

import string
import unittest
import warnings

import lob_python
from lob_python.api.reverse_geocode_lookups_api import ReverseGeocodeLookupsApi  # noqa: E501
from lob_python.model.location import Location  # noqa: E501
from lob_python.exceptions import UnauthorizedException, NotFoundException, ApiException
from unittest.mock import Mock, MagicMock

class TestReverseGeocodeLookupsApi(unittest.TestCase):
    """ReverseGeocodeLookupsApi unit test stubs"""

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.config_for_unit = lob_python.Configuration(
            username = "Totally Fake Key"
        )
        with lob_python.ApiClient(self.config_for_unit) as self.api_client:
            self.mock_api = ReverseGeocodeLookupsApi(self.api_client)

        self.location = Location(
            latitude = 10.0518,
            longitude = 77.5677,
        )

    def test_lookup_geocode(self):
        """Test for looking up geocode"""
        self.mock_api.reverse_geocode_lookup = MagicMock(return_value={
            "id": "us_reverse_geocode_fakeId"
        })
        geocode_result = self.mock_api.reverse_geocode_lookup(self.location)
        self.assertIsNotNone(geocode_result)
        self.assertEqual(geocode_result["id"], "us_reverse_geocode_fakeId")

    def test_lookup_geocode_with_size(self):
        """Test for looking up geocode with size"""
        self.mock_api.reverse_geocode_lookup = MagicMock(return_value={
            "id": "us_reverse_geocode_fakeId"
        })
        geocode_result = self.mock_api.reverse_geocode_lookup(self.location, size=2)
        self.assertIsNotNone(geocode_result)
        self.assertEqual(geocode_result["id"], "us_reverse_geocode_fakeId")

    def test_lookup_geocode_with_custom_headers(self):
        """Test for looking up geocode with custom headers"""
        self.mock_api.reverse_geocode_lookup = MagicMock(return_value={
            "id": "us_reverse_geocode_fakeId"
        })
        geocode_result = self.mock_api.reverse_geocode_lookup(self.location, _content_type="application/json")
        self.assertIsNotNone(geocode_result)
        self.assertEqual(geocode_result["id"], "us_reverse_geocode_fakeId")

    def test_lookup_geocode_error_handle(self):
        """Test case for handling geocode lookup error"""
        self.mock_api.reverse_geocode_lookup = Mock(side_effect=UnauthorizedException(status=401, reason="Unauthorized"))

        with self.assertRaises(Exception) as context:
            self.mock_api.reverse_geocode_lookup(self.location)
        self.assertTrue("Unauthorized" in context.exception.__str__())

if __name__ == '__main__':
    unittest.main()
