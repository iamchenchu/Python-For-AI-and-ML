import re

url = input("What's your URL : ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"username : ", matches.group(1))


"""
there are other functions too other than this one 
re.sub(pattern, repl, string, count=0, flags=0)
re.findall(pattern, string, flags=0)
"""