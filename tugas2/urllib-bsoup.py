# get short tutorial here: http://www.pythonforbeginners.com/python-on-the-web/beautifulsoup-4-python/
from urllib.request import urlopen
from bs4 import BeautifulSoup

# response = urlopen('http://www.python.org').read()
response = urlopen('https://classroom.its.ac.id').read()

soup = BeautifulSoup(response, "lxml")

# print(soup.title.string)
# print(soup.get_text())

# masih ada newline yg tdk sesuai output
# print(soup.body.nav.ul.get_text().split("\n\n\n\n")[1])
# print(soup.body.nav.ul.get_text().split("\n\n\n\n")[2])

# sudah sesuai output
# print(soup.body.nav.ul.get_text().splitlines()[4].replace("        ", ""))
daftar_menu = soup.body.nav.ul.get_text().splitlines()
print(daftar_menu[4].strip())
print("   ", daftar_menu[7])
print("   ", daftar_menu[8])
# print(daftar_menu[12].replace("        ", ""))
print(daftar_menu[12].strip())
print("   ", daftar_menu[15])
# print("\t", daftar_menu[15])
# print(daftar_menu)

# daftar_menu = soup.body.nav.ul.get_text().split()
# print(daftar_menu)
# print(daftar_menu[:2][0], daftar_menu[:2][1])

# daftar_menu = soup.body.nav.ul.get_text().strip().splitlines()
# print(daftar_menu)

# print(daftar_menu[4])
# print(daftar_menu[7])
# print(daftar_menu[8])
# print(daftar_menu[12])
# print(daftar_menu[15])