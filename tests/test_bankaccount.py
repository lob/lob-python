import unittest
import lob

class BankAccountFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'
        self.addr = lob.Address.list(limit=1).data[0]

    def test_list_bankAccounts(self):
        bankAccounts = lob.BankAccount.list()
        self.assertTrue(isinstance(bankAccounts.data[0], lob.BankAccount))
        self.assertEqual(bankAccounts.object, 'list')

    def test_list_bankAccounts_limit(self):
        bankAccounts = lob.BankAccount.list(limit=2)
        self.assertTrue(isinstance(bankAccounts.data[0], lob.BankAccount))
        self.assertEqual(len(bankAccounts.data), 2)

    def test_list_bankAccounts_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.BankAccount.list, limit=1000)

    def test_create_bankAccount_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.BankAccount.create)

    def test_create_bankAccount(self):
        bankAccount = lob.BankAccount.create(
            routing_number='122100024',
            account_number='123456789',
            signatory='John Doe'
        )
        self.assertTrue(isinstance(bankAccount, lob.BankAccount))

    def test_retrieve_bankAccount(self):
        bankAccount = lob.BankAccount.retrieve(id=lob.BankAccount.list().data[0].id)
        self.assertTrue(isinstance(bankAccount, lob.BankAccount))

    def test_retrieve_bankAccount_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.BankAccount.retrieve, id='test')

    def test_delete_bankAccount(self):
        ba = lob.BankAccount.list().data[0].id
        delBa = lob.BankAccount.delete(id=ba)
        self.assertEqual(ba, delBa.id)

    def test_verify_bankAccount(self):
        ba = lob.BankAccount.create(
            routing_number='122100024',
            account_number='223456789',
            signatory='John Doe'
        )
        verBa = lob.BankAccount.verify(id=ba.id, amounts=[25, 75])
        self.assertTrue(verBa.verified)
