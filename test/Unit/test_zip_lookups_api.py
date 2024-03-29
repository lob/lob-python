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
from lob_python.api.zip_lookups_api import ZipLookupsApi  # noqa: E501
from lob_python.model.zip_editable import ZipEditable
from lob_python.exceptions import UnauthorizedException, NotFoundException, ApiException
from unittest.mock import Mock, MagicMock

class TestZipLookupsApi(unittest.TestCase):
    """ZipLookupsApi unit test stubs"""

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.config_for_unit = lob_python.Configuration(
            username = "Totally Fake Key"
        )
        with lob_python.ApiClient(self.config_for_unit) as self.api_client:
            self.mock_api = ZipLookupsApi(self.api_client)

        self.zip_editable = ZipEditable(zip_code = "07090")

    def test_zip_lookup(self):
        """Test case for zip lookup"""
        self.mock_api.zip_lookup = MagicMock(return_value={
            "id": "us_zip_fakeId"
        })
        response = self.mock_api.zip_lookup(self.zip_editable)
        self.assertIsNotNone(response)
        self.assertEqual(response["id"], "us_zip_fakeId")

    def test_zip_lookup_with_custom_headers(self):
        """Test case for zip lookup with custom headers"""
        self.mock_api.zip_lookup = MagicMock(return_value={
            "id": "us_zip_fakeId"
        })
        response = self.mock_api.zip_lookup(self.zip_editable, _content_type="application/json")
        self.assertIsNotNone(response)
        self.assertEqual(response["id"], "us_zip_fakeId")

    def test_zip_lookup_error_handle(self):
        """Test case for handling zip lookup error"""
        self.mock_api.zip_lookup = Mock(side_effect=UnauthorizedException(status=401, reason="Unauthorized"))

        with self.assertRaises(Exception) as context:
            self.mock_api.zip_lookup(self.zip_editable)
        self.assertTrue("Unauthorized" in context.exception.__str__())

if __name__ == '__main__':
    unittest.main()
