class Account:
    def __init__(self, card_num, type, balance=0):
        self.card_num = card_num
        self.type = type
        self.balance = balance

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def add_balance(self, money):
        self.balance += money

    def get_balance(self):
        return self.balance

    def minus_balance(self, money):
        new_balance = self.balance - money
        if new_balance < 0:
            return False
            
        else:
            self.balance = new_balance
