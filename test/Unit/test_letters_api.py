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
from lob_python.api.letters_api import LettersApi  # noqa: E501
from lob_python.model.letter_editable import LetterEditable
from lob_python.model.address_editable import AddressEditable
from lob_python.model.ltr_use_type import LtrUseType
from lob_python.model.mail_type import MailType
from lob_python.model.sort_by3 import SortBy3
from lob_python.model.metadata_model import MetadataModel
from lob_python.model.include_model import IncludeModel
from lob_python.exceptions import UnauthorizedException, NotFoundException, ApiException
from unittest.mock import Mock, MagicMock

class TestLettersApi(unittest.TestCase):
    """LettersApi unit test stubs"""

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.config_for_unit = lob_python.Configuration(
            username = "Totally Fake Key"
        )
        with lob_python.ApiClient(self.config_for_unit) as self.api_client:
            self.mock_api = LettersApi(self.api_client)

        self.mock_list_of_letters =  MagicMock(return_value={
            "data": [{ "id": "fake 1" }, { "id": "fake 2" }]
        })

        self.letter_editable = LetterEditable(
            to = "adr_fakeId1",
            _from = "adr_fakeId2",
            file = "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/us_letter_1pg.pdf",
            color = True,
            use_type = LtrUseType("marketing")
        )

    def test_letter_retrieve_error_handle(self):
        """Test case for handling retrieve error"""
        self.mock_api.letter_retrieve = Mock(side_effect=UnauthorizedException(status=401, reason="Unauthorized"))

        with self.assertRaises(Exception) as context:
            self.mock_api.letter_retrieve("ltr_fakeId")
        self.assertTrue("Unauthorized" in context.exception.__str__())

    def test_letter_retrieve(self):
        """Test case for retrieving letter"""
        self.mock_api.letter_retrieve = MagicMock(return_value={
            "id": "ltr_fakeId"
        })
        retrieved_letter = self.mock_api.letter_retrieve("ltr_fakeId")
        self.assertIsNotNone(retrieved_letter)
        self.assertEqual(retrieved_letter["id"], "ltr_fakeId")

    def test_letter_retrieve_with_custom_headers(self):
        """Test case for retrieving new letter with custom headers"""
        self.mock_api.letter_retrieve = MagicMock(return_value={
            "id": "ltr_fakeId"
        })
        retrieved_letter = self.mock_api.letter_retrieve("ltr_fakeId", _content_type="application/json")
        self.assertIsNotNone(retrieved_letter)
        self.assertEqual(retrieved_letter["id"], "ltr_fakeId")

    def test_letters_list(self):
        """Test case for listing letters"""
        self.mock_api.letters_list = self.mock_list_of_letters
        letters = self.mock_api.letters_list()
        self.assertIsNotNone(letters)
        self.assertEqual(len(letters["data"]), 2)

    def test_letters_list_with_custom_headers(self):
        """Test case for listing letters with custom headers"""
        self.mock_api.letters_list = self.mock_list_of_letters
        letters = self.mock_api.letters_list(_content_type="application/json")
        self.assertIsNotNone(letters)
        self.assertEqual(len(letters["data"]), 2)

    def test_letters_list_error_handle(self):
        """Test case for handling list error"""
        msg = """Cannot prepare a request message for provided
                 arguments. Please check that your arguments match
                 declared content type."""
        self.mock_api.letters_list = Mock(side_effect=ApiException(status=0, reason=msg))

        with self.assertRaises(Exception) as context:
            self.mock_api.letters_list()
        self.assertTrue("Cannot prepare a request message" in context.exception.__str__())

    def test_letters_list_with_limit_param(self):
        """Test case for listing letter with limit parameter"""
        self.mock_api.letters_list = self.mock_list_of_letters
        letters = self.mock_api.letters_list(limit=10)
        self.assertIsNotNone(letters)
        self.assertEqual(len(letters["data"]), 2)

    def test_letters_list_with_before_param(self):
        """Test case for listing letter with before parameter"""
        self.mock_api.letters_list = self.mock_list_of_letters
        letters = self.mock_api.letters_list(before="before")
        self.assertIsNotNone(letters)
        self.assertEqual(len(letters["data"]), 2)

    def test_letters_list_with_after_param(self):
        """Test case for listing letter with after parameter"""
        self.mock_api.letters_list = self.mock_list_of_letters
        letters = self.mock_api.letters_list(after="after")
        self.assertIsNotNone(letters)
        self.assertEqual(len(letters["data"]), 2)

    def test_letters_list_with_include_param(self):
        """Test case for listing letter with include parameter"""
        self.mock_api.letters_list = self.mock_list_of_letters
        letters = self.mock_api.letters_list(include=IncludeModel(["total_count"]))
        self.assertIsNotNone(letters)
        self.assertEqual(len(letters["data"]), 2)

    def test_letters_list_with_date_created_param(self):
        """Test case for listing letter with date_created parameter"""
        self.mock_api.letters_list = self.mock_list_of_letters
        letters = self.mock_api.letters_list(date_created={ "gt": "2020-01-01", "lt": "2020-01-31T12" })
        self.assertIsNotNone(letters)
        self.assertEqual(len(letters["data"]), 2)

    def test_letters_list_with_metadata_param(self):
        """Test case for listing letter with metadata parameter"""
        self.mock_api.letters_list = self.mock_list_of_letters
        letters = self.mock_api.letters_list(metadata=MetadataModel(fakeMetadata = "fakeMetadata"))
        self.assertIsNotNone(letters)
        self.assertEqual(len(letters["data"]), 2)

    def test_letters_list_with_color_param(self):
        """Test case for listing letter with color parameter"""
        self.mock_api.letters_list = self.mock_list_of_letters
        letters = self.mock_api.letters_list(color=True)
        self.assertIsNotNone(letters)
        self.assertEqual(len(letters["data"]), 2)

    def test_letters_list_with_scheduled_param(self):
        """Test case for listing letter with scheduled parameter"""
        self.mock_api.letters_list = self.mock_list_of_letters
        letters = self.mock_api.letters_list(scheduled=True)
        self.assertIsNotNone(letters)
        self.assertEqual(len(letters["data"]), 2)

    def test_letters_list_with_send_date_param(self):
        """Test case for listing letter with send_date parameter"""
        self.mock_api.letters_list = self.mock_list_of_letters
        letters = self.mock_api.letters_list(send_date={ "gt": "2012-01-01", "lt": "2012-01-31T12:34:56Z" })
        self.assertIsNotNone(letters)
        self.assertEqual(len(letters["data"]), 2)

    def test_letters_list_with_mail_type_param(self):
        """Test case for listing letter with mail_type parameter"""
        self.mock_api.letters_list = self.mock_list_of_letters
        letters = self.mock_api.letters_list(mail_type=MailType('usps_first_class'))
        self.assertIsNotNone(letters)
        self.assertEqual(len(letters["data"]), 2)

    def test_letters_list_with_sort_by_param(self):
        """Test case for listing letter with sort_by parameter"""
        self.mock_api.letters_list = self.mock_list_of_letters
        letters = self.mock_api.letters_list(sort_by=SortBy3(date_created = 'asc'))

        self.assertIsNotNone(letters)
        self.assertEqual(len(letters["data"]), 2)

    def test_letter_cancel(self):
        """Test case for canceling letter"""
        self.mock_api.letter_cancel = MagicMock(return_value={
            "id": "ltr_fakeId", "deleted": True
        })
        canceled_letter = self.mock_api.letter_cancel("ltr_fakeId")
        self.assertTrue(canceled_letter["deleted"])

    def test_letter_cancel_with_custom_headers(self):
        """Test case for canceling letter"""
        self.mock_api.letter_cancel = MagicMock(return_value={
            "id": "ltr_fakeId", "deleted": True
        })
        canceled_letter = self.mock_api.letter_cancel("ltr_fakeId", _content_type="application/json")
        self.assertTrue(canceled_letter["deleted"])

    def test_letter_cancel_error_handle(self):
        """Test case for handling cancel error"""
        self.mock_api.letter_cancel = Mock(side_effect=NotFoundException(status=404, reason="Not Found"))

        with self.assertRaises(Exception) as context:
            self.mock_api.letter_cancel("ltr_fakeId")
        self.assertTrue("Not Found" in context.exception.__str__())

    def test_letter_create_error_handle(self):
        """Test case for handling create error"""
        self.mock_api.letter_create = Mock(side_effect=UnauthorizedException(status=401, reason="Unauthorized"))

        with self.assertRaises(Exception) as context:
            self.mock_api.letter_create(self.letter_editable)
        self.assertTrue("Unauthorized" in context.exception.__str__())

    def test_letter_create(self):
        """Test case for creating new letter"""
        self.mock_api.letter_create = MagicMock(return_value={
            "id": "ltr_fakeId"
        })
        created_letter = self.mock_api.letter_create(self.letter_editable)
        self.assertIsNotNone(created_letter)
        self.assertIsNotNone(created_letter["id"])

    def test_letter_create_with_custom_headers(self):
        """Test case for creating new letter with custom headers"""
        self.mock_api.letter_create = MagicMock(return_value={
            "id": "ltr_fakeId"
        })
        created_letter = self.mock_api.letter_create(self.letter_editable, _content_type="application/json")
        self.assertIsNotNone(created_letter)
        self.assertIsNotNone(created_letter["id"])

if __name__ == '__main__':
    unittest.main()
