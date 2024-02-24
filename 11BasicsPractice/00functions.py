

def my_function(fname, lname):
    full_name = fname + lname
    print(f"Full name is : {fname} {lname}")
    return full_name

def email_making(fname, lname):
    
    email = my_function(fname, lname) + "@gmail.com"
    print("Email id is : "+ email)
    




email_making("Chenchu", "Reddy")
email_making("Rajia", "Reddy")