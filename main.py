import requests
import json
import config

headers = {
    'TRN-Api-Key': config.api_key
}
response = requests.get('https://api.fortnitetracker.com/v1/profile/pc/snipe_celly34', headers = headers)

print(response.text)
test = response.json()
print(test["stats"]["p2"])
