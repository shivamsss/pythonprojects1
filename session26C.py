import matplotlib.pyplot as plt
import requests
import json

url="https://api.covid19india.org/data.json"
response=requests.get(url)

data=json.loads(response.text)
#print(data)

statedata=data['statewise']
# print(statedata)
statewise_data=[]
for case in statedata:
    statewise_data.append(int(case['confirmed']))
print(statewise_data)
plt.bar(1,statewise_data)
plt.show()
