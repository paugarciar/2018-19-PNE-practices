import http.client
import json

# -- API information
HOSTNAME = "www.metaweather.com"
ENDPOINT1 = "/api/location/"

# Choosing a capital
capital = input("Please enter a capital: ")

ENDPOINT2 = "/api/location/search/?query="+ capital





METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT2 + '/', None, headers)

r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

text_json = r1.read().decode("utf-8")
conn.close()

weather = json.loads(text_json)

# -- Get the data
print(weather)