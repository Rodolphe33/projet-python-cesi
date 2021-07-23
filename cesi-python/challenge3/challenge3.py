import requests
import json

response = requests.get("http://app.objco.com:8099/?account=16L1SPQZS3&limit=5")
# print(response.status_code)
# print(response.json)
dico = response.json()
# print("1=> ", dico[0])
for i in range(0, len(dico)):
    json_string = json.dumps(dico[i][0], indent=1)
    print("2=> ", json_string)
    newList = int(dico[i][0]) + ": " + str(dico[i][1])
    print(newList)