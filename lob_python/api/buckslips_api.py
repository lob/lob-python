"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> Looking for our [previous documentation](https://lob.github.io/legacy-docs/)?   # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: lob-openapi@lob.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from lob_python.api_client import ApiClient, Endpoint as _Endpoint
from lob_python.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from lob_python.model.buckslip import Buckslip
from lob_python.model.buckslip_deletion import BuckslipDeletion
from lob_python.model.buckslip_editable import BuckslipEditable
from lob_python.model.buckslip_id import BuckslipId
from lob_python.model.buckslip_updatable import BuckslipUpdatable
from lob_python.model.buckslips_list import BuckslipsList
from lob_python.model.include_model import IncludeModel
from lob_python.model.lob_error import LobError


class BuckslipsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.Create_endpoint = _Endpoint(
            settings={
                'response_type': (Buckslip,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/buckslips',
                'operation_id': 'Create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'buckslip_editable',
                ],
                'required': [
                    'buckslip_editable',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'buckslip_editable':
                        (BuckslipEditable,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'buckslip_editable': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'application/x-www-form-urlencoded',
                    'multipart/form-data'
                ]
            },
            api_client=api_client
        )
        self.Delete_endpoint = _Endpoint(
            settings={
                'response_type': (BuckslipDeletion,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/buckslips/{buckslip_id}',
                'operation_id': 'Delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'buckslip_id',
                ],
                'required': [
                    'buckslip_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'buckslip_id':
                        (BuckslipId,),
                },
                'attribute_map': {
                    'buckslip_id': 'buckslip_id',
                },
                'location_map': {
                    'buckslip_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.Retrieve_endpoint = _Endpoint(
            settings={
                'response_type': (Buckslip,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/buckslips/{buckslip_id}',
                'operation_id': 'Retrieve',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'buckslip_id',
                ],
                'required': [
                    'buckslip_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'buckslip_id':
                        (BuckslipId,),
                },
                'attribute_map': {
                    'buckslip_id': 'buckslip_id',
                },
                'location_map': {
                    'buckslip_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.Update_endpoint = _Endpoint(
            settings={
                'response_type': (Buckslip,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/buckslips/{buckslip_id}',
                'operation_id': 'Update',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'buckslip_id',
                    'buckslip_updatable',
                ],
                'required': [
                    'buckslip_id',
                    'buckslip_updatable',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'buckslip_id':
                        (BuckslipId,),
                    'buckslip_updatable':
                        (BuckslipUpdatable,),
                },
                'attribute_map': {
                    'buckslip_id': 'buckslip_id',
                },
                'location_map': {
                    'buckslip_id': 'path',
                    'buckslip_updatable': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'application/x-www-form-urlencoded',
                    'multipart/form-data'
                ]
            },
            api_client=api_client
        )
        self.List_endpoint = _Endpoint(
            settings={
                'response_type': (BuckslipsList,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/buckslips',
                'operation_id': 'List',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'limit',
                    'before',
                    'after',
                    'include',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'limit':
                        (int,),
                    'before':
                        (str,),
                    'after':
                        (str,),
                    'include':
                        (IncludeModel,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'before': 'before',
                    'after': 'after',
                    'include': 'include',
                },
                'location_map': {
                    'limit': 'query',
                    'before': 'query',
                    'after': 'query',
                    'include': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def Create(
        self,
        buckslip_editable,
        **kwargs
    ):
        """Create  # noqa: E501

        Creates a new buckslip given information  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.Create(buckslip_editable, async_req=True)
        >>> result = thread.get()

        Args:
            buckslip_editable (BuckslipEditable):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Buckslip
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['buckslip_editable'] = \
            buckslip_editable
        return self.Create_endpoint.call_with_http_info(**kwargs)

    def Delete(
        self,
        buckslip_id,
        **kwargs
    ):
        """Delete  # noqa: E501

        Delete an existing buckslip. You need only supply the unique identifier that was returned upon buckslip creation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.Delete(buckslip_id, async_req=True)
        >>> result = thread.get()

        Args:
            buckslip_id (BuckslipId): id of the buckslip

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            BuckslipDeletion
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['buckslip_id'] = \
            buckslip_id
        return self.Delete_endpoint.call_with_http_info(**kwargs)

    def Retrieve(
        self,
        buckslip_id,
        **kwargs
    ):
        """Retrieve  # noqa: E501

        Retrieves the details of an existing buckslip. You need only supply the unique customer identifier that was returned upon buckslip creation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.Retrieve(buckslip_id, async_req=True)
        >>> result = thread.get()

        Args:
            buckslip_id (BuckslipId): id of the buckslip

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Buckslip
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['buckslip_id'] = \
            buckslip_id
        return self.Retrieve_endpoint.call_with_http_info(**kwargs)

    def Update(
        self,
        buckslip_id,
        buckslip_updatable,
        **kwargs
    ):
        """Update  # noqa: E501

        Update the details of an existing buckslip. You need only supply the unique identifier that was returned upon buckslip creation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.Update(buckslip_id, buckslip_updatable, async_req=True)
        >>> result = thread.get()

        Args:
            buckslip_id (BuckslipId): id of the buckslip
            buckslip_updatable (BuckslipUpdatable):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Buckslip
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['buckslip_id'] = \
            buckslip_id
        kwargs['buckslip_updatable'] = \
            buckslip_updatable
        return self.Update_endpoint.call_with_http_info(**kwargs)

    def List(
        self,
        **kwargs
    ):
        """List  # noqa: E501

        Returns a list of your buckslips. The buckslips are returned sorted by creation date, with the most recently created buckslips appearing first.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.List(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            limit (int): How many results to return.. [optional] if omitted the server will use the default value of 10
            before (str): A reference to a list entry used for paginating to the previous set of entries. This field is pre-populated in the `previous_url` field in the return response. . [optional]
            after (str): A reference to a list entry used for paginating to the next set of entries. This field is pre-populated in the `next_url` field in the return response. . [optional]
            include (IncludeModel): Request that the response include the total count by specifying `include[]=total_count`. . [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            BuckslipsList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.List_endpoint.call_with_http_info(**kwargs)

