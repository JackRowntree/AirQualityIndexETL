import requests
from bs4 import BeautifulSoup
from helpers import parse_cells

URL = 'https://uk-air.defra.gov.uk/air-pollution/daqi'
REQ = requests.get(URL, headers)
SOUP = BeautifulSoup(req.content, 'html.parser')

def check():
	"""
	Does scraping
	"""
	pass

def scrape():
	"""
	Does scraping
	"""
	cells = SOUP.find('tbody').find_all('td')
	out = parse_cells(cells)
	pass

def load():
	"""
	Does scraping
	"""
	pass

if __name__ == "__main__":
	scrape()