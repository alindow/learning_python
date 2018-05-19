import requests
import collections

search = 'capital'
key="ef26d57b"

url = 'http://www.omdbapi.com/?apikey={}&t={}'.format(key,search)

resp = requests.get(url)

movie_data = resp.json()

print(type(movie_data), movie_data)