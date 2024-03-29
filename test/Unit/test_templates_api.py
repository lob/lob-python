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
from lob_python.api.templates_api import TemplatesApi  # noqa: E501
from lob_python.model.template_writable import TemplateWritable
from lob_python.model.template_update import TemplateUpdate
from lob_python.model.metadata_model import MetadataModel
from lob_python.model.include_model import IncludeModel
from lob_python.exceptions import UnauthorizedException, NotFoundException, ApiException
from unittest.mock import Mock, MagicMock

class TestTemplatesApi(unittest.TestCase):
    """TemplatesApi unit test stubs"""

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.config_for_unit = lob_python.Configuration(
            username = "Totally Fake Key"
        )
        with lob_python.ApiClient(self.config_for_unit) as self.api_client:
            self.mock_api = TemplatesApi(self.api_client)

        self.template_writable = TemplateWritable(
            description = "Newer Template",
            html = "<html>Updated HTML for {{name}}</html>",
        )

        self.template_update = TemplateUpdate(
            description = "template updated",
            published_version = "vrsn_fakeId",
        )

        self.mock_list_of_templates =  MagicMock(return_value={
            "data": [{ "id": "fake 1" }, { "id": "fake 2" }]
        })

    def test_template_create_error_handle(self):
        """Test case for handling create error"""
        self.mock_api.create_template = Mock(side_effect=UnauthorizedException(status=401, reason="Unauthorized"))

        with self.assertRaises(Exception) as context:
            self.mock_api.create_template(self.template_writable)
        self.assertTrue("Unauthorized" in context.exception.__str__())

    def test_template_create(self):
        """Test case for creating new template"""
        self.mock_api.create_template = MagicMock(return_value={
            "id": "tmpl_fakeId"
        })
        created_template = self.mock_api.create_template(self.template_writable)
        self.assertIsNotNone(created_template)
        self.assertIsNotNone(created_template["id"])

    def test_template_create_with_custom_headers(self):
        """Test case for creating new template with custom headers"""
        self.mock_api.create_template = MagicMock(return_value={
            "id": "tmpl_fakeId"
        })
        created_template = self.mock_api.create_template(self.template_writable, _content_type="application/json")
        self.assertIsNotNone(created_template)
        self.assertIsNotNone(created_template["id"])

    def test_template_retrieve(self):
        """Test case for retrieving template"""
        self.mock_api.template_retrieve = MagicMock(return_value={
            "id": "tmpl_fakeId"
        })
        retrieved_template = self.mock_api.template_retrieve("tmpl_fakeId")
        self.assertEqual(retrieved_template["id"], "tmpl_fakeId")

    def test_template_retrieve_with_custom_headers(self):
        """Test case for retrieving template with custom headers"""
        self.mock_api.template_retrieve = MagicMock(return_value={
            "id": "tmpl_fakeId"
        })
        retrieved_template = self.mock_api.template_retrieve("tmpl_fakeId", _content_type="application/json")
        self.assertEqual(retrieved_template["id"], "tmpl_fakeId")

    def test_template_retrieve_error_handle(self):
        """Test case for handling retrieve error"""
        self.mock_api.template_retrieve = Mock(side_effect=NotFoundException(status=404, reason="Not Found"))

        with self.assertRaises(Exception) as context:
            self.mock_api.template_retrieve("tmpl_fakeId")
        self.assertTrue("Not Found" in context.exception.__str__())

    def test_template_delete(self):
        """Test case for deleting template"""
        self.mock_api.template_delete = MagicMock(return_value={
            "id": "tmpl_fakeId", "deleted": True
        })
        deleted_template = self.mock_api.template_delete("tmpl_fakeId")
        self.assertTrue(deleted_template["deleted"])

    def test_template_delete_with_custom_headers(self):
        """Test case for deleting template"""
        self.mock_api.template_delete = MagicMock(return_value={
            "id": "tmpl_fakeId", "deleted": True
        })
        deleted_template = self.mock_api.template_delete("tmpl_fakeId", _content_type="application/json")
        self.assertTrue(deleted_template["deleted"])

    def test_template_delete_error_handle(self):
        """Test case for handling delete error"""
        self.mock_api.template_delete = Mock(side_effect=NotFoundException(status=404, reason="Not Found"))

        with self.assertRaises(Exception) as context:
            self.mock_api.template_delete("tmpl_fakeId")
        self.assertTrue("Not Found" in context.exception.__str__())

    def test_template_update(self):
        """Test case for updating template"""
        self.mock_api.template_update = MagicMock(return_value={
            "id": "tmpl_fakeId"
        })
        updated_template = self.mock_api.template_update("tmpl_fakeId", self.template_update)
        self.assertIsNotNone(updated_template)
        self.assertEqual(updated_template["id"], "tmpl_fakeId")

    def test_template_update_with_custom_headers(self):
        """Test case for updating template with custom headers"""
        self.mock_api.template_update = MagicMock(return_value={
            "id": "tmpl_fakeId"
        })
        updated_template = self.mock_api.template_update("tmpl_fakeId", self.template_update, _content_type="application/json")
        self.assertIsNotNone(updated_template)
        self.assertEqual(updated_template["id"], "tmpl_fakeId")

    def test_template_update_error_handle(self):
        """Test case for handling update error"""
        self.mock_api.template_update = Mock(side_effect=NotFoundException(status=404, reason="Not Found"))

        with self.assertRaises(Exception) as context:
            self.mock_api.template_update("tmpl_fakeId", self.template_update)
        self.assertTrue("Not Found" in context.exception.__str__())

    def test_templates_list(self):
        """Test case for listing templates"""
        self.mock_api.templates_list = self.mock_list_of_templates
        templates = self.mock_api.templates_list()
        self.assertIsNotNone(templates)
        self.assertEqual(len(templates["data"]), 2)

    def test_templates_list_with_custom_headers(self):
        """Test case for listing templates with custom headers"""
        self.mock_api.templates_list = self.mock_list_of_templates
        templates = self.mock_api.templates_list(_content_type="application/json")
        self.assertIsNotNone(templates)
        self.assertEqual(len(templates["data"]), 2)

    def test_templates_list_error_handle(self):
        """Test case for handling list error"""
        msg = """Cannot prepare a request message for provided
                 arguments. Please check that your arguments match
                 declared content type."""
        self.mock_api.templates_list = Mock(side_effect=ApiException(status=0, reason=msg))

        with self.assertRaises(Exception) as context:
            self.mock_api.templates_list()
        self.assertTrue("Cannot prepare a request message" in context.exception.__str__())

    def test_templates_list_with_limit_param(self):
        """Test case for listing templates with limit parameter"""
        self.mock_api.templates_list = self.mock_list_of_templates
        templates = self.mock_api.templates_list(limit=10)
        self.assertIsNotNone(templates)
        self.assertEqual(len(templates["data"]), 2)

    def test_templates_list_with_before_param(self):
        """Test case for listing templates with before parameter"""
        self.mock_api.templates_list = self.mock_list_of_templates
        templates = self.mock_api.templates_list(before="before")
        self.assertIsNotNone(templates)
        self.assertEqual(len(templates["data"]), 2)

    def test_templates_list_with_after_param(self):
        """Test case for listing templates with after parameter"""
        self.mock_api.templates_list = self.mock_list_of_templates
        templates = self.mock_api.templates_list(after="after")
        self.assertIsNotNone(templates)
        self.assertEqual(len(templates["data"]), 2)

    def test_templates_list_with_include_param(self):
        """Test case for listing templates with include parameter"""
        self.mock_api.templates_list = self.mock_list_of_templates
        templates = self.mock_api.templates_list(include=IncludeModel(["total_count"]))
        self.assertIsNotNone(templates)
        self.assertEqual(len(templates["data"]), 2)

    def test_templates_list_with_dateCreated_param(self):
        """Test case for listing templates with date_created parameter"""
        self.mock_api.templates_list = self.mock_list_of_templates
        templates = self.mock_api.templates_list(date_created={ "gt": "2020-01-01", "lt": "2020-01-31T12" })
        self.assertIsNotNone(templates)
        self.assertEqual(len(templates["data"]), 2)

    def test_templates_list_with_metadata_param(self):
        """Test case for listing self mailer with metadata parameter"""
        self.mock_api.templates_list = self.mock_list_of_templates
        templates = self.mock_api.templates_list(metadata=MetadataModel(fakeMetadata = "fakeMetadata"))
        self.assertIsNotNone(templates)
        self.assertEqual(len(templates["data"]), 2)

if __name__ == '__main__':
    unittest.main()
