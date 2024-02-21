"""
Encapsulation : Wrapping the data and functions into a single unit(Object)

"""

# Create a bank account class with 2 attributes - balance and account no 
# create methods for debit, credit & printing the balance 

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("Total Balance left now = ", self.get_balance())
    
    def credit(self, amount):
        self.balance += amount
        print("Rs : ", amount, " Was credited")
        print("Total Balance left now = ", self.get_balance())

    def get_balance(self):
        return self.balance



acc1 = Account(10000, 123455)
acc1.debit(300)
acc1.credit(5000)




