# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import termcolor
import json

PORT = 8001
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/listusers")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

print("CONTENT: ")

# -- Print the received data
print(data1)

# -- Create a variable with the data,
# -- form the JSON received
members = json.loads(data1)

print("CONTENT: ")

# Print the information in the object

print()

for people in members:
    termcolor.cprint("Name: ", 'green', end='')
    print(people['Firstname'], people['Lastname'])
    termcolor.cprint("Age: ", 'green', end='')
    print(people['age'])
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(people['phoneNumber']))
    for i, num in enumerate(people['phoneNumber']):
        termcolor.cprint("Phone {}: \n".format(i), 'blue', end='')

        termcolor.cprint("     Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("     Number: ", 'red', end='')
        print(num['number'])
    print()
