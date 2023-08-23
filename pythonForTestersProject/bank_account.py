class BankAccount:
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance can not be negative!")
        self.__balance = new_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount can not be zero or negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount can not be zero or negative")
        if amount > self.balance:
            raise ValueError("Not enough funds!")
        self.balance -= amount


account = BankAccount()
account.deposit(100)
print(account.balance)

account.withdraw(50)
print(account.balance)

account.withdraw(60)