import requests
import lob
import json
from lob import error

class APIRequestor(object):
  def __init__(self, key=None):
    self.api_key = lob.api_key

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
        resp.content, resp.status_code, resp)

  def request(self, method, url, params=None):
    if method == 'get':
      return self.parse_response(
          requests.get(lob.api_base + url, auth=(self.api_key, ''), params=params)
      )
    if method == 'delete':
      return self.parse_response(
        requests.delete(lob.api_base + url, auth=(self.api_key, ''))
      )

