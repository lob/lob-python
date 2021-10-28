import unittest
import lob
import pytest
import requests_mock
class TimeoutTests(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'mockAPIkey123'
    
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
    def test_connection_timeout_on_get_requests(self, adapter):
        adapter.register_uri('GET', 'https://api.lob.com/v1/addresses', json=self.return_list)
        lob.Address.list(timeout=3)
        self.assertEqual(3, adapter.last_request.timeout)
    
    @requests_mock.Mocker()
    def test_connection_timeout_triggers_on_delete_requests(self, adapter):
        adapter.register_uri('DELETE', 'https://api.lob.com/v1/addresses/adr_12345', json=self.return_single)
        lob.Address.delete(id='adr_12345', timeout=22)
        self.assertEqual(22, adapter.last_request.timeout)


    @requests_mock.Mocker()
    def test_connection_timeout_triggers_on_post_requests(self, adapter):
        adapter.register_uri('POST', 'https://api.lob.com/v1/addresses', json=self.return_status)
        lob.Address.create(
            name='Lob',
            address_line1='185 Berry Street',
            address_line2='Suite 1510',
            address_city='San Francisco',
            address_zip='94017',
            address_state='CA',
            address_country='US',
            timeout=33
        )
        self.assertEqual(33, adapter.last_request.timeout)
