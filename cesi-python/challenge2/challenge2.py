# Augmenter ce script d'un formatage JSON. (parser chaque groupe de
# données).

import requests
import json

response = requests.get("http://app.objco.com:8099/?account=16L1SPQZS3&limit=5")
print(response.status_code)
print(response.json)
dico = response.json()
#print(dico)
for i in range(0, len(dico)):
    json_string = json.dumps(dico[i], indent=1)
    print(json_string)
