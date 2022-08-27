import requests

page_number = 1
url = 'https://www.imdb.com/chart/top/'
source = requests.get(url)

print(source)