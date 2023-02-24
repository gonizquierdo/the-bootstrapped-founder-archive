from bs4 import BeautifulSoup
import requests
from parse_article import parse_article

# URL to scrape
url = 'https://thebootstrappedfounder.com/archive/'

# Get the HTML
r = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(r.text, 'html.parser')

# Get the links where the class contains 'post-'
links = soup.find_all('a', class_='sya_postlink')

# Print the links
for link in links:
    # Get the link
    href = link.get('href')
    # Print the link
    parse_article(href)
