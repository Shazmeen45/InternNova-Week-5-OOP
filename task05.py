from abc import ABC, abstractmethod

# Abstract parent class
class BankAccount(ABC):
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.__balance

    def _set_balance(self, amount):
        self.__balance = amount

# Child class
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            new_balance = self.get_balance() + amount
            self._set_balance(new_balance)
            print("Amount deposited:", amount)
        else:
            print("Please enter a valid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount <= self.get_balance():
            new_balance = self.get_balance() - amount
            self._set_balance(new_balance)
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance.")

    def display_info(self):
        print("Account Holder:", self.name)
        print("Account Balance:", self.get_balance())

# Creating a bank account object
account = SavingsAccount("Shazmeen", 5000)

# Displaying initial account information
account.display_info()
print()

# Depositing money
account.deposit(2000)
account.display_info()
print()

# Withdrawing money
account.withdraw(1000)
account.display_info()
