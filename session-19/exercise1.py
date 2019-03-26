# Program to obtain information of jokes about Chuck Norris

import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT1 = "/jokes/count"  # For counting the number of jokes
ENDPOINT2 = "/categories"   # Obtaining the names of the categories
ENDPOINT3 = "/jokes/random?firstName=Chuck&amp;lastName=Norris1http:/"  # Random joke
ENDPOINTS = [ENDPOINT1, ENDPOINT2, ENDPOINT3]
METHOD = "GET"
result = []

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
for element in ENDPOINTS:
    conn.request(METHOD, element, None, headers)

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

    # -- Optionally you can print the
    # -- received json file for testing
    # print(text_json)

    # -- Generate the object from the json file
    result.append(json.loads(text_json))

# Number of categories
result.append(len(result[1]["value"]))

# Printing the information
print("\nNumber of jokes about Chuck Norris: ", result[0]["value"])
print("List of categories: ", result[1]["value"])
print("Number of categories: ", result[3])
print("Random joke: ", result[2]["value"]["joke"])
