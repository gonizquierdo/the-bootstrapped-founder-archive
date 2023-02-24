import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
def parse_article(url):
    response = requests.get(url)
    
    # Extract title from url
    title = url.split('/')[-2]
    
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div containing the article content
    article_div = soup.find('div', {'class': 'entry-content'})

    # Extract the text of the article
    article_text = article_div.get_text()

    # Save the article text to a file with the title as the name and encoding as utf-8
    with open('out/' + title + '.txt', 'w', encoding='utf-8') as f:
        f.write(article_text)


