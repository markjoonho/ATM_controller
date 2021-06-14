### Instruction

##### Python Version

3.8.6

> I used formatting function which does not exist in python 2. Please use python 3.X

##### Cloning the git repository

```bash
git clone https://github.com/markjoonho/ATM_controller.git
```

##### Run the code

- move in to the directory ATM_controller

```bash
python ./main.py
```

##### Debugging account

- Card Number: 000000

- Pin: 000000

> Or you can make your own account! :)

### Simple Description

This is the about simple ATM controller. Anyone can make card and create three different types of account(i.e. chequeing, saving, credit). You can deposit, withdraw or check balance

##### Sign In

When you first enter, you have 2 options.

> Welcome Joonho Bank :) Are you a new customer? (y/n)

If you choose `y`, they will let you to create new card. The card number is 6 digits randomize number.

If you choose `n`, they will let you to write card number and pin. (for debuggin you can use 000000 for both car number and pin)

##### Account Selecting

Now you are signed in! Now you have 3 or more choices

- (m) making New Account
- (l) log out
- (q) quit

If you choose `(m)`, now you are able to create accounts

- (c) for Chequing Account
- (s) for Saving Account
- (r) for Credit Account
- others for return

After you make account, you are automatically going back to Account selecting page with additional option.

- (c) move to Chequeing's Account
- (m) making New Account
- (l) log out
- (q) quit

Now you got a new Chequing Account.

##### Bank work

If you enter to the chequing account, they will give you 5 different options

- (d) for Deposit
- (w) for Withdraw
- (b) for Check Balance
- (r) for return to account Select
- (q) for quit

You can use whatever options!
