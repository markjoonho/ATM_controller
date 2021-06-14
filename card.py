from random import randrange
from account import Account


class Card:
    def __init__(self, card_num=randrange(100000, 999999)):
        self.card_num = card_num
        self.pin = "000000"
        self.accounts = []

    def get_card_num(self):
        return self.card_num

    def set_pin(self, pin):
        self.pin = pin

    def get_pin(self):
        return self.pin

    def make_account(self, account_type, event=0):
        if account_type == "c":
            new_account = Account(self.card_num, "Chequeing", event)
        elif account_type == "s":
            new_account = Account(self.card_num, "Saving", event)
        elif account_type == "r":
            new_account = Account(self.card_num, "Credit", event)
        self.accounts.append(new_account)

    def get_accounts(self):
        return self.accounts

    def get_account(self, account):
        for acc in self.accounts:
            if acc.get_type()[0].lower() == account:
                return acc

        return None

    # def get_balance(self, account):
    #     current_account = self.get_account(account)
    #     return current_account.get_balance

    # def withdraw(self, account, balance):
    #     current_account = self.get_account(account)
    #     return current_account.minus_balance(balance)
