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
import os
from lob_python.model.bank_account_verify import BankAccountVerify
from lob_python.model.bank_type_enum import BankTypeEnum
from lob_python.api.bank_accounts_api import BankAccountsApi  # noqa: E501
from lob_python.model.bank_account_writable import BankAccountWritable  # noqa: E501
from lob_python.model.metadata_model import MetadataModel
from lob_python.model.include_model import IncludeModel
from lob_python.exceptions import UnauthorizedException, NotFoundException, ApiException
from unittest.mock import Mock, MagicMock

class TestBankAccountsApi(unittest.TestCase):
    """BankAccountsApi unit test stubs"""

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.config_for_unit = lob_python.Configuration(
            username = "Totally Fake Key"
        )
        with lob_python.ApiClient(self.config_for_unit) as self.api_client:
            self.mock_api = BankAccountsApi(self.api_client)

        self.bank_account_writable = BankAccountWritable(
            routing_number = "123456789",
            account_number = "fake account",
            account_type = BankTypeEnum('individual'),
            signatory = "fake signatory",
        )

        self.bank_account_verify = BankAccountVerify(
          amounts = [1, 2]
        )

        self.mock_list_of_bank_accounts =  MagicMock(return_value={
            "data": [{ "id": "fake 1" }, { "id": "fake 2" }]
        })

    def test_bank_account_create_error_handle(self):
        """Test case for handling create error"""
        self.mock_api.bank_account_create = Mock(side_effect=UnauthorizedException(status=401, reason="Unauthorized"))

        with self.assertRaises(Exception) as context:
            self.mock_api.bank_account_create(self.bank_account_writable)
        self.assertTrue("Unauthorized" in context.exception.__str__())

    def test_bank_account_create(self):
        """Test case for creating new bank account"""
        self.mock_api.bank_account_create = MagicMock(return_value={
            "id": "bank_fakeId"
        })
        created_bank_account = self.mock_api.bank_account_create(self.bank_account_writable)
        self.assertIsNotNone(created_bank_account)
        self.assertIsNotNone(created_bank_account["id"])

    def test_bank_account_create_with_custom_headers(self):
        """Test case for creating new bank account with custom headers"""
        self.mock_api.bank_account_create = MagicMock(return_value={
            "id": "bank_fakeId"
        })
        created_bank_account = self.mock_api.bank_account_create(self.bank_account_writable, _content_type="application/json")
        self.assertIsNotNone(created_bank_account)
        self.assertIsNotNone(created_bank_account["id"])

    def test_bank_account_retrieve(self):
        """Test case for retrieving bank account"""
        self.mock_api.bank_account_retrieve = MagicMock(return_value={
            "id": "bank_differentFakeId"
        })
        retrieved_bank_account = self.mock_api.bank_account_retrieve("bank_fakeId")
        self.assertEqual(retrieved_bank_account["id"], "bank_differentFakeId")

    def test_bank_account_retrieve_with_custom_headers(self):
        """Test case for retrieving bank account with custom headers"""
        self.mock_api.bank_account_retrieve = MagicMock(return_value={
            "id": "bank_differentFakeId"
        })
        retrieved_bank_account = self.mock_api.bank_account_retrieve("bank_fakeId", _content_type="application/json")
        self.assertEqual(retrieved_bank_account["id"], "bank_differentFakeId")

    def test_bank_account_retrieve_error_handle(self):
        """Test case for handling retrieve error"""
        self.mock_api.bank_account_retrieve = Mock(side_effect=NotFoundException(status=404, reason="Not Found"))

        with self.assertRaises(Exception) as context:
            self.mock_api.bank_account_retrieve("bank_fakeId")
        self.assertTrue("Not Found" in context.exception.__str__())

    def test_bank_account_verify(self):
      """Test case for verifying bank account"""
      self.mock_api.bank_account_verify = MagicMock(return_value={
          "id": "bank_fakeId"
      })

      verified_bank_account = self.mock_api.bank_account_verify(self.bank_account_verify)
      self.assertEqual(verified_bank_account["id"], "bank_fakeId")

    def test_bank_account_verify_with_custom_headers(self):
      """Test case for verifying bank account with custom headers"""
      self.mock_api.bank_account_verify = MagicMock(return_value={
          "id": "bank_fakeId"
      })

      verified_bank_account = self.mock_api.bank_account_verify(self.bank_account_verify, _content_type="application/json")
      self.assertEqual(verified_bank_account["id"], "bank_fakeId")

    def test_bank_account_verify_error_handle(self):
      """Test case for handling verify error"""
      self.mock_api.bank_account_verify = Mock(side_effect=UnauthorizedException(status=401, reason="Unauthorized"))

      with self.assertRaises(Exception) as context:
          self.mock_api.bank_account_verify(self.bank_account_verify)
      self.assertTrue("Unauthorized" in context.exception.__str__())

    def test_bank_accounts_list(self):
        """Test case for listing bank accounts"""
        self.mock_api.bank_accounts_list = self.mock_list_of_bank_accounts
        bank_accounts = self.mock_api.bank_accounts_list()
        self.assertIsNotNone(bank_accounts)
        self.assertEqual(len(bank_accounts["data"]), 2)

    def test_bank_accounts_list_with_custom_headers(self):
        """Test case for listing bank accounts with custom headers"""
        self.mock_api.bank_accounts_list = self.mock_list_of_bank_accounts
        bank_accounts = self.mock_api.bank_accounts_list(_content_type="application/json")
        self.assertIsNotNone(bank_accounts)
        self.assertEqual(len(bank_accounts["data"]), 2)

    def test_bank_accounts_list_error_handle(self):
        """Test case for handling list error"""
        msg = """Cannot prepare a request message for provided
                    arguments. Please check that your arguments match
                    declared content type."""
        self.mock_api.bank_accounts_list = Mock(side_effect=ApiException(status=0, reason=msg))

        with self.assertRaises(Exception) as context:
            self.mock_api.bank_accounts_list()
        self.assertTrue("Cannot prepare a request message" in context.exception.__str__())

    def test_bank_accounts_list_with_limit_param(self):
        """Test case for listing bank accounts with limit parameter"""
        self.mock_api.bank_accounts_list = self.mock_list_of_bank_accounts
        bank_accounts = self.mock_api.bank_accounts_list(limit=10)
        self.assertIsNotNone(bank_accounts)
        self.assertEqual(len(bank_accounts["data"]), 2)

    def test_bank_accounts_list_with_before_param(self):
        """Test case for listing bank accounts with before parameter"""
        self.mock_api.bank_accounts_list = self.mock_list_of_bank_accounts
        bank_accounts = self.mock_api.bank_accounts_list(before="before")
        self.assertIsNotNone(bank_accounts)
        self.assertEqual(len(bank_accounts["data"]), 2)

    def test_bank_accounts_list_with_after_param(self):
        """Test case for listing bank accounts with after parameter"""
        self.mock_api.bank_accounts_list = self.mock_list_of_bank_accounts
        bank_accounts = self.mock_api.bank_accounts_list(after="after")
        self.assertIsNotNone(bank_accounts)
        self.assertEqual(len(bank_accounts["data"]), 2)

    def test_bank_accounts_list_with_include_param(self):
        """Test case for listing bank accounts with include parameter"""
        self.mock_api.bank_accounts_list = self.mock_list_of_bank_accounts
        bank_accounts = self.mock_api.bank_accounts_list(include=IncludeModel(["total_count"]))
        self.assertIsNotNone(bank_accounts)
        self.assertEqual(len(bank_accounts["data"]), 2)

    def test_bank_accounts_list_with_dateCreated_param(self):
        """Test case for listing bank accounts with date_created parameter"""
        self.mock_api.bank_accounts_list = self.mock_list_of_bank_accounts
        bank_accounts = self.mock_api.bank_accounts_list(date_created={ "gt": "2020-01-01", "lt": "2020-01-31T12" })
        self.assertIsNotNone(bank_accounts)
        self.assertEqual(len(bank_accounts["data"]), 2)

    def test_bank_accounts_list_with_metadata_param(self):
        """Test case for listing bank accounts with metadata parameter"""
        self.mock_api.bank_accounts_list = self.mock_list_of_bank_accounts
        bank_accounts = self.mock_api.bank_accounts_list(metadata=MetadataModel(fakeMetadata = "fakeMetadata"))
        self.assertIsNotNone(bank_accounts)
        self.assertEqual(len(bank_accounts["data"]), 2)

    def test_bank_account_delete(self):
        """Test case for deleting bank account"""
        self.mock_api.bank_account_delete = MagicMock(return_value={
            "id": "bank_fakeId", "deleted": True
        })
        deleted_bank_account = self.mock_api.bank_account_delete("bank_fakeId")
        self.assertTrue(deleted_bank_account["deleted"])

    def test_bank_account_delete_with_custom_headers(self):
        """Test case for deleting bank account with custom headers"""
        self.mock_api.bank_account_delete = MagicMock(return_value={
            "id": "bank_fakeId", "deleted": True
        })
        deleted_bank_account = self.mock_api.bank_account_delete("bank_fakeId", _content_type="application/json")
        self.assertTrue(deleted_bank_account["deleted"])

    def test_bank_account_delete_error_handle(self):
        """Test case for handling delete error"""
        self.mock_api.bank_account_delete = Mock(side_effect=NotFoundException(status=404, reason="Not Found"))

        with self.assertRaises(Exception) as context:
            self.mock_api.bank_account_delete("bank_fakeId")
        self.assertTrue("Not Found" in context.exception.__str__())

if __name__ == '__main__':
    unittest.main()
