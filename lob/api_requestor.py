import requests
import lob
import json
import resource
from lob import error

class APIRequestor(object):
    def __init__(self, key=None):
        self.api_key = key or lob.api_key

    def parse_response(self, resp):
        payload = json.loads(resp.content)
        if resp.status_code == 200:
            return payload
        elif resp.status_code == 401:
            raise error.AuthenticationError(payload['errors'][0]['message'],
                resp.content, resp.status_code, resp)
        elif resp.status_code in [404, 422]:
            raise error.InvalidRequestError(payload['errors'][0]['message'],
                resp.content, resp.status_code, resp)
        else:
            raise error.APIError(payload['errors'][0]['message'],
                    resp.content, resp.status_code, resp) #pragma: no cover

    def request(self, method, url, params=None):
        if method == 'get':
            return self.parse_response(
                requests.get(lob.api_base + url, auth=(self.api_key, ''), params=params)
            )
        elif method == 'delete':
            return self.parse_response(
                requests.delete(lob.api_base + url, auth=(self.api_key, ''))
            )
        elif method == 'post':
            data = {}
            files = {}
            explodedParams = {}

            for k,v in params.iteritems():
                if isinstance(v, dict) and not isinstance(v, resource.LobObject):
                    for k2,v2 in v.iteritems():
                        explodedParams[k + '[' + k2 + ']'] = v2
                else:
                    explodedParams[k] = v

            for k,v in explodedParams.iteritems():
                if isinstance(v, file):
                    files[k] = v
                else:
                    if isinstance(v, resource.LobObject):
                        data[k] = v.id
                    else:
                        data[k] = v

            return self.parse_response(
                requests.post(lob.api_base + url, auth=(self.api_key, ''), data=data, files=files)
            )

