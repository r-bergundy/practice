""" Unit Tests for account.py"""

import unittest
import bin.account as account


class TestAccount(unittest.TestCase):

    def test_get_balance(self):
        user_account = account.Account("ron", "r@b.com", 20000)
        balance = user_account.get_balance()
        self.assertEquals(20000, balance)

    def test_get_name(self):
        user_account = account.Account("ron", "r@b.com", 2000)
        name = user_account.get_name()
        self.assertTrue("ron", name)

    def test_deposit(self):
        user_account = account.Account("ron", "r@b.com", 20000)
        user_account.deposit_amount(20000)
        new_balance = user_account.get_balance()
        self.assertEquals(new_balance, 40000)

    def test_withdraw(self):
        user_account = account.Account("ron", "r@b.com", 20000)
        user_account.withdraw_amount(10000)
        new_balance = user_account.get_balance()
        self.assertEquals(new_balance, 10000)

    def test_insufficient_funds(self):
        user_account = account.Account("ron", "r@b.com", 9000)
        self.assertRaises(SystemExit, user_account.withdraw_amount, 10000)

if __name__ == '__main__':
    unittest.main()
