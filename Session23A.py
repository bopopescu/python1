# import requests as rq

import requests

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=API_KEY"
response = requests.get(url)
print(response, type(response))
print("~~~~~~~~~~~~~~~~~~~~~")
jsonData = response.text
print(jsonData)
print("~~~~~~~~~~~~~~~~~~~~~")


newsDictionary = json.loads(jsonData)
print(newsDictionary)
print(type(newsDictionary))

print("~~~~~~~~~~~~~~~~~~~~~")

print(">> TOTAL NEWS:", newsDictionary["totalResults"])

articles = newsDictionary["articles"]
print(len(articles))

print("~~~~~~~~~~~~~~~~~~~~~")

for article in articles:
    print("~~~~~~~~~~~~~~~~~~~~~")
    print(article["author"])
    print(article["title"])
    print(article["description"])
    print("~~~~~~~~~~~~~~~~~~~~~")
    print()

