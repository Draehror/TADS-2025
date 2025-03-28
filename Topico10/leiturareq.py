# import requests

# PARAMS = {'bibkeys':'ISBN:1718500521', 'format':'json'}

# requests.get('http://openlibrary.org/api/books', params = PARAMS)

# import urllib3

# http = urllib3.PoolManager()

# r = http.request('GET', 'http://127.0.0.1:5500/texto.txt')

# for i, line in enumerate(r.data.decode('utf-8').split('\n')):
#     if line.strip():
#         print("Line %i:" %i, line.strip())

# import json
# import urllib3

# http = urllib3.PoolManager()

# r = http.request('GET', 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=80c6a04f3982422583a8c2cbb01461b0')

# articles = json.loads(r.data.decode('utf-8'))
# for article in articles['articles']:
#     print(article['title'])
#     print(article['publishedAt'])
#     print(article['url'])
#     print()
    
import json
import requests

params = {'q':'Bitcoin',
          'apiKey':'80c6a04f3982422583a8c2cbb01461b0'
          }

r = requests.get('https://newsapi.org/v2/everything', params=params)

articles = json.loads(r.text)

for article in articles['articles']:
    print(article['title'])
    print(article['publishedAt'])
    print(article['url'])
    print()