class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self.__balance = balance             # Private attribute (hidden)

    # Public method to get balance
    def get_balance(self):
        return self.__balance

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive!")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount!")

# Create an instance of the BankAccount class
account = BankAccount("123456789", 1000)

# Accessing public attributes and methods
print(f"Account Number: {account.account_number}")
account.deposit(500)
account.withdraw(300)

# Attempting to access the private attribute directly (will raise an AttributeError)
# print(account.__balance)  # Uncommenting this line will cause an error

# Access private attribute using a public method
print(f"Balance: ${account.get_balance()}")
