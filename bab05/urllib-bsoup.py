# get short tutorial here: http://www.pythonforbeginners.com/python-on-the-web/beautifulsoup-4-python/
from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('http://www.python.org').read()
# response = urlopen('http://localhost:8080').read()

soup = BeautifulSoup(response, features="lxml")

print(soup.title.string)
print(soup.get_text())
