import http.client
import json

# -- API information
HOSTNAME = "rest.ensembl.org"
ENDPOINT = "/sequence/id/ENSG00000165879?content-type=application/json"

METHOD = "GET"

headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers

conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

result = json.loads(text_json)
print(result)
