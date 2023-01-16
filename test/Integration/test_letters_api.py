"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> Looking for our [previous documentation](https://lob.github.io/legacy-docs/)?   # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: lob-openapi@lob.com
    Generated by: https://openapi-generator.tech
"""


from email.headerregistry import Address
import string
import unittest
from lob_python.model.ltr_use_type import LtrUseType
from unittest_data_provider import data_provider
import warnings
import datetime as dt

import lob_python
import os
from dotenv import load_dotenv
from dateutil.parser import *
from lob_python.api.letters_api import LettersApi  # noqa: E501
from lob_python.model.mail_type import MailType  # noqa: E501
from lob_python.model.sort_by3 import SortBy3
from lob_python.model.country_extended import CountryExtended
from lob_python.model.merge_variables import MergeVariables  # noqa: E501
from lob_python.model.metadata_model import MetadataModel  # noqa: E501
from lob_python.model.letter_editable import LetterEditable  # noqa: E501
from lob_python.model.address_editable import AddressEditable  # noqa: E501
from lob_python.model.letter_editable_custom_envelope import LetterEditableCustomEnvelope  # noqa: E501

last_month = dt.datetime.combine(
    dt.datetime.now() - dt.timedelta(weeks=4),
    dt.datetime.min.time()
)

class TestLettersApi(unittest.TestCase):
    """LettersApi unit test stubs"""
    # limit, before, after, include, date_created, metadata, color, scheduled, send_date, mail_type, sort_by
    query_params = lambda: (
        (None, None, None, ["total_count"], None, None, None, None, None, None, None), # include
        (None, None, None, None, {"gt": last_month}, None, None, None, None, None, None), # date_created
        (None, None, None, None, None, MetadataModel(key = "key_example"), None, None, None, None, None), # metadata
        (None, None, None, None, None, None, True, None, None, None, None), # color
        (None, None, None, None, None, None, None, True, None, None, None), # scheduled
        (None, None, None, None, None, None, None, None, {"gt": last_month.strftime("%Y-%m-%dT%H:%M:%S%z")}, None, None), # send_date
        (None, None, None, None, None, None, None, None, None, MailType("usps_first_class"), None), # mail_type
        (None, None, None, None, None, None, None, None, None, None, SortBy3(date_created="asc")), # sort_by
    )

    @classmethod
    def setUpClass(self):
        load_dotenv()

        now = dt.datetime.now()

        warnings.simplefilter("ignore", ResourceWarning)
        self.ltr_ids = []
        self.configuration = lob_python.Configuration(
            username = os.getenv('LOB_API_TEST_KEY')
        )
        with lob_python.ApiClient(self.configuration) as self.api_client:
            self.api = LettersApi(self.api_client)  # noqa: E501

        self.to_address = AddressEditable(
            name = "THING T. THING",
            address_line1 = "1313 CEMETERY LN",
            address_city = "WESTFIELD",
            address_state = "NJ",
            address_zip = "07000"
        )

        self.to2 = AddressEditable(
            name = "FESTER",
            address_line1 = "001 CEMETERY LN",
            address_line2 = "SUITE 666",
            address_city = "WESTFIELD",
            address_state = "NJ",
            address_zip = "07000"
        )

        self.intl_addr = AddressEditable(
            name = "INTL ADDRESS",
            address_line1 = "35 TOWER HILL",
            address_city = "LONDON",
            address_country = CountryExtended("GB")
        )

        self.regular_letter = LetterEditable(
            to = self.to_address,
            _from = self.to2,
            file = "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/us_letter_1pg.pdf",
            color = True,
            use_type = LtrUseType("marketing")
        )

        # some fields, like billing_group and address_placement,
        # are trickier to fill in due to permissions
        self.full_letter = LetterEditable(
            to = self.to_address,
            _from = self.to2,
            file = "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/us_letter_1pg.pdf",
            color = True,
            description = "Dummy letter with all fields filled out",
            metadata=MetadataModel(
                key="key_example",
            ),
            mail_type=MailType("usps_first_class"),
            merge_variables=MergeVariables(),
            send_date=now + dt.timedelta(days=30),
            double_sided = True,
            return_envelope = True,
            perforated_page = 1,
            custom_envelope = None,
            use_type = LtrUseType("marketing")
        )

        self.certified_letter = LetterEditable(
            to = self.to_address,
            _from = self.to2,
            file = "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/us_letter_1pg.pdf",
            color = True,
            extra_service = "certified",
            use_type = LtrUseType("marketing")
        )

        self.registered_letter = LetterEditable(
            to = self.to_address,
            _from = self.to2,
            file = "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/us_letter_1pg.pdf",
            color = True,
            extra_service = "registered",
            use_type = LtrUseType("marketing")
        )

    @classmethod
    def tearDownClass(self):
        for i in self.ltr_ids:
            self.api.cancel(i)
        del self.to_address
        del self.to2
        del self.intl_addr
        del self.regular_letter
        del self.full_letter
        del self.certified_letter
        del self.registered_letter
        del self.ltr_ids
        del self.api
        del self.configuration

    def tearDown(self):
        for i in self.ltr_ids:
            self.api.cancel(i)
        pass

    def test_401(self):
        """Test case for create with status code 401"""
        configuration = lob_python.Configuration(
            username = "Totally fake key"
        )
        with lob_python.ApiClient(configuration) as api_client:
            invalid_api = LettersApi(api_client)  # noqa: E501

        with self.assertRaises(Exception) as context:
            invalid_api.create(self.regular_letter)
        self.assertTrue("Your API key is not valid" in context.exception.__str__())

    def test_create200(self):
        """Test case for create

        create  # noqa: E501
        """
        created_letter = self.api.create(self.regular_letter)
        self.ltr_ids.append(created_letter.id)
        self.assertIsNotNone(created_letter.id)

    def test_create_full200(self):
        """Test case for create

        create  # noqa: E501
        """
        created_letter = self.api.create(self.full_letter)
        self.ltr_ids.append(created_letter.id)
        self.assertIsNotNone(created_letter.id)

    def test_create_certified200(self):
        """Test case for create

        create  # noqa: E501
        """
        created_letter = self.api.create(self.certified_letter)
        self.ltr_ids.append(created_letter.id)
        self.assertIsNotNone(created_letter.id)

    def test_create_registered200(self):
        """Test case for create

        create  # noqa: E501
        """
        created_letter = self.api.create(self.registered_letter)
        self.ltr_ids.append(created_letter.id)
        self.assertIsNotNone(created_letter.id)

    def test_create422_perforation_greater_than_num_pages(self):
        """Test case for create

        create  # noqa: E501
        """
        invalid_letter = LetterEditable(
            to = self.to_address,
            _from = self.to2,
            file = "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/us_letter_1pg.pdf", # only 1 page
            perforated_page = 2,
            return_envelope = True,
            color = True,
            use_type = LtrUseType("marketing")
        )
        with self.assertRaises(Exception) as context:
            self.api.create(invalid_letter)
        self.assertTrue("perforation number must be less than or equal to the number of pages" in context.exception.__str__())

    def test_create422_perforation_and_return_envelope_not_together(self):
        """Test case for create

        create  # noqa: E501
        """
        invalid_letter = LetterEditable(
            to = self.to_address,
            _from = self.to2,
            file = "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/us_letter_1pg.pdf",
            perforated_page = 1,
            color = True,
            use_type = LtrUseType("marketing")
        )
        with self.assertRaises(Exception) as context:
            self.api.create(invalid_letter)
        self.assertTrue("return_envelope and perforation must be used together" in context.exception.__str__())

    def test_create422_intl_from(self):
        """Test case for create

        create  # noqa: E501
        """
        invalid_letter = LetterEditable(
            to = self.to_address,
            _from = self.intl_addr,
            file = "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/us_letter_1pg.pdf",
            color = True,
            use_type = LtrUseType("marketing")
        )
        with self.assertRaises(Exception) as context:
            self.api.create(invalid_letter)
        self.assertTrue("The 'from' address must be a US address" in context.exception.__str__())

    def test_create_certified422_custom_envelope_with_certified(self):
        """Test case for create

        create  # noqa: E501
        """
        invalid_certified_letter = LetterEditable(
            to = self.to_address,
            _from = self.to2,
            file = "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/us_letter_1pg.pdf",
            color = True,
            extra_service = "certified",
            custom_envelope = "env_fakeId",
            use_type = LtrUseType("marketing")
        )
        with self.assertRaises(Exception) as context:
            self.api.create(invalid_certified_letter)
        self.assertTrue("Certified mail cannot be sent with custom envelopes" in context.exception.__str__())

    def test_create_certified422_only_US(self):
        """Test case for create

        create  # noqa: E501
        """
        invalid_certified_letter = LetterEditable(
            to = self.intl_addr,
            _from = self.to2,
            file = "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/us_letter_1pg.pdf",
            color = True,
            extra_service = "certified",
            use_type = LtrUseType("marketing")
        )
        with self.assertRaises(Exception) as context:
            self.api.create(invalid_certified_letter)
        self.assertTrue("Certified mail can only sent within the United States" in context.exception.__str__())

    def test_get200(self):
        """Test case for get

        get  # noqa: E501
        """
        created_letter = self.api.create(self.regular_letter)
        retrieved_letter = self.api.get(created_letter.id)
        self.ltr_ids.append(created_letter.id)
        self.assertIsNotNone(retrieved_letter.id)
        self.assertEqual(retrieved_letter.id, created_letter.id)

    def test_get404(self):
        """Test case for get

        get  # noqa: E501
        """
        with self.assertRaises(Exception) as context:
            self.api.get("ltr_fake")
        self.assertTrue("letter not found" in context.exception.__str__())

    def test_list200(self):
        """Test case for list

        list  # noqa: E501
        """
        letter_1 = self.api.create(self.regular_letter)
        letter_2 = self.api.create(self.certified_letter)
        letter_3 = self.api.create(self.full_letter)
        self.ltr_ids.append(letter_1.id)
        self.ltr_ids.append(letter_2.id)
        self.ltr_ids.append(letter_3.id)
        listed_letters = self.api.list(limit=2)
        self.assertLessEqual(len(listed_letters.data), 2)
        self.assertIsNotNone(listed_letters.data[0]['id'])
        next = listed_letters.getNextPageToken()

        # perform test with after query param
        if next:
            listed_letters_after = self.api.list(limit=2, after=next)
            self.assertEqual(len(listed_letters_after.data), 2)
            self.assertIsNotNone(listed_letters_after.data[0]['id'])
            prev = listed_letters_after.getPreviousPageToken()
            if prev:
                listed_letters_before = self.api.list(limit=2, before=prev)
                self.assertLessEqual(len(listed_letters_before.data), 2)
                self.assertIsNotNone(listed_letters_before.data[0]['id'])

    @data_provider(query_params)
    def test_list_other_query_params(self, limit, before, after, include, date_created, metadata, color, scheduled, send_date, mail_type, sort_by):
        """Test case for list with other params"""
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

        if color:
            args["color"] = color

        if scheduled:
            args["scheduled"] = scheduled

        if send_date:
            args["send_date"] = send_date

        if mail_type:
            args["mail_type"] = mail_type

        if sort_by:
            args["sort_by"] = sort_by
        response = self.api.list(**args)

        self.assertGreaterEqual(len(response["data"]), 0)
        if include:
            self.assertIsNotNone(response["total_count"])

    def test_list422(self):
        """Test case for list

        list  # noqa: E501
        """

        letter_1 = self.api.create(self.regular_letter)
        letter_2 = self.api.create(self.certified_letter)
        self.ltr_ids.append(letter_1.id)
        self.ltr_ids.append(letter_2.id)
        with self.assertRaises(Exception) as context:
            self.api.list(limit=101)
        self.assertTrue("Invalid value for `limit`" in context.exception.__str__())

    def test_delete200(self):
        """Test case for delete

        delete  # noqa: E501
        """
        created_letter = self.api.create(self.regular_letter)
        deleted_letter = self.api.cancel(created_letter.id)
        self.assertEqual(deleted_letter.deleted, True)

if __name__ == '__main__':
    unittest.main()
