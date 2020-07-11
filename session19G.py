import requests
import json

url = "https://api.covid19india.org/data.json"
response = requests.get(url)
#print(response.text)

covid_data = json.loads(response.text)
print(covid_data)
print("+++++++++++++++++++++++++++++++++++")

#print(covid_data['statewise'])

for i in range(0,len(covid_data['statewise'])):
    print(covid_data["statewise"][i]["state"])
    print(covid_data["statewise"][i]["active"])
    print(covid_data["statewise"][i]["confirmed"])
    print(covid_data["statewise"][i]["deaths"])
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print()