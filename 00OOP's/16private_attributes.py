"""
Private attributes and methods : are meant to be used only within the class and are not accessible from outside the class
if we wanted to make any attribute private then make sure to put 2 underscores before them to make them private
"""

class Account:
    def __init__(self, name, acc_no, acc_pw):
        self.name = name
        self.account_no = acc_no
        self.__account_pw = acc_pw

    def pw_reset(self):
        print(f"Current pw is : {self.__account_pw}")  # we can access the private attributes within the class for our required use 



acc1 = Account("Chenchu", 904657322, "Chenchu@143")
print(acc1.name)
acc1.pw_reset()
print(acc1.__account_pw) # this would result the error as we don't have access to access them as they are private
