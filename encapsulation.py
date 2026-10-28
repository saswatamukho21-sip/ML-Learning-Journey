class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance

    def deposit(self,amount):
        if amount >0:
            self.__balance +=amount
            print(f"Deposited:{amount} ;New balance:{self.__balance}")

    def withdraw(self,amount):
        if amount>self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -=amount
            print(f"Withdrawn:{amount};Current balance:{self.__balance}")

    def get_balance(self):
        return self.__balance

account=BankAccount("Rahul",10000)
account.deposit(2000)
account.withdraw(550)
print(account.get_balance())
        
