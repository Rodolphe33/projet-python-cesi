import requests
import json

response = requests.get("http://app.objco.com:8099/?account=16L1SPQZS3&limit=10")
print(response.status_code)
print(response.json)
dico = response.json()
#print(dico)
for i in range(0, 5):
    json_string = json.dumps(dico[i], sort_keys=True, indent=2)
    print(json_string)
