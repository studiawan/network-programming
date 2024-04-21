from html.parser import HTMLParser
from urllib.request import urlopen
import gzip
from io import BytesIO

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_h2_tag = False

    def handle_starttag(self, tag, attrs):
        if tag == 'h2':
            self.in_h2_tag = True

    def handle_endtag(self, tag):
        if tag == 'h2':
            self.in_h2_tag = False

    def handle_data(self, data):
        if self.in_h2_tag:
            print("Section Title:", data)

def get_url_content(url):
    response = urlopen(url)
    if response.info().get('Content-Encoding') == 'gzip':
        buf = BytesIO(response.read())
        f = gzip.GzipFile(fileobj=buf)
        content = f.read()
    else:
        content = response.read()
    return content

parser = MyHTMLParser()
url = 'http://www.python.org'
content = get_url_content(url)
parser.feed(content.decode('utf-8'))
