import unittest
import lob
# Setting the API key

# Create an address

class TestAddressFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

    def test_list_addresses(self):
        addresses = lob.Address.list()
        self.assertEqual(addresses)
#
#    def test_bad_address(self):
#        self.assertRaises(lob.error.InvalidRequestError, lob.Address.create)
#
#    def test_address(self):
#        address = lob.Address.create(name='Lob', address_line1='104, Printing Boulevard',
#                address_city='Boston', address_state='MA', address_country='US',
#                address_zip='12345')
#        print address
#
#
#    def test_address_other_parameters(self):
#        """Can also pass other parameters while creating an address"""
#        address = lob.Address.create(name='Lob', address_line1='104, Printing Boulevard',
#                address_line2='Sunset Town', email='support@lob.com',
#                address_city='Boston', address_state='MA', address_country='US',
#                address_zip='12345')
#        print address
#
#
#    def test_list_addresses(self):
#        print lob.Address.list()
#
#
#    def test_list_addresses_count_offset(self):
#        # Can also pass count and offset
#        print lob.Address.list(count=5, offset=2)
#
#
#    def test_find_address(self):
#        print lob.Address.retrieve(id=lob.Address.list(count=1).data[0].id)
#
#
#    def test_delete_address(self):
#        print lob.Address.delete(id=lob.Address.list(count=1).data[0].id)
#
#
#    def test_address_verification(self):
#        print lob.Verification.create(name='Lob',
#                email='support@lob.com',
#                address_line1='220 William T Morrissey',
#                address_city='Boston',
#                address_state='MA',
#                address_zip='02125',
#                address_country='US'
#                )
#
