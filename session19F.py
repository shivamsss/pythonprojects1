import requests
import json


apikey ="e24a4958e15444c49a21fea59dfd7946"
url = "http://newsapi.org/v2/everything?q=bitcoin&from=2020-06-11&sortBy=publishedAt&apiKey=API_KEY".format(apikey)
response = requests.get(url)
print(response.text)
news_data = json.loads(response.text)
print(news_data)