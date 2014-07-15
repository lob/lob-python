import lob
import unittest
# Setting the API key

class CheckFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'
        self.addr = lob.Address.list(count=1).data[0]
        self.ba = lob.BankAccount.list(count=1).data[0]

    def test_list_checks(self):
        checks = lob.Check.list()
        self.assertTrue(isinstance(checks.data[0], lob.Check))
        self.assertEqual(checks.object, 'list')

    def test_list_checks_limit(self):
        checks = lob.Check.list(count=2)
        self.assertTrue(isinstance(checks.data[0], lob.Check))
        self.assertEqual(len(checks.data), 2)

    def test_list_checks_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Check.list, count=1000)

    def test_create_check(self):
        check = lob.Check.create(
            name = 'Test Check',
            bank_account = self.ba.id,
            to = self.addr.id,
            amount = 1000,
            memo = 'Test Check'
        )

        self.assertTrue(isinstance(check, lob.Check))
        self.assertEqual(check.bank_account.id, self.ba.id)
        self.assertEqual(check.to.id, self.addr.id)

    def test_create_check_lob_obj(self):
        check = lob.Check.create(
            name = 'Test Check',
            bank_account = self.ba,
            to = self.addr,
            amount = 1000,
            memo = 'Test Check'
        )

        self.assertTrue(isinstance(check, lob.Check))
        self.assertEqual(check.bank_account.id, self.ba.id)
        self.assertEqual(check.to.id, self.addr.id)

    def test_create_check_inline(self):
        check = lob.Check.create(
            name = 'Test Check',
            bank_account = self.ba,
            to= {
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
        self.assertEqual(check.to.name, 'Lob')

    def test_create_check_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Check.create)

    def test_retrieve_check(self):
        check = lob.Check.retrieve(id=lob.Check.list().data[0].id)
        self.assertTrue(isinstance(check, lob.Check))

    def test_retrieve_check_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Check.retrieve, id='test')
