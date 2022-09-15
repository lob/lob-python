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
from unittest_data_provider import data_provider
import warnings
import datetime as dt

import lob_python
import os
from dotenv import load_dotenv
from dateutil.parser import *
from lob_python.api.templates_api import TemplatesApi  # noqa: E501
from lob_python.api.template_versions_api import TemplateVersionsApi  # noqa: E501
from lob_python.model.template_writable import TemplateWritable  # noqa: E501
from lob_python.model.template_version_writable import TemplateVersionWritable  # noqa: E501
from lob_python.model.template_version_updatable import TemplateVersionUpdatable  # noqa: E501

class TestTemplateVersionsApi(unittest.TestCase):
    """TemplatesApi unit test stubs"""
    # limit, before, after, include, date_created,
    query_params = lambda: (
        (None, None, None, ["total_count"], None),
        (None, None, None, None, {"gt": dt.datetime.combine(
            dt.datetime.now() - dt.timedelta(weeks=4),
            dt.datetime.min.time()
        )}),
    )

    @classmethod
    def setUpClass(self):
        load_dotenv()
        warnings.simplefilter("ignore", ResourceWarning)
        self.tmpl_vers_ids = []
        self.configuration = lob_python.Configuration(
            username = os.getenv('LOB_API_TEST_KEY')
        )
        with lob_python.ApiClient(self.configuration) as self.api_client:
            self.templates_api = TemplatesApi(self.api_client)  # noqa: E501

        with lob_python.ApiClient(self.configuration) as self.api_client:
            self.api = TemplateVersionsApi(self.api_client)  # noqa: E501

        self.template_writable  = TemplateWritable(
            description = "Test Template Version 1",
            html = "<html>Updated HTML for template 1</html>"
        )

        self.id = self.templates_api.create(self.template_writable).id
        self.deleted_tmpl_id = self.templates_api.create(self.template_writable).id
        self.templates_api.delete(self.deleted_tmpl_id)

        self.template_version_writable  = TemplateVersionWritable(
            description = "Test Template Version 1",
            html = "<html>Updated HTML for template version 1</html>"
        )

        self.writable_template_version2 = TemplateVersionWritable(
            description = "Test Template Version 2",
            html = "<html>Updated HTML for template version 2</html>"
        )

    @classmethod
    def tearDownClass(self):
        for i in self.tmpl_vers_ids:
            self.api.delete(self.id, i)
        del self.template_version_writable
        del self.writable_template_version2
        del self.api
        del self.configuration
        del self.tmpl_vers_ids

        self.templates_api.delete(self.id)
        del self.deleted_tmpl_id
        del self.templates_api
        del self.template_writable

    def test_create200(self):
        """Test case for create

        create  # noqa: E501
        """
        created_template_version = self.api.create(self.id, self.template_version_writable)
        self.tmpl_vers_ids.append(created_template_version.id)
        self.assertIsNotNone(created_template_version.id)

    def test_create404(self):
        """Test case for create

        create  # noqa: E501
        """
        with self.assertRaises(Exception) as context:
            created_template_version = self.api.create(self.deleted_tmpl_id, self.template_version_writable)
            self.tmpl_vers_ids.append(created_template_version.id)
        self.assertTrue("template not found" in context.exception.__str__())

    def test_get200(self):
        """Test case for get

        get  # noqa: E501
        """
        created_template_version = self.api.create(self.id, self.template_version_writable)
        retrieved_template_version = self.api.get(self.id, created_template_version.id)
        self.tmpl_vers_ids.append(created_template_version.id)
        self.assertIsNotNone(retrieved_template_version.id)
        self.assertEqual(retrieved_template_version.id, created_template_version.id)

    def test_get404(self):
        """Test case for get

        get  # noqa: E501
        """
        with self.assertRaises(Exception) as context:
            self.api.get(self.id, "tmpl_fake")
        self.assertTrue("template version not found" in context.exception.__str__())

    def test_update200(self):
        """Test case for get

        get  # noqa: E501
        """
        updatable_template = TemplateVersionUpdatable(
            description = "Updated template version"
        )
        created_template_version = self.api.create(self.id, self.template_version_writable)
        updated = self.api.update(self.id, created_template_version.id, updatable_template)
        self.tmpl_vers_ids.append(updated.id)
        self.assertIsNotNone(updated.id)
        self.assertEqual(updated.description, "Updated template version")

    def test_update404(self):
        """Test case for update

        update  # noqa: E501
        """
        updatable_template = TemplateVersionUpdatable(
            description = "Updated template version"
        )
        with self.assertRaises(Exception) as context:
            self.api.update(self.id, "tmpl_fakeId", updatable_template)
        self.assertTrue("template version not found" in context.exception.__str__())

    def test_list200(self):
        """Test case for list

        list  # noqa: E501
        """

        writable_template_version3 = TemplateVersionWritable(
            description = "Test Template Version 3",
            html = "<html>Updated HTML for template version 3</html>"
        )

        tv_1 = self.api.create(self.id, self.template_version_writable)
        tv_2 = self.api.create(self.id, self.writable_template_version2)
        tv_3 = self.api.create(self.id, writable_template_version3)
        self.tmpl_vers_ids.append(tv_1.id)
        self.tmpl_vers_ids.append(tv_2.id)
        self.tmpl_vers_ids.append(tv_3.id)
        listed_template_versions = self.api.list(self.id, limit=2)
        self.assertLessEqual(len(listed_template_versions.data), 2)
        self.assertIsNotNone(listed_template_versions.data[0]['id'])
        next = listed_template_versions.getNextPageToken()

        # perform test with after query param
        if next:
            listed_template_versions_after = self.api.list(self.id, limit=2, after=next)
            self.assertEqual(len(listed_template_versions_after.data), 2)
            self.assertIsNotNone(listed_template_versions_after.data[0]['id'])
            prev = listed_template_versions_after.getPreviousPageToken()
            if prev:
                listed_template_versions_before = self.api.list(self.id, limit=2, before=prev)
                self.assertLessEqual(len(listed_template_versions_before.data), 2)
                self.assertIsNotNone(listed_template_versions_before.data[0]['id'])

    @data_provider(query_params)
    def test_list_other_query_params(self, limit, before, after, include, date_created):
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
        response = self.api.list(self.id, **args)

        self.assertGreaterEqual(len(response["data"]), 0)
        if include:
            self.assertIsNotNone(response["total_count"])

    def test_list422(self):
        """Test case for list

        list  # noqa: E501
        """

        tv_1 = self.api.create(self.id, self.template_version_writable)
        tv_2 = self.api.create(self.id, self.writable_template_version2)
        self.tmpl_vers_ids.append(tv_1.id)
        self.tmpl_vers_ids.append(tv_2.id)
        with self.assertRaises(Exception) as context:
            self.api.list(self.id, limit=101)
        self.assertTrue("Invalid value for `limit`" in context.exception.__str__())

    def test_delete200(self):
        """Test case for delete

        delete  # noqa: E501
        """
        created_template_version = self.api.create(self.id, self.template_version_writable)
        deleted_template = self.api.delete(self.id, created_template_version.id)
        self.assertEqual(deleted_template.deleted, True)

    def test_delete404(self):
        """Test case for delete

        delete  # noqa: E501
        """
        with self.assertRaises(Exception) as context:
            self.api.delete(self.id, "tmpl_fake")
        self.assertTrue("template version cannot be deleted" in context.exception.__str__())


if __name__ == '__main__':
    unittest.main()
