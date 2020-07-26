import requests
import threading

class fetchdetail(threading.Thread):
    def run(self):
        print("News fetching started ")
        url="http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=e24a4958e15444c49a21fea59dfd7946"
        response =  requests.get(url)
        print(response.text)
        print("Fetch News Finished")


def main():
    print("App started")
    fref = fetchdetail()
    fref.start()
    for i in range(1,10):
        print("i is :",i)
    print("App Finished")

if __name__ == '__main__':
    main()