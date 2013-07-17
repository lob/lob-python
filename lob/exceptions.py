class LobError(Exception):
    def __init__(self, error=None, http_body=None,
                 http_status=None, json_body=None):
        super(LobError, self).__init__(error)
        self.http_body = http_body or http_body.decode('utf-8')
        self.http_status = http_status
        self.json_body = json_body


class APIError(LobError):
    pass


class APIConnectionError(LobError):
    pass


class InvalidRequestError(LobError):
    pass


class AuthenticationError(LobError):
    pass
