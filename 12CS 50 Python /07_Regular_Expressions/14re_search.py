import re

url = input("URL : ").strip()

matches = re.search(r"https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)

if matches:
    print(f"Username : ", matches.group(2))

"""
if := matches = re.search(r"https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
    print(f"Username : ", matches.group(2))  # this block also work 

"""