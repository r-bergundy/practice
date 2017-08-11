""" This is a test Account class """
import logging
import sys


class Account:

    def __init__(self, name, email, balance):
        self.balance = balance
        self.name = name
        self.email = email

    def get_name(self):
        logging.info("Retrieving Account Name....")
        logging.info("> " + str(self.name))
        return self.name

    def get_email(self):
        logging.info("Retrieving Account Email....")
        logging.info("> " + str(self.email))
        return self.email

    def get_balance(self):
        logging.info("Retrieving Account Balance....")
        logging.info("> " + str(self.balance))
        return self.balance

    def withdraw_amount(self, amount_to_withdraw):
        logging.info("Withdrawing " + str(amount_to_withdraw))
        if self.balance < amount_to_withdraw:
            logging.warning("Not enough funds in the balance to withdraw that"
                            " ammount")
            sys.exit(1)
        else:
            self.balance = self.balance - amount_to_withdraw

    def deposit_amount(self, amount_to_deposit):
        logging.info("Depositing " + str(amount_to_deposit))
        self.balance = self.balance + amount_to_deposit
