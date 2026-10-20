"""Exercise optional query parameters through the public API client."""

import unittest
from unittest.mock import Mock

import urllib3

from lob_python import ApiClient, Configuration


class TestOptionalQueryParams(unittest.TestCase):
    def test_requests_with_optional_query_parameters(self):
        methods = ('GET', 'HEAD', 'POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE')
        cases = (
            ('omitted', {}),
            ('none', {'query_params': None}),
            ('empty', {'query_params': []}),
            ('populated', {'query_params': [('limit', 10)]}),
        )
        for method in methods:
            for label, kwargs in cases:
                with self.subTest(method=method, query_params=label):
                    with ApiClient(Configuration(username='test_key')) as client:
                        transport = Mock(return_value=urllib3.HTTPResponse(
                            body=b'{}', status=200, headers={}
                        ))
                        client.rest_client.pool_manager.request = transport
                        client.call_api('/addresses', method, **kwargs)
                        transport.assert_called_once()
                        args, request_kwargs = transport.call_args
                        self.assertEqual(args[0], method)
                        expected_url = 'https://api.lob.com/v1/addresses'
                        if method in ('GET', 'HEAD'):
                            self.assertEqual(request_kwargs['fields'],
                                             [('limit', 10)] if label == 'populated' else [])
                        elif label == 'populated':
                            expected_url += '?limit=10'
                        self.assertEqual(args[1], expected_url)


if __name__ == '__main__':
    unittest.main()
