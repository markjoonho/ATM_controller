from controller import Controller
from view import View


def main():
    controller = Controller()
    view = View(controller)
    print("Welcome Joonho Bank :) ", end="")
    while True:
        print("Are you a new customer? (y/n)")
        x = input()
        if x == "n":
            controller.sign_in()
            break
        elif x == "y":
            controller.make_card()
            break
        else:
            pass

    
    controller.call_card()
    while True:
        controller.bank_work()


main()
