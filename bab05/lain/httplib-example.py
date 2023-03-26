#!/usr/bin/env python

import http.client

connection = http.client.HTTPSConnection("www.its.ac.id")
connection.request("GET", "/")
response = connection.getresponse()
header = response.getheaders()

print("Status:", response.status, response.reason)
print("Response header:")
for item in header:
    print(item)

# print("Content:", response.read())
