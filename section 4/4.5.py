class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # прихований атрибут

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # 150
