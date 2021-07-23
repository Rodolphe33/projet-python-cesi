import requests

response = requests.get("http://135.125.100.41:8099/?account=ERIC&limit=2")

#print(response.status_code)
print(response.text)
print("Chaine JSON brute " + str(response.json()))
dico = response.json()
for i in range(0, len(dico)):
    print("trame de data de la ligne " + str(i) + " " + str(dico[i][1]))