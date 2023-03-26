#!/usr/bin/env python

import http.client

# cuma bisa url, gabisa uri, gabisa pake urn, langsung nama host
# connection = http.client.HTTPSConnection("www.en.wikipedia.org/wiki/List_of_HTTP_header_fields")
connection = http.client.HTTPSConnection("classroom.its.ac.id")

connection.request("GET", "/")
response = connection.getresponse()
header = response.getheaders()

# print("Status:", response.status, response.reason, response.getheader("Content-Type").split()[0])      #200 OK, 301 Moved Permanently

print("Status:", response.status, response.reason, response.getheader("Content-Type").partition("=")[2])      #200 OK, 301 Moved Permanently
print("Response header:")
for item in header:
    print(item)

# print("Content:", response.read())
