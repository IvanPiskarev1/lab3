class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def add(self, amount):
        self.__balance += amount

    def remove(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount(50)
account.add(60)
account.remove(50)
print(account.get_balance())