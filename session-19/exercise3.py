import http.client
import json

# -- API information
HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = "Obijuan"
METHOD = "GET"

# -- Real name
headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)
r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()
user1 = json.loads(text_json)

print("Real name: ", user1["name"])


# -- List of repositories
headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT + GITHUB_ID + "/repos", None, headers)
r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()

user2 = json.loads(text_json)

print("List of repos: ")
for repo in user2:
    print("  "+repo["name"])

# --Number of commits
ENDPOINT = "/repos/"
headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT + GITHUB_ID + "/2018-19-PNE-practices/contributors", None, headers)
r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()

user3 = json.loads(text_json)

print("Number of commits to the 2018-19-PNE-practices: ", user3[0]["contributions"])