import requests

response = requests.get("http://app.objco.com:8099/?account=16L1SPQZS3&limit=5")
print(response.status_code)
# print(response.json())
dico = response.json()
for i in range(0, len(dico)):
    print(str(dico[i]))
