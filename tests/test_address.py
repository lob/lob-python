import unittest
import lob
# Setting the API key

# Create an address

class TestAddressFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

    def test_list_addresses(self):
        addresses = lob.Address.list()
        self.assertTrue(isinstance(addresses.data[0], lob.Address))
        self.assertEqual(addresses.object, 'list')

    def test_list_addresses_limit(self):
        addresses = lob.Address.list(count=2)
        self.assertTrue(isinstance(addresses.data[0], lob.Address))
        self.assertEqual(len(addresses.data), 2)

    def test_list_address_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Address.list, count=1000)

    def test_create_address(self):
        address = lob.Address.create(
            name='Lob',
            address_line1='185 Berry Street',
            address_line2='Suite 1510',
            address_city='San Francisco',
            address_zip='94017',
            address_state='CA',
            address_country='US'
        )

        self.assertTrue(isinstance(address, lob.Address))
        self.assertEqual(address.name, 'Lob')

    def test_create_addresss_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Address.create)

    def test_retrieve_address(self):
        address = lob.Address.retrieve(id=lob.Address.list().data[0].id)
        self.assertTrue(isinstance(address, lob.Address))

    def test_retrieve_address_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Address.retrieve, id='test')


    def test_delete_address(self):
        addr = lob.Address.list().data[0].id
        delAddr = lob.Address.delete(id=addr)
        self.assertEqual(addr, delAddr.id)


    def test_address_verification(self):
        addr = lob.Verification.create(
            address_line1='220 William T Morrissey',
            address_city='Boston',
            address_state='MA',
            address_zip='02125',
            address_country='US'
        )

        self.assertEqual(addr.address.address_line1, '220 WILLIAM T MORRISSEY BLVD')

