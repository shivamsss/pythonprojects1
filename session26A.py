import matplotlib.pyplot as plt
import json
import requests

url = "https://api.covid19india.org/data.json"
response = requests.get(url)

covid_data=json.loads(response.text)
print(covid_data)
covidday_data = covid_data['cases_time_series']
#print(covidday_data)
total_confirmed=[]
for i in covidday_data:
    total_confirmed.append(int(i['totalconfirmed']))
#print(total_confirmed)
print("PLotting started")
plt.plot(total_confirmed)
plt.show()