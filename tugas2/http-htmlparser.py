from html.parser import HTMLParser
from urllib.request import urlopen


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


parser = MyHTMLParser()
response = urlopen('http://classroom.its.ac.id').read()
parser.feed(response.decode('utf-8'))
