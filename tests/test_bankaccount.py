import unittest
import lob
# Setting the API key
lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

class BankAccountFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'
        self.addr = lob.Address.list(count=1).data[0]

    def test_list_bankAccounts(self):
        bankAccounts = lob.BankAccount.list()
        self.assertTrue(isinstance(bankAccounts.data[0], lob.BankAccount))
        self.assertEqual(bankAccounts.object, 'list')

    def test_list_bankAccounts_limit(self):
        bankAccounts = lob.BankAccount.list(count=2)
        self.assertTrue(isinstance(bankAccounts.data[0], lob.BankAccount))
        self.assertEqual(len(bankAccounts.data), 2)

    def test_list_bankAccounts_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.BankAccount.list, count=1000)


    def test_create_bankAccount(self):
        bankAccount = lob.BankAccount.create(
            routing_number='123456789',
            account_number='123456789',
            bank_address=self.addr.id,
            account_address=self.addr.id
        )
        self.assertTrue(isinstance(bankAccount, lob.BankAccount))
        self.assertEqual(bankAccount.bank_address.id, self.addr.id)

    def test_create_bankAccount_lob_obj(self):
        bankAccount = lob.BankAccount.create(
            routing_number='123456789',
            account_number='123456789',
            bank_address=self.addr,
            account_address=self.addr
        )
        self.assertTrue(isinstance(bankAccount, lob.BankAccount))
        self.assertEqual(bankAccount.bank_address.id, self.addr.id)

    def test_create_bankAccount_inline(self):
        bankAccount = lob.BankAccount.create(
            routing_number='123456789',
            account_number='123456789',
            bank_address= {
                'name': 'Lob1',
                'address_line1': '185 Berry Street',
                'address_line2': 'Suite 1510',
                'address_city': 'San Francisco',
                'address_zip': '94107',
                'address_state': 'CA'
            },
            account_address= {
                'name': 'Lob2',
                'address_line1': '185 Berry Street',
                'address_line2': 'Suite 1510',
                'address_city': 'San Francisco',
                'address_zip': '94107',
                'address_state': 'CA'
            }
        )
        self.assertTrue(isinstance(bankAccount, lob.BankAccount))
        self.assertEquals(bankAccount.bank_address.name, 'Lob1')
        self.assertEquals(bankAccount.account_address.name, 'Lob2')

    def test_retrieve_bankAccount(self):
        bankAccount = lob.BankAccount.retrieve(id=lob.BankAccount.list().data[0].id)
        self.assertTrue(isinstance(bankAccount, lob.BankAccount))

    def test_retrieve_bankAccount_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.BankAccount.retrieve, id='test')


    def test_delete_bankAccount(self):
        ba = lob.BankAccount.list().data[0].id
        delBa = lob.BankAccount.delete(id=ba)
        self.assertEqual(ba, delBa.id)

