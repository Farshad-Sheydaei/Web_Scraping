import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'
source = requests.get(url).text

soup = BeautifulSoup(source, 'html.parser')

movie_name = soup.select('td.titleColumn a')

rating = soup.find_all('td', attrs={"class": "ratingColumn imdbRating"})

year = soup.find_all('span', attrs={'class': 'secondaryInfo'})
