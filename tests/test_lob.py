import unittest
import lob
import requests_mock
import base64

class TestLob(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'asdf'
        lob.api_version = 'apiVersion'

    def test_bad_auth(self):
        self.assertRaises(lob.error.AuthenticationError, lob.Address.list)

    def test_set_version(self):
        self.assertEqual(lob.api_version, 'apiVersion')
    
    def show_list(self, request, context):
        return {
            "data": [
                {
                "id": "adr_e68217bd744d65c8",
                "description": "Harry - Office",
                "name": "HARRY ZHANG",
                "company": "LOB",
                "phone": "5555555555",
                "email": "harry@lob.com",
                "address_line1": "210 KING ST STE 6100",
                "address_line2": None,
                "address_city": "SAN FRANCISCO",
                "address_state": "CA",
                "address_zip": "94107-1741",
                "address_country": "UNITED STATES",
                "metadata": {},
                "date_created": "2019-08-12T00:16:00.361Z",
                "date_modified": "2019-08-12T00:16:00.361Z",
                "object": "address"
                },
                {
                "id": "adr_asdi2y3riuasasoi",
                "description": "Harry - Office",
                "name": "Harry Zhang",
                "company": "Lob",
                "phone": "5555555555",
                "email": "harry@lob.com",
                "metadata": {},
                "address_line1": "370 WATER ST",
                "address_line2": "",
                "address_city": "SUMMERSIDE",
                "address_state": "PRINCE EDWARD ISLAND",
                "address_zip": "C1N 1C4",
                "address_country": "CANADA",
                "date_created": "2019-09-20T00:14:00.361Z",
                "date_modified": "2019-09-20T00:14:00.361Z",
                "object": "address"
                }
            ],
            "object": "list",
            "next_url": "https://api.lob.com/v1/addresses?limit=2&after=eyJkYXRlT2Zmc2V0IjoiMjAxOS0wOC0wN1QyMTo1OTo0Ni43NjRaIiwiaWRPZmZzZXQiOiJhZHJfODMwYmYwZWFiZGFhYTQwOSJ9",
            "previous_url": None,
            "count": 2
        }

    def parse_header_string(self, header):
        auth_str = header['Authorization'].split(" ")
        return base64.b64decode(auth_str[1])

    @requests_mock.Mocker()
    def test_set_different_api_keys_per_call(self, adapter):
        adapter.register_uri('GET', 'https://api.lob.com/v1/addresses', json=self.show_list)
        lob.Address.list(api_key='key12345')
        decoded_api_key = self.parse_header_string(adapter.last_request.headers)
        self.assertEqual(bytes('key12345:', 'utf8'), decoded_api_key)
        lob.Address.list(api_key='key98765')
        decoded_api_key = self.parse_header_string(adapter.last_request.headers)
        self.assertEqual(bytes('key98765:', 'utf8'), decoded_api_key)

    def tearDown(self):
        del lob.api_version
