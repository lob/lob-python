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
from lob_python.model.creative_patch import CreativePatch
from lob_python.model.creative_response import CreativeResponse
from lob_python.model.creative_writable import CreativeWritable
from lob_python.model.crv_id import CrvId
from lob_python.model.lob_error import LobError


class CreativesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_endpoint = _Endpoint(
            settings={
                'response_type': (CreativeResponse,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/creatives',
                'operation_id': 'create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'creative_writable',
                    'x_lang_output',
                ],
                'required': [
                    'creative_writable',
                ],
                'nullable': [
                ],
                'enum': [
                    'x_lang_output',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('x_lang_output',): {

                        "NATIVE": "native",
                        "MATCH": "match"
                    },
                },
                'openapi_types': {
                    'creative_writable':
                        (CreativeWritable,),
                    'x_lang_output':
                        (str,),
                },
                'attribute_map': {
                    'x_lang_output': 'x-lang-output',
                },
                'location_map': {
                    'creative_writable': 'body',
                    'x_lang_output': 'header',
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
        self.get_endpoint = _Endpoint(
            settings={
                'response_type': (CreativeResponse,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/creatives/{crv_id}',
                'operation_id': 'get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'crv_id',
                ],
                'required': [
                    'crv_id',
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
                    'crv_id':
                        (CrvId,),
                },
                'attribute_map': {
                    'crv_id': 'crv_id',
                },
                'location_map': {
                    'crv_id': 'path',
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
        self.update_endpoint = _Endpoint(
            settings={
                'response_type': (CreativeResponse,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/creatives/{crv_id}',
                'operation_id': 'update',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'crv_id',
                    'creative_patch',
                ],
                'required': [
                    'crv_id',
                    'creative_patch',
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
                    'crv_id':
                        (CrvId,),
                    'creative_patch':
                        (CreativePatch,),
                },
                'attribute_map': {
                    'crv_id': 'crv_id',
                },
                'location_map': {
                    'crv_id': 'path',
                    'creative_patch': 'body',
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

    def create(
        self,
        creative_writable,
        **kwargs
    ):
        """create  # noqa: E501

        Creates a new creative with the provided properties  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(creative_writable, async_req=True)
        >>> result = thread.get()

        Args:
            creative_writable (CreativeWritable):

        Keyword Args:
            x_lang_output (str): * `native` - Translate response to the native language of the country in the request * `match` - match the response to the language in the request  Default response is in English. . [optional]
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
            CreativeResponse
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
        kwargs['creative_writable'] = \
            creative_writable
        return self.create_endpoint.call_with_http_info(**kwargs)

    def get(
        self,
        crv_id,
        **kwargs
    ):
        """get  # noqa: E501

        Retrieves the details of an existing creative. You need only supply the unique creative identifier that was returned upon creative creation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get(crv_id, async_req=True)
        >>> result = thread.get()

        Args:
            crv_id (CrvId): id of the creative

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
            CreativeResponse
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
        kwargs['crv_id'] = \
            crv_id
        return self.get_endpoint.call_with_http_info(**kwargs)

    def update(
        self,
        crv_id,
        creative_patch,
        **kwargs
    ):
        """update  # noqa: E501

        Update the details of an existing creative. You need only supply the unique identifier that was returned upon creative creation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update(crv_id, creative_patch, async_req=True)
        >>> result = thread.get()

        Args:
            crv_id (CrvId): id of the creative
            creative_patch (CreativePatch):

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
            CreativeResponse
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
        kwargs['crv_id'] = \
            crv_id
        kwargs['creative_patch'] = \
            creative_patch
        return self.update_endpoint.call_with_http_info(**kwargs)

