#Encapsulation restricts direct access to some object components, preventing accidental modification.
#It is implemented using private (__), protected (_), and public attributes.



class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

# Usage
acc = BankAccount("12345", 1000)
print(acc.get_balance())  # Access balance via method
