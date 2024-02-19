
url = input("What's your twitter URL :").strip()

username = url.replace("https://twitter.com/", "")

print(f"your user name is : {username}")