# pip install requests : this requests api will be installed
# JSON : Java Script Object Notation
# API : Application programming interface

import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])


o = response.json()
for result in o["results"]:
    print(result["trackName"])

# should run it as : python3 08apis.py weezer
