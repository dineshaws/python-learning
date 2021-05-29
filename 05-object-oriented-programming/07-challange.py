# For this challenge, create a bank account class that has two attributes:

# owner
# balance
# and two methods:

# deposit
# withdraw
# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


class BankAccount():
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} deposited successfully')

    def withdraw(self, amount):
        if (amount > self.balance):
            print(f'\n Your withdrawl amount {amount} exceed to bank deposit')
            return False
        self.balance -= amount
        print(f'{amount} withdrawl successfully')
        return True

    def current_balance(self):
        print(f'Owner {self.owner} current balance is {self.balance}')


ba = BankAccount('Foo', balance=0)
ba.current_balance()
ba.deposit(100)
ba.current_balance()
ba.withdraw(200)
ba.withdraw(50)
ba.current_balance()
ba.deposit(1000)
ba.current_balance()
ba.withdraw(200)
ba.current_balance()