from bs4 import BeautifulSoup
import requests
import random

response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')

def get_random_quote() -> str:
    return random.choice(quotes).text



