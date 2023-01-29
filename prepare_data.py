import re

import requests
from bs4 import BeautifulSoup


url = 'http://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="html.parser")



def create_quotes():
    tags = soup.find_all(name='div', attrs='tags')
    authors = soup.find_all(name='small', attrs='author')
    quotes = soup.find_all(name='span', attrs='text')
    quotes_list = []
    for i in range(0, len(quotes)):
        tag_for_one = tags[i].find_all(name='a', attrs='tag')
        res = {
            'tags': [x.text for x in tag_for_one],
            'author': authors[i].text,
            'quote': quotes[i].text
        }
        quotes_list.append(res)
    return quotes_list


def create_authors():
    authors = soup.find_all('a', href=re.compile('author'))
    list_authors = []
    for i in authors:
        href = i.get('href')
        new_url = url+href
        resp = requests.get(new_url)
        sooup = BeautifulSoup(resp.text, features="html.parser")
        fullname = sooup.find_all(name='h3', attrs='author-title')
        born_date = sooup.find_all(name='span', attrs='author-born-date')
        born_location = sooup.find_all(name='span', attrs='author-born-location')
        description = sooup.find_all(name='div', attrs='author-description')
        res = {
            'fullname': fullname[0].text.split('\n')[0],
            'born_date': born_date[0].text,
            "born_location": born_location[0].text,
            'description': description[0].text
        }
        list_authors.append(res)
    return list_authors







