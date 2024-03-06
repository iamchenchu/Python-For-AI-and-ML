"""
Private(like) attributes and methods : Conceptual implementations in python
Private attributes and methods are meant to be used only within the class and are not accessible from outside the class

"""

class Account:
    def __init__(self, acc_no, acc_pw):
        self.acc_no = acc_no
        self.__acc_pw = acc_pw # making private

    def reset_pw(self):
        print(self.__acc_pw) # we can access as we are doing this within the class


cx1 = Account(635272, "Chenchu@143")

print(cx1.acc_no)
cx1.reset_pw() # Through this we can access the pw 
print(cx1.__acc_pw) # can not access as we are doing it outside of the class