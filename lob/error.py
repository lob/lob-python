from __future__ import unicode_literals


class LobError(Exception):

    def __init__(self, message=None, http_body=None, http_status=None,
                 json_body=None):
        super(LobError, self).__init__(message)
        self.http_body = http_body
        self.http_status = http_status
        self.json_body = json_body


class APIError(LobError):
    pass


class APIConnectionError(LobError):
    pass


class AuthenticationError(LobError):
    pass


class InvalidRequestError(LobError):
    pass
