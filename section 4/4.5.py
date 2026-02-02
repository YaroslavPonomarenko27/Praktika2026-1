class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Іван", 1000)

account.deposit(500)
account.withdraw(300)

print("Власник:", account.owner)
print("Баланс:", account.get_balance())
