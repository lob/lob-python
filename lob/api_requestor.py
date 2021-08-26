from __future__ import unicode_literals

import requests
import json

import lob
from lob import error
from lob.version import VERSION


def _is_file_like(obj):
    """
    Checks if an object is file-like enough to be sent to requests.

    In particular, file, StringIO and cStringIO objects are file-like.
    Refs http://stackoverflow.com/questions/3450857/python-determining-if-an-object-is-file-like
    """
    return hasattr(obj, 'read') and hasattr(obj, 'seek')


class APIRequestor(object):
    def __init__(self, key=None):
        self.api_key = key or lob.api_key

    def parse_response(self, resp):
        if resp.status_code == 504:
            raise error.APIConnectionError(resp.content or resp.reason,  # pragma: no cover
                                           resp.content, resp.status_code, resp)

        payload = resp.json()
        if resp.status_code == 200:
            return payload
        elif resp.status_code == 401:
            raise error.AuthenticationError(payload['error']['message'],
                                            resp.content, resp.status_code, resp)
        elif resp.status_code in [404, 422]:
            raise error.InvalidRequestError(payload['error']['message'],
                                            resp.content, resp.status_code, resp)
        else:  # pragma: no cover
            raise error.APIError(payload['error']['message'], resp.content, resp.status_code, resp)

    def request(self, method, url, params=None):
        headers = {
            'User-Agent': 'Lob/v1 PythonBindings/%s' % VERSION
        }

        if hasattr(lob, 'api_version'):
            headers['Lob-Version'] = lob.api_version

        if params and 'lob_version' in params:
            headers['Lob-Version'] = params.pop('lob_version')

        if params and 'headers' in params:
            headers.update(params['headers'])
            del params['headers']

        if method == 'get':
            return self.parse_response(
                requests.get(lob.api_base + url, auth=(self.api_key, ''), params=params, headers=headers)
            )
        elif method == 'delete':
            return self.parse_response(
                requests.delete(lob.api_base + url, auth=(self.api_key, ''), headers=headers)
            )
        elif method == 'post':
            query = {}
            data = {}
            files = params.pop('files', {})
            explodedParams = {}

            if params and 'query' in params:
                query.update(params['query'])
                del params['query']

            for k, v in params.items():
                if k == 'merge_variables' or k == 'addresses':
                    explodedParams[k] = json.dumps(v)
                elif isinstance(v, dict) and not isinstance(v, lob.resource.LobObject):
                    for k2, v2 in v.items():
                        explodedParams[k + '[' + k2 + ']'] = v2
                else:
                    explodedParams[k] = v

            for k, v in explodedParams.items():
                if _is_file_like(v):
                    files[k] = v
                else:
                    if isinstance(v, lob.resource.LobObject):
                        data[k] = v.id
                    else:
                        if isinstance(v, dict):
                            for k2, v2 in v.items():
                                data[k + '[' + k2 + ']'] = v2
                        else:
                            data[k] = v

            return self.parse_response(
                requests.post(lob.api_base + url, auth=(self.api_key, ''), params=query, data=data, files=files, headers=headers)
            )
