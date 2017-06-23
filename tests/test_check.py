import lob
import unittest

class CheckFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'
        self.addr = lob.Address.list(limit=1).data[0]
        self.ba = lob.BankAccount.create(
            routing_number = '122100024',
            account_number = '123456789',
            account_type = 'company',
            signatory = 'John Doe'
        )
        lob.BankAccount.verify(id=self.ba.id, amounts=[20, 80])

    def test_list_checks(self):
        checks = lob.Check.list()
        self.assertTrue(isinstance(checks.data[0], lob.Check))
        self.assertEqual(checks.object, 'list')

    def test_list_checks_limit(self):
        checks = lob.Check.list(limit=2)
        self.assertTrue(isinstance(checks.data[0], lob.Check))
        self.assertEqual(len(checks.data), 2)

    def test_list_checks_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Check.list, limit=1000)

    def test_create_check(self):
        check = lob.Check.create(
            description = 'Test Check',
            bank_account = self.ba.id,
            to_address = self.addr.id,
            from_address = self.addr.id,
            amount = 1000,
            memo = 'Test Check'
        )

        self.assertTrue(isinstance(check, lob.Check))
        self.assertEqual(check.bank_account.id, self.ba.id)
        self.assertEqual(check.to_address.id, self.addr.id)
        self.assertEqual(check.from_address.id, self.addr.id)

    def test_create_check_inline(self):
        check = lob.Check.create(
            description = 'Test Check',
            bank_account = self.ba,
            to_address = {
                'name': 'Lob',
                'address_line1': '185 Berry Street',
                'address_line2': 'Suite 1510',
                'address_city': 'San Francisco',
                'address_zip': '94107',
                'address_state': 'CA'
            },
            from_address = {
                'name': 'Lob',
                'address_line1': '185 Berry Street',
                'address_line2': 'Suite 1510',
                'address_city': 'San Francisco',
                'address_zip': '94107',
                'address_state': 'CA'
            },
            amount = 1000,
            memo = 'Test Check'
        )

        self.assertTrue(isinstance(check, lob.Check))
        self.assertEqual(check.bank_account.id, self.ba.id)
        self.assertEqual(check.to_address.name, 'Lob')
        self.assertEqual(check.from_address.name, 'Lob')

    def test_delete_postcard(self):
        check = lob.Check.create(
            description = 'Test Check',
            bank_account = self.ba.id,
            to_address = self.addr.id,
            from_address = self.addr.id,
            amount = 1000,
            memo = 'Test Check'
        )
        deleted_response = lob.Check.delete(check.id);
        self.assertTrue(deleted_response.deleted)

    def test_create_check_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Check.create)

    def test_retrieve_check(self):
        check = lob.Check.retrieve(id=lob.Check.list().data[0].id)
        self.assertTrue(isinstance(check, lob.Check))

    def test_retrieve_check_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Check.retrieve, id='test')
