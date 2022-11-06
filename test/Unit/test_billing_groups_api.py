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
from lob_python.api.billing_groups_api import BillingGroupsApi  # noqa: E501
from lob_python.model.billing_group_editable import BillingGroupEditable
from lob_python.model.include_model import IncludeModel
from lob_python.model.sort_by3 import SortBy3
from lob_python.exceptions import UnauthorizedException, NotFoundException, ApiException
from unittest.mock import Mock, MagicMock

class TestBillingGroupsApi(unittest.TestCase):
    """BillingGroupsApi unit test stubs"""

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.config_for_unit = lob_python.Configuration(
            username = "Totally Fake Key"
        )
        with lob_python.ApiClient(self.config_for_unit) as self.api_client:
            self.mock_api = BillingGroupsApi(self.api_client)
        self.billing_group_editable = BillingGroupEditable(
          name = "fake billing group name",
          description = "fake billing group description",
        )
        self.updated_billing_group_editable = BillingGroupEditable(
          name = "billing group updated",
          description = "billing group updated",
        )
        self.mock_api.billing_group_update = MagicMock(return_value={
          "id": "bg_fakeId",
          "name": self.updated_billing_group_editable["name"],
          "description": self.updated_billing_group_editable["description"],
        })
        self.mock_list_of_billing_groups =  MagicMock(return_value={
            "data": [{ "id": "fake 1" }, { "id": "fake 2" }]
        })

    def test_billing_group_create_error_handle(self):
        """Test case for handling create error"""
        self.mock_api.billing_group_create = Mock(side_effect=UnauthorizedException(status=401, reason="Unauthorized"))

        with self.assertRaises(Exception) as context:
            self.mock_api.billing_group_create(self.billing_group_editable)
        self.assertTrue("Unauthorized" in context.exception.__str__())

    def test_billing_group_create(self):
        """Test case for creating new billing group"""
        self.mock_api.billing_group_create = MagicMock(return_value={
            "id": "bg_fakeId"
        })
        created_billing_group = self.mock_api.billing_group_create(self.billing_group_editable)
        self.assertIsNotNone(created_billing_group)
        self.assertIsNotNone(created_billing_group["id"])

    def test_billing_group_create_with_custom_headers(self):
        """Test case for creating new billing group with custom headers"""
        self.mock_api.billing_group_create = MagicMock(return_value={
            "id": "bg_fakeId"
        })
        created_billing_group = self.mock_api.billing_group_create(self.billing_group_editable, _content_type="application/json")
        self.assertIsNotNone(created_billing_group)
        self.assertIsNotNone(created_billing_group["id"])

    def test_billing_group_retrieve(self):
        """Test case for retrieving billing group"""
        self.mock_api.billing_group_retrieve = MagicMock(return_value={
            "id": "bg_differentFakeId"
        })
        retrieved_billing_group = self.mock_api.billing_group_retrieve("bg_fakeId")
        self.assertEqual(retrieved_billing_group["id"], "bg_differentFakeId")

    def test_billing_group_retrieve_with_custom_headers(self):
        """Test case for retrieving billing group with custom headers"""
        self.mock_api.billing_group_retrieve = MagicMock(return_value={
            "id": "bg_differentFakeId"
        })
        retrieved_billing_group = self.mock_api.billing_group_retrieve("bg_fakeId", _content_type="application/json")
        self.assertEqual(retrieved_billing_group["id"], "bg_differentFakeId")

    def test_billing_group_retrieve_error_handle(self):
        """Test case for handling retrieve error"""
        self.mock_api.billing_group_retrieve = Mock(side_effect=NotFoundException(status=404, reason="Not Found"))

        with self.assertRaises(Exception) as context:
            self.mock_api.billing_group_retrieve("bg_fakeId")
        self.assertTrue("Not Found" in context.exception.__str__())

    def test_billing_groups_list(self):
        """Test case for listing billing groups"""
        self.mock_api.billing_groups_list = self.mock_list_of_billing_groups
        billing_groups = self.mock_api.billing_groups_list()
        self.assertIsNotNone(billing_groups)
        self.assertEqual(len(billing_groups["data"]), 2)

    def test_billing_groups_list_with_custom_headers(self):
        """Test case for listing billing groups with custom headers"""
        self.mock_api.billing_groups_list = self.mock_list_of_billing_groups
        billing_groups = self.mock_api.billing_groups_list(_content_type="application/json")
        self.assertIsNotNone(billing_groups)
        self.assertEqual(len(billing_groups["data"]), 2)

    def test_billing_groups_list_error_handle(self):
        """Test case for handling list error"""
        msg = """Cannot prepare a request message for provided
                    arguments. Please check that your arguments match
                    declared content type."""
        self.mock_api.billing_groups_list = Mock(side_effect=ApiException(status=0, reason=msg))

        with self.assertRaises(Exception) as context:
            self.mock_api.billing_groups_list()
        self.assertTrue("Cannot prepare a request message" in context.exception.__str__())

    def test_billing_groups_list_with_limit_param(self):
        """Test case for listing billing groups with limit parameter"""
        self.mock_api.billing_groups_list = self.mock_list_of_billing_groups
        billing_groups = self.mock_api.billing_groups_list(limit=10)
        self.assertIsNotNone(billing_groups)
        self.assertEqual(len(billing_groups["data"]), 2)

    def test_billing_groups_list_with_offset_param(self):
        """Test case for listing billing groups with offset parameter"""
        self.mock_api.billing_groups_list = self.mock_list_of_billing_groups
        billing_groups = self.mock_api.billing_groups_list(offset=1)
        self.assertIsNotNone(billing_groups)
        self.assertEqual(len(billing_groups["data"]), 2)

    def test_billing_groups_list_with_include_param(self):
        """Test case for listing billing groups with include parameter"""
        self.mock_api.billing_groups_list = self.mock_list_of_billing_groups
        billing_groups = self.mock_api.billing_groups_list(include=IncludeModel(["total_count"]))
        self.assertIsNotNone(billing_groups)
        self.assertEqual(len(billing_groups["data"]), 2)

    def test_billing_groups_list_with_dateCreated_param(self):
        """Test case for listing billing groups with date_created parameter"""
        self.mock_api.billing_groups_list = self.mock_list_of_billing_groups
        billing_groups = self.mock_api.billing_groups_list(date_created={ "gt": "2020-01-01", "lt": "2020-01-31T12" })
        self.assertIsNotNone(billing_groups)
        self.assertEqual(len(billing_groups["data"]), 2)

    def test_billing_groups_list_with_dateModified_param(self):
        """Test case for listing billing groups with date_modified parameter"""
        self.mock_api.billing_groups_list = self.mock_list_of_billing_groups
        billing_groups = self.mock_api.billing_groups_list(date_modified={ "gt": "2020-01-01", "lt": "2020-01-31T12" })
        self.assertIsNotNone(billing_groups)
        self.assertEqual(len(billing_groups["data"]), 2)

    def test_billing_groups_list_with_sort_by_param(self):
        """Test case for listing billing groups with sort_by parameter"""
        self.mock_api.billing_groups_list = self.mock_list_of_billing_groups
        billing_groups = self.mock_api.billing_groups_list(sort_by=SortBy3(date_created = 'asc'))
        self.assertIsNotNone(billing_groups)
        self.assertEqual(len(billing_groups["data"]), 2)

    def test_billing_group_update(self):
        """Test case for updating billing group"""
        updated_billing_group = self.mock_api.billing_group_update("bg_fakeId", self.updated_billing_group_editable)
        self.assertIsNotNone(updated_billing_group)
        self.assertEqual(updated_billing_group["name"], self.updated_billing_group_editable["name"])
        self.assertEqual(updated_billing_group["description"], self.updated_billing_group_editable["description"])

    def test_billing_group_update_with_custom_headers(self):
        """Test case for updating billing group"""
        updated_billing_group = self.mock_api.billing_group_update("bg_fakeId", self.updated_billing_group_editable, _content_type="application/json")
        self.assertIsNotNone(updated_billing_group)
        self.assertEqual(updated_billing_group["name"], self.updated_billing_group_editable["name"])
        self.assertEqual(updated_billing_group["description"], self.updated_billing_group_editable["description"])

    def test_billing_group_update_error_handle(self):
        """Test case for handling update error"""
        self.mock_api.billing_group_update = Mock(side_effect=NotFoundException(status=404, reason="Not Found"))
        with self.assertRaises(Exception) as context:
            self.mock_api.billing_group_update("bg_fakeId", self.mock_api.billing_group_update)
        self.assertTrue("Not Found" in context.exception.__str__())

if __name__ == '__main__':
    unittest.main()
