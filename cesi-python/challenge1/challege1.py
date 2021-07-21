import requests

response = requests.get("http://app.objco.com:8099/?account=16L1SPQZS3&limit=10")
print(response.status_code)
# print(response.json())
dico = response.json()
for i in range(0, 5):
    print(str(dico[i]))
