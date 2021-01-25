import requests
from bs4 import BeautifulSoup
from ruamel.yaml.util import RegExp
import re
import config_tools
from requests.api import head
from bs4 import BeautifulSoup

LETTERBOXURL = 'https://letterboxd.com'

url = 'https://letterboxd.com/film/portrait-of-a-lady-on-fire/'
list_url = 'https://letterboxd.com/ericx13/list/letterboxd-top-250-french-language-films'

def letterboxd_get_ids(plex, letterboxd_url: str):
    list_regex = r"https:\/\/letterboxd.com\/.*\/list\/.*"
    if re.match(list_regex, letterboxd_url):
        print("is valid list")
        req = requests.get(letterboxd_url)
        soup = BeautifulSoup(req.content)
        
    else:
        print('Not a valid letterboxd list')

def letterboxd_get_movies(config_path, plex, plex_map, value):
    matched = []
    missing = []
    for tmdb_id in 
    

def get_movie_ids(movie_url):
    soup = BeautifulSoup(requests.get(movie_url).content, 'lxml')
    return {'imdb': get_movie_imdb(soup), 'tmdb': get_movie_tmdb(soup)}

def get_movie_tmdb(soup: BeautifulSoup):
    tmdb_url = soup.find(attrs={'data-track-action': 'TMDb'}).get('href')
    return re.match('.*\/movie\/(\d*)/', tmdb_url).group(1)

def get_movie_imdb(soup: BeautifulSoup):
    imdb_url = soup.find(attrs={'data-track-action': 'IMDb'}).get('href')
    return re.match('.*\/(tt\d*)\/', imdb_url).group(1)

def get_list_pages(list_url):
    pages = []
    req = requests.get(list_url)
    list_soup = BeautifulSoup(req.content, 'lxml')
    pagination = list_soup.find('div', class_='paginate-pages')
    if pagination is not None:
        for page in pagination.findAll('li'):
            pages.append(list_url + "/page/" + page.text)
    else:
        pages.append(list_url)
    return pages

def get_list_movies(list_url):
    movies_ids = []
    for page_url in get_list_pages(list_url):
        req = requests.get(page_url)
        page_soup = BeautifulSoup(req.content, 'lxml')
        for movie in page_soup.find('ul', class_='poster-list').findAll('div', class_="poster"):
            movies_ids.append(get_movie_ids(LETTERBOXURL + movie['data-film-slug']))
    return movies_ids
    
url1 = "https://letterboxd.com/ericx13/list/watchlist-tilda-swinton/"
#get_list_movies('https://letterboxd.com/ericx13/list/letterboxd-top-250-french-language-films')
for x in get_list_movies(url1):
    print(x['imdb'])
    print(x['tmdb'])

#print(get_list_movies(url1))