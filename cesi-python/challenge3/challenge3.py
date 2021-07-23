import requests
import json
import sql

response = requests.get("http://app.objco.com:8099/?account=16L1SPQZS3&limit=5")
dico = response.json()
for i in range(0, len(dico)):
    json_string = json.dumps(dico[i][0], indent=1)
    print("2=> ", json_string)
