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
from lob_python.api.card_orders_api import CardOrdersApi  # noqa: E501
from lob_python.model.card_order_editable import CardOrderEditable
from lob_python.exceptions import UnauthorizedException, NotFoundException
from unittest.mock import Mock, MagicMock

class TestCardOrdersApi(unittest.TestCase):
    """CardOrdersApi unit test stubs"""

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.config_for_unit = lob_python.Configuration(
            username = "Totally Fake Key"
        )
        with lob_python.ApiClient(self.config_for_unit) as self.api_client:
            self.mock_api = CardOrdersApi(self.api_client)

        self.card_order_editable = CardOrderEditable(
            quantity = 10000,
        )

    def test_card_order_create_error_handle(self):
        """Test case for handling create error"""
        self.mock_api.card_order_create = Mock(side_effect=UnauthorizedException(status=401, reason="Unauthorized"))

        with self.assertRaises(Exception) as context:
            self.mock_api.card_order_create("card_fakeId", self.card_order_editable)
        self.assertTrue("Unauthorized" in context.exception.__str__())

    def test_card_order_create(self):
        """Test case for creating new card"""
        self.mock_api.card_order_create = MagicMock(return_value={
            "id": "co_fakeId"
        })
        created_card_order = self.mock_api.card_order_create("card_fakeId", self.card_order_editable)
        self.assertIsNotNone(created_card_order)
        self.assertEqual(created_card_order["id"], "co_fakeId")

    def test_card_order_create_with_custom_headers(self):
        """Test case for creating new card with custom headers"""
        self.mock_api.card_order_create = MagicMock(return_value={
            "id": "co_fakeId"
        })
        created_card_order = self.mock_api.card_order_create("card_fakeId", self.card_order_editable, _content_type="application/json")
        self.assertIsNotNone(created_card_order)
        self.assertEqual(created_card_order["id"], "co_fakeId")

    def test_card_order_retrieve(self):
        """Test case for retrieving card order"""
        self.mock_api.card_order_retrieve = MagicMock(return_value={
            "data": [{ "card_id": "card_fakeId" }, { "card_id": "card_differentFakeId" }]
        })
        retrieved_card_order = self.mock_api.card_order_retrieve("card_fakeId")
        card_included = False
        for card in retrieved_card_order["data"]:
            if card["card_id"] == "card_fakeId":
                card_included = True
        self.assertTrue(card_included)

    def test_card_order_retrieve_with_custom_headers(self):
        """Test case for retrieving card order with custom headers"""
        self.mock_api.card_order_retrieve = MagicMock(return_value={
            "data": [{ "card_id": "card_fakeId" }, { "card_id": "card_differentFakeId" }]
        })
        retrieved_card_order = self.mock_api.card_order_retrieve("card_fakeId", _content_type="application/json")
        card_included = False
        for card in retrieved_card_order["data"]:
            if card["card_id"] == "card_fakeId":
                card_included = True
        self.assertTrue(card_included)

    def test_card_order_retrieve_error_handle(self):
        """Test case for handling retrieve error"""
        self.mock_api.card_order_retrieve = Mock(side_effect=NotFoundException(status=404, reason="Not Found"))

        with self.assertRaises(Exception) as context:
            self.mock_api.card_order_retrieve("card_fakeId")
        self.assertTrue("Not Found" in context.exception.__str__())

if __name__ == '__main__':
    unittest.main()
