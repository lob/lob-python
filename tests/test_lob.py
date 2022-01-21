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

    def parse_headers(self, headers):
        auth = headers['Authorization'].split(" ")
        return base64.b64decode(auth[1])
    
    def return_list(self, request, context):
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
    
    def return_status(self, request, context):
        return {
            "id": "adr_123456789",
            "deleted": True
        }

    def return_single(self, request, context):
        return {
                "id": "adr_d3489cd64c791ab5",
                "description": "Harry - Office",
                "name": "HARRY ZHANG",
                "company": "LOB",
                "phone": "5555555555",
                "email": "harry@lob.com",
                "address_line1": "210 KING ST STE 6100",
                "address_city": "SAN FRANCISCO",
                "address_state": "CA",
                "address_zip": "94107",
                "address_country": "UNITED STATES",
                "metadata": {},
                "date_created": "2017-09-05T17:47:53.767Z",
                "date_modified": "2017-09-05T17:47:53.767Z",
                "object": "address"
            }

    @requests_mock.Mocker()
    def test_different_api_keys_per_call(self, adapter):
        adapter.register_uri('GET', 'https://api.lob.com/v1/addresses', json=self.return_list)
        adapter.register_uri('POST', 'https://api.lob.com/v1/addresses', json=self.return_single)
        adapter.register_uri('GET', 'https://api.lob.com/v1/addresses/adr_12345', json=self.return_single)
        adapter.register_uri('DELETE', 'https://api.lob.com/v1/addresses/adr_12345', json=self.return_status)

        lob.Address.list(api_key='key12345')
        self.assertEqual(bytes('key12345:', 'utf8'), self.parse_headers(adapter.last_request.headers))
        lob.Address.create(
            name='Lob',
            address_line1='185 Berry Street',
            address_line2='Suite 1510',
            address_city='San Francisco',
            address_zip='94017',
            address_state='CA',
            address_country='US',
            api_key='key98765'
        )
        self.assertEqual(bytes('key98765:', 'utf8'), self.parse_headers(adapter.last_request.headers))
        lob.Address.retrieve(id='adr_12345', api_key='key9999')
        self.assertEqual(bytes('key9999:', 'utf8'), self.parse_headers(adapter.last_request.headers))
        lob.Address.delete(id='adr_12345', api_key='key8080')
        self.assertEqual(bytes('key8080:', 'utf8'), self.parse_headers(adapter.last_request.headers))

    def tearDown(self):
        del lob.api_version
