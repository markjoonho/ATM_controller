from card import Card
from account import Account
from subject import Subject


class Controller(Subject):
    def __init__(self):
        self.cards = [Card("000000")]
        self.current_card = None
        self.current_account = None

        self.sign_up = False
        self.sign_in_ = False
        self.sign_in_id = False
        self.sign_in_pwd = False
        self.sign_in_id_invalid = False
        self.sign_in_pwd_invalid = False

        self.select_account = False
        self.make_new_account = False
        self.account_exist = False
        self.banking = False
        self.banking_type = "a"
        self.banking_work_done = False
        self.withdraw_fail = False

        super().__init__()

    def add_card(self, card):
        self.cards.append(card)

    def make_card(self):
        self.sign_up = True
        my_card = Card()
        super().notifyObserver(my_card.get_card_num())
        x = input()
        my_card.set_pin(x)
        pin = my_card.get_pin()

        self.add_card(my_card)
        self.sign_up = False
        self.sign_in()

    def sign_in(self):
        self.sign_in_id = True
        super().notifyObserver()
        self.sign_in_id = False

        x = input()
        for card in self.cards:
            if str(card.get_card_num()) == x:
                self.sign_in_pwd = True
                super().notifyObserver()
                self.sign_in_pwd = False

                x = input()
                if str(card.get_pin()) == x:
                    self.current_card = card
                    self.sign_in_ = True
                    super().notifyObserver()
                    self.sign_in_ = False
                    return
                else:
                    self.sign_in_pwd_invalid = True
                    super().notifyObserver()
                    self.sign_in_pwd_invalid = False
                    x = input()
                    if x == "t":
                        self.sign_in()
                        return
                    elif x == "m":
                        self.make_card()
                    else:
                        exit(1)
                        return
        self.sign_in_id_invalid = True
        super().notifyObserver()
        self.sign_in_id_invalid = False

        x = input()
        if x == "t":
            self.sign_in()
            return
        elif x == "m":
            self.make_card()
        else:
            exit(1)
            return

    def call_card(self):

        self.select_account = True
        super().notifyObserver()
        self.select_account = False

        x = input()
        if x == "m":
            self.make_account()
        elif x == "l":
            self.current_account = None
            self.current_card = None
            self.sign_in()
            return
        elif x == "q":
            exit(1)
        elif x in "csr":
            self.call_account(x)
            self.bank_work()
        else:
            self.call_card()

    def call_account(self, account):
        self.current_account = self.current_card.get_account(account)
        if self.current_account is None:
            self.call_card()

    def make_account(self):
        self.make_new_account = True
        super().notifyObserver()
        self.make_new_account = False

        account_type = input()

        for account in self.get_accounts():
            if account.get_type()[0].lower() == account_type:
                self.account_exist = True
                super().notifyObserver()
                self.account_exist = False
                self.call_card()
                return

        if account_type in ["c", "s", "r"]:
            self.current_card.make_account(account_type)
            self.call_card()
        else:
            self.call_card()

    def bank_work(self):
        if self.current_account == None:
            self.call_card()

        self.banking = True
        super().notifyObserver()
        self.banking = False
        x = input()
        if x == "d":
            self.banking_type = "d"
            super().notifyObserver()
            self.banking_type = "a"
            num = input()
            self.current_account.add_balance(int(num))
        elif x == "w":
            self.banking_type = "w"
            super().notifyObserver()
            self.banking_type = "a"
            num = input()
            if self.current_account.minus_balance(int(num)) == False:
                self.withdraw_fail = True
                super().notifyObserver()
                self.withdraw_fail = False
        elif x == "b":
            self.banking_type = "b"
            super().notifyObserver()
            self.banking_type = "a"
        elif x == "r":
            self.call_card()
        elif x == "q":
            self.banking_type = "q"
            super().notifyObserver()
            self.banking_type = "a"
            exit(1)

        self.banking_work_done = True
        super().notifyObserver()
        self.banking_work_done = False

    def get_accounts(self):
        return self.current_card.get_accounts()

    def get_type(self):
        return self.current_account.get_type()

    def get_certain_type(self, account):
        return account.get_type()

    def get_balance(self):
        return self.current_account.get_balance()
