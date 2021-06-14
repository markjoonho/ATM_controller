from observer import Observer
from controller import Controller


class View(Observer):
    def __init__(self, controller):
        self.controller = controller
        self.controller.attach(self)

    def notify(self, card_num=0):

        # sign up message
        if self.controller.sign_up:
            print("SIGN UP PAGE")
            print(f"\tNew Card Number: {card_num}.")
            print("\tPin for your New Card:", end=" ")

        # sign in message (id)
        if self.controller.sign_in_id:
            print("SIGN IN PAGE")
            print("\tCard Number:", end=" ")

        # sign in message (password)
        if self.controller.sign_in_pwd:
            print("\tPin:", end=" ")

        # sign in message (success)
        if self.controller.sign_in_:
            print("\nSIGNED IN SUCCESS! :)\n")

        # sign in message (invalid card number)
        if self.controller.sign_in_id_invalid:
            print("Invalid Card Num.")
            print("\t- Press(t) to try again.")
            print("\t- Press(m) to make new card.")
            print("\t- Press others to quit.")

        # sign in message (invalid password/pin)
        if self.controller.sign_in_pwd_invalid:
            print("Invalid Pin.")
            print("\t- Press(t) to try again.")
            print("\t- Press(m) to make new card.")
            print("\t- Press others to quit.")

        # select account type message
        if self.controller.select_account:
            print("Please Select Your Account")
            accounts = self.controller.get_accounts()
            for account in accounts:
                print(
                    f"\t - ({self.controller.get_certain_type(account)[0].lower()}) move to {self.controller.get_certain_type(account)}'s Account"
                )
            print("\t - (m) making New Account")
            print("\t - (l) log out")
            print("\t - (q) quit")

        # select account type message (make new account type)
        if self.controller.make_new_account:
            print("Enter your account type: ")
            print("\t - (c) for Chequing Account")
            print("\t - (s) for Saving Account")
            print("\t - (r) for Credit Account")
            print("\t - others for return")

        if self.controller.account_exist:
            print("\nThis account already exists!\n")

        # select bank work
        if self.controller.banking:
            print("Select Your Choice:")
            print("\t - (d) for Deposit")
            print("\t - (w) for Withdraw")
            print("\t - (b) for Check Balance")
            print("\t - (r) for return to account Select")
            print("\t - (q) for quit")

        # select bank work (deposit)
        if self.controller.banking_type == "d":
            print(f"Balance: {self.controller.get_balance()}")
            print("Enter your amount to deposit:", end=" ")

        # select bank work (withdraw)
        if self.controller.banking_type == "w":
            print(f"Balance: {self.controller.get_balance()}")
            print("Enter your amount to withdraw:", end=" ")

        # select bank work (withdraw fail, not enough amount to withdraw)
        if self.controller.withdraw_fail:
            print("Unable to withdraw! Please check your balance")

        # select bank work (balance check)
        if self.controller.banking_type == "b":
            print(f"Balance: {self.controller.get_balance()}")

        # select bank work (quit)
        if self.controller.banking_type == "q":
            print("Thank you for using Joonho Bank!")
            print(
                f"Your Balance for {self.controller.get_type()} account: {self.controller.get_balance()}"
            )

        # bank work done
        if self.controller.banking_work_done:
            print(
                f"\n{self.controller.get_type()} Account Balance: {self.controller.get_balance()}\n"
            )
