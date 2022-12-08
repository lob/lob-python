"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> Looking for our [previous documentation](https://lob.github.io/legacy-docs/)?   # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: lob-openapi@lob.com
    Generated by: https://openapi-generator.tech
"""


import string
import unittest
from unittest_data_provider import data_provider
import warnings

import lob_python
import os
from dotenv import load_dotenv
from lob_python.api.addresses_api import AddressesApi  # noqa: E501
from lob_python.model.address_editable import AddressEditable  # noqa: E501
from lob_python.model.address_list import AddressList  # noqa: E501
from lob_python.model.country_extended import CountryExtended  # noqa: E501
import datetime as dt

class TestAddressesApi(unittest.TestCase):
    """AddressesApi unit test stubs"""
    # limit, before, after, include, date_created, metadata
    query_params = lambda: (
        (None, None, None, ["total_count"], None, None),
        (None, None, None, None, {"gt": dt.datetime.combine(
            dt.datetime.now() - dt.timedelta(weeks=4),
            dt.datetime.min.time()
        )}, None),
        (None, None, None, None, None, {"name": "harry"})
    )

    @classmethod
    def setUpClass(self):
        load_dotenv()
        warnings.simplefilter("ignore", ResourceWarning)
        self.adr_ids = []
        self.configuration = lob_python.Configuration(
            username = os.getenv('LOB_API_TEST_KEY')
        )
        with lob_python.ApiClient(self.configuration) as self.api_client:
            self.api = AddressesApi(self.api_client)  # noqa: E501
        self.address_editable = AddressEditable(
            name = "THING T. THING",
            address_line1 = "1313 CEMETERY LN",
            address_city = "WESTFIELD",
            address_state = "NJ",
            address_zip = "07000"
        )

    @classmethod
    def tearDownClass(self):
        for i in self.adr_ids:
            self.api.delete(i)
        del self.address_editable
        del self.api
        del self.configuration
        del self.adr_ids

    def test_create200(self):
        """Test case for create

        create  # noqa: E501
        """
        created_address = self.api.create(self.address_editable)
        self.adr_ids.append(created_address.id)
        self.assertIsNotNone(created_address.id)
        self.assertEqual(created_address.address_line1, "1313 CEMETERY LN")

    def test_create422(self):
        """Test case for create

        create  # noqa: E501
        """
        faulty_address = AddressEditable(
            name = "FESTER",
            address_line2 = "SUITE 666",
            address_city = "WESTFIELD",
            address_state = "NJ",
            address_zip = "07000"
        )
        with self.assertRaises(Exception) as context:
            self.api.create(faulty_address)
        self.assertTrue("address_line1 is required" in context.exception.__str__())

    def test_create422_invalid_zip(self):
        """Test case for create

        create  # noqa: E501
        """
        faulty_address = AddressEditable(
            name = "FESTER",
            address_line1 = "1313 CEMETERY LN",
            address_city = "WESTFIELD",
            address_state = "NJ",
            address_zip = "999999"
        )
        with self.assertRaises(Exception) as context:
            self.api.create(faulty_address)
        self.assertTrue("address_zip is not a valid ZIP code" in context.exception.__str__())

    def test_create422_addr_too_long(self):
        """Test case for create

        create  # noqa: E501
        """
        faulty_address = AddressEditable(
            name = "FESTER",
            address_line1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit porttitor",
            address_line2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit porttitor",
            address_city = "WESTFIELD",
            address_state = "NJ",
            address_zip = "07000"
        )
        with self.assertRaises(Exception) as context:
            self.api.create(faulty_address)
        self.assertTrue("address_line1 length must be less than or equal to 64 characters long" in context.exception.__str__())

    def test_get200(self):
        """Test case for get

        get  # noqa: E501
        """
        created_address = self.api.create(self.address_editable)
        getd_address = self.api.get(created_address.id)
        self.adr_ids.append(created_address.id)
        self.assertIsNotNone(getd_address.id)
        self.assertEqual(getd_address.id, created_address.id)

    def test_get404(self):
        """Test case for get

        get  # noqa: E501
        """
        with self.assertRaises(Exception) as context:
            self.api.get("adr_fake")
        self.assertTrue("address not found" in context.exception.__str__())

    def test_list200(self):
        """Test case for list

        list  # noqa: E501
        """
        editable_address2 = AddressEditable(
            name = "FESTER",
            address_line1 = "001 CEMETERY LN",
            address_line2 = "SUITE 666",
            address_city = "WESTFIELD",
            address_state = "NJ",
            address_zip = "07000"
        )

        address_1 = self.api.create(self.address_editable)
        address_2 = self.api.create(editable_address2)
        self.adr_ids.append(address_1.id)
        self.adr_ids.append(address_2.id)
        listed_addresses = self.api.list(limit=2)
        self.assertEqual(len(listed_addresses.data), 2)
        self.assertIsNotNone(listed_addresses.data[0]['id'])
        next = listed_addresses.getNextPageToken()

        # perform test with after query param
        if next:
            listed_addresses_after = self.api.list(limit=2, after=next)
            self.assertLessEqual(len(listed_addresses_after.data), 2)
            self.assertIsNotNone(listed_addresses_after.data[0]['id'])
            prev = listed_addresses_after.getPreviousPageToken()
            if prev:
                listed_addresses_before = self.api.list(limit=2, before=prev)
                self.assertLessEqual(len(listed_addresses_before.data), 2)
                self.assertIsNotNone(listed_addresses_before.data[0]['id'])

    @data_provider(query_params)
    def test_list_other_params(self, limit, before, after, include, date_created, metadata):
        args = {}
        if limit:
            args["limit"] = limit

        if before:
            args["before"] = before

        if after:
            args["after"] = after

        if include:
            args["include"] = include

        if date_created:
            args["date_created"] = date_created

        if metadata:
            args["metadata"] = metadata

        listed_addresses = self.api.list(**args)

        self.assertGreaterEqual(len(listed_addresses["data"]), 0)
        if include:
            self.assertIsNotNone(listed_addresses["total_count"])

    def test_list422(self):
        """Test case for list

        list  # noqa: E501
        """
        editable_address2 = AddressEditable(
            name = "FESTER",
            address_line1 = "001 CEMETERY LN",
            address_line2 = "SUITE 666",
            address_city = "WESTFIELD",
            address_state = "NJ",
            address_zip = "07000"
        )

        address_1 = self.api.create(self.address_editable)
        address_2 = self.api.create(editable_address2)
        self.adr_ids.append(address_1.id)
        self.adr_ids.append(address_2.id)
        with self.assertRaises(Exception) as context:
            self.api.list(limit=101)
        self.assertTrue("Invalid value for `limit`" in context.exception.__str__())

    def test_delete200(self):
        """Test case for delete

        delete  # noqa: E501
        """
        created_address = self.api.create(self.address_editable)
        deleted_address = self.api.delete(created_address.id)
        self.assertEqual(deleted_address.deleted, True)

    def test_delete404(self):
        """Test case for delete

        delete  # noqa: E501
        """
        with self.assertRaises(Exception) as context:
            self.api.delete("adr_fake")
        self.assertTrue("address not found" in context.exception.__str__())


if __name__ == '__main__':
    unittest.main()