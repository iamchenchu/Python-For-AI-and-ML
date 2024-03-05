"""
Create account class with 2 attributes - balence and account no
Create methods for debit, credit and printing the balence
"""

class Account:
    def __init__(self, balence, account_no):
        self.balence = balence
        self.account_no = account_no

    def debit(self, num):
        self.balence = self.balence - num
        print(f"The remaining balence in the account {self.account_no} is : {self.balence}")

    def credit(self, num):
        self.balence += num
        print(f"The Updated balence in the account {self.account_no} is :{self.balence}")

    def bal(self):
        print(f"The Updated balence in {self.account_no} account is {self.balence}")

    

customer1 = Account(3000, 1234)
customer1.credit(100)
customer1.debit(2000)
customer1.credit(10000)
customer1.bal()
