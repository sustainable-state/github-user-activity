from urllib import request
import json
from pprint import pprint

username = "sustainable-state"
url = f"https://api.github.com/users/{username}/events"

req = request.Request(url)

resp = request.urlopen(req)

resp_data = json.load(resp)

pprint(resp_data)

