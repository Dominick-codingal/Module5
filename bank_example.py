class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self.__balance = balance    # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance
acc = BankAccount("Dominic", 5000)

acc.deposit(2000)
acc.withdraw(1000)

print(acc.get_balance())
