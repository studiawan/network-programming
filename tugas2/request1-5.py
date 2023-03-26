import requests
from bs4 import BeautifulSoup

class MyHTMLParser:
    def __init__(self, url):
        self.url = url
        self.response = None
        self.html_content = None
        self.soup = None

    def get(self):
        self.response = requests.get(self.url)
        self.html_content = self.response.content
        self.soup = BeautifulSoup(self.html_content, 'html.parser')

    def response_header_status_code(self):
        return self.response.status_code
    
    def response_header_description(self):
        return self.response.reason
    
    def response_header_content_encoding(self):
        return self.response.headers.get("Content-Encoding")
    
    def response_header_http_version(self):
        return self.response.raw.version
    
    def response_header_content_type_charset(self):
        contenttype = self.response.headers.get("Content-Type")
        if contenttype:
            charset_start = contenttype.find("charset=")
            if charset_start != -1:
                charset = contenttype[charset_start + 8:]
                return charset
            else:
                return None
        else: return None
    
    def daftar_menu(self):
        menu_ul = self.soup.find('ul', {'class':'navbar-nav h-100 wdm-custom-menus links'})
        result = []
        try:
            menu_li = menu_ul.find_all('li')
            for li in menu_li:
                a = li.find('a')
                if a:
                    result.append(a.text.strip())
                div = li.find('div')
                a_content = div.find_all('a')
                for content in a_content:
                    result.append('     ' + content.text.strip())
        
        except AttributeError:
            pass
        return result


if __name__ == "__main__":
    parser = MyHTMLParser('https://classroom.its.ac.id/')
    parser.get()
    print("Status Code and Description:", parser.response_header_status_code(), parser.response_header_description())
    print("Content-Encoding:", parser.response_header_content_encoding())
    print("HTTP Version:", parser.response_header_http_version())
    print("Charset:", parser.response_header_content_type_charset())
    # print("Menu:", parser.daftar_menu())
    for menu in parser.daftar_menu():
        print(menu)
