from __future__ import unicode_literals

import requests

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
        payload = resp.json()
        if resp.status_code == 200:
            return payload

        error_message = payload.get('error', {}).get('message')
        if resp.status_code == 401:
            raise error.AuthenticationError(error_message,
                resp.content, resp.status_code, resp)
        elif resp.status_code in [404, 422]:
            raise error.InvalidRequestError(error_message,
                resp.content, resp.status_code, resp)
        else: # pragma: no cover
            raise error.APIError(error_message, resp.content, resp.status_code, resp)


    def request(self, method, url, params=None):
        headers = {
            'User-Agent': 'Lob/v1 PythonBindings/%s' % VERSION
        }

        if hasattr(lob, 'api_version'):
            headers['Lob-Version'] = lob.api_version

        if method == 'get':
            return self.parse_response(
                requests.get(lob.api_base + url, auth=(self.api_key, ''), params=params, headers=headers)
            )
        elif method == 'delete':
            return self.parse_response(
                requests.delete(lob.api_base + url, auth=(self.api_key, ''), headers=headers)
            )
        elif method == 'post':
            data = {}
            files = params.pop('files', {})
            explodedParams = {}

            for k,v in params.items():
                if isinstance(v, dict) and not isinstance(v, lob.resource.LobObject):
                    for k2,v2 in v.items():
                        explodedParams[k + '[' + k2 + ']'] = v2
                else:
                    explodedParams[k] = v

            for k,v in explodedParams.items():
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
                requests.post(lob.api_base + url, auth=(self.api_key, ''), data=data, files=files, headers=headers)
            )
