
import requests

from bs4 import BeautifulSoup
url="https://www.imdb.com/india/top-rated-indian-movies/"
response=requests.get(url)
#print(response.text)
soup=BeautifulSoup(response.text,"html.parser")
movie_nametag=soup.find_all("td",classmethod="titleColumn")

for tags in movie_nametag:
    print(tags.text)

