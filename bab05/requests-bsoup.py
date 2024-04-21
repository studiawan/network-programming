import requests
from bs4 import BeautifulSoup

def fetch_and_parse_url(url):
    # Fetch the content of the URL
    response = requests.get(url)
    # Parse the content with BeautifulSoup using the HTML parser
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def print_links(soup):
    # Find all 'a' tags, which define hyperlinks
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')  # Get the href attribute of the link
        text = link.text.strip()  # Get the text enclosed in the <a> tag
        print(f"URL: {href}, Text: {text}")

# URL to be parsed
url = 'http://www.python.org'
# Fetch and parse the URL
soup = fetch_and_parse_url(url)
# Print all links found in the HTML
print_links(soup)
