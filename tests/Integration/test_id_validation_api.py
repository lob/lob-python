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
from lob_python.api.identity_validation_api import IdentityValidationApi  # noqa: E501
from lob_python.model.multi_line_address import MultiLineAddress

class TestIdentityValidationApi(unittest.TestCase):
    """IdentityValidationApi unit test stubs"""

    @classmethod
    def setUpClass(self):
        load_dotenv()
        warnings.simplefilter("ignore", ResourceWarning)
        self.configuration = lob_python.Configuration(
            username = os.getenv('LOB_API_LIVE_KEY')
        )
        with lob_python.ApiClient(self.configuration) as self.api_client:
            self.api = IdentityValidationApi(self.api_client)  # noqa: E501

    @classmethod
    def tearDownClass(self):
        del self.api
        del self.configuration

    def test_lookup_recipient(self):
        """Test case for identity_validation

        lookup  # noqa: E501
        """
        mlAddr = MultiLineAddress(
            recipient = "MORTICIA ADDAMS",
            primary_line = "001 CEMETERY LN",
            secondary_line = "SUITE 666",
            city = "WESTFIELD",
            state = "NJ",
            zip_code = "07000"
        )

        idv = self.api.validate(mlAddr)
        self.assertIn("id_validation", idv.id)
        self.assertFalse(idv['score'])

    def test_lookup_company(self):
        """Test case for identity_validation

        lookup  # noqa: E501
        """
        mlAddr = MultiLineAddress(
            company = "THE ADDAMS TRUST",
            primary_line = "001 CEMETERY LN",
            secondary_line = "SUITE 666",
            city = "WESTFIELD",
            state = "NJ",
            zip_code = "07000"
        )

        idv = self.api.validate(mlAddr)
        self.assertIn("id_validation", idv.id)
        self.assertFalse(idv['score'])

    def test_invalid_lookup(self):
        """Test case for identity_validation

        lookup  # noqa: E501
        """
        mlAddr = MultiLineAddress(
            recipient = "MORTICIA ADDAMS",
            company = "THE ADDAMS TRUST",
            primary_line = "001 CEMETERY LN",
            secondary_line = "SUITE 666",
            city = "WESTFIELD",
            state = "NJ",
            zip_code = "07000"
        )

        with self.assertRaises(Exception) as context:
            self.api.validate(mlAddr)
        self.assertTrue("only recipient or company is allowed" in context.exception.__str__())

    def test_lookup_error(self):
        """Test case for identity_validation

        lookup  # noqa: E501
        """
        mlAddr = MultiLineAddress(
            recipient = "MORTICIA ADDAMS",
            primary_line = "001 CEMETERY LN",
            secondary_line = "SUITE 666",
            city = "WESTFIELD",
            state = "NJ",
            zip_code = "ABCDE"
        )

        with self.assertRaises(Exception) as context:
            self.api.validate(mlAddr)
        self.assertTrue("zip_code must be in a valid zip or zip+4 format" in context.exception.__str__())


if __name__ == '__main__':
    unittest.main()
