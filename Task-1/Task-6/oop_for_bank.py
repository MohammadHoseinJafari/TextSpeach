# Task 1 - 7

# I make a Bank Class for have all accounts at the one point
# I have 5 method : create_account , Transfer_net , display_net , transaction_history , get_customer_info

class Bank:
    def __init__(self):
        self.accounts = []

    #create account for every customer with ' Account Class() '
    def create_account(self, customer):
        account = Account(customer)
        self.accounts.append(account)
        return account

    # transfer some network(amount of money) to another account with Account class method like (withdraw or deposit)
    def transfer_net(self, from_account, to_account, amount):
        if from_account.withdraw(amount):
            to_account.deposit(amount)
            print("transfer is successfully.")
        else:
            print("operations failed .its will back to your account.")

    # print current net at the bank acount
    def display_net(self, account):
        balance = account.get_balance()
        print(f"Current network : {balance}")

    # print all transactions which done by current customer
    def transaction_history(self, account):
        history = account.get_transaction_history()
        print("Transaction History:")
        for transaction in history:
            print(transaction)

    # print all of info for current user (customer)
    def get_customer_info(self, customer):
        info = customer.get_info()
        print(f"Customer Information : {info}")

# Account Class for acounting works
# at the Account Class i Hava 4 method :
# method 1 (deposit) -> for deposit money from account
# method 2 (withdraw) -> for withdraw money from account
# method 3 (get_balance) -> print amount of money account
# method 1 (get_transaction_history) -> for print transaction history like (deposit-withdraw-transfer) you have in the bank system

class Account:
    def __init__(self, customer):
        self.customer = customer
        self.balance = 0
        self.transaction_history = []

    #method 1
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +{amount}") # deposit -> variz

    #method 2
    def withdraw(self, amount):
        if self.balance >= amount: #check if a amount for transaction are bigger than balance money
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -{amount}") # Withdraw -> bardasht
            return True
        else:
            return False

    #method 3
    def get_balance(self):
        return self.balance

    #method 4
    def get_transaction_history(self):
        return self.transaction_history

# Person Class : for save User Informations
# this class include 1 method
# method 1 (get_info) : print all informations from current customer

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    # method 1
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"


# Customer Class Inheritance from Person Class : Inheritance some User Informations
# this class include 1 method
# method 1 (create_account) : Create a acount for user (By Account Classes) after get name and some informations
class Customer(Person):
    def __init__(self, name, age, address):
        super().__init__(name, age, address)
        self.accounts = []
    # method 1
    def create_account(self, bank):
        account = Account(self)
        bank.accounts.append(account)
        self.accounts.append(account)
        return account

#My Object from Above classes
bank = Bank()
customer = Customer("MohammadHosein-Jafari", 22, "Khayam Blv,Mashhad")
account = customer.create_account(bank)
account.deposit(1000)

# result :
print(customer.get_info())
print(account.get_transaction_history())
