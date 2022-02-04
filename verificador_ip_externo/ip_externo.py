import re
import json
from urllib.request import urlopen


url = "http://ipinfo.io/json"
response = urlopen(url)
data = json.load(response)

for key, value in data.items():
    print(f'{key}: {value}')