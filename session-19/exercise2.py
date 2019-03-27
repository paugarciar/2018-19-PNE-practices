import http.client
import json

# -- API information
HOSTNAME = "www.metaweather.com"

# Choosing a capital
capital = input("Please enter a capital: ")

ENDPOINT1 = "/api/location/search/?query=" + capital


METHOD = "GET"


def city_weather(endpoint):

    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection(HOSTNAME)

    conn.request(METHOD, endpoint, None, headers)

    r1 = conn.getresponse()

    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)

    text_json = r1.read().decode("utf-8")
    conn.close()

    result = json.loads(text_json)
    return result


try:
    # --Calculating the woeid number of the city
    woeid_number = city_weather(ENDPOINT1)
    LOCATION_WOEID = str(woeid_number[0]['woeid'])

    # --Calculating the weather characteristics
    ENDPOINT2 = "/api/location/" + LOCATION_WOEID + "/"
    weather = city_weather(ENDPOINT2)

    temp0 = weather['consolidated_weather'][0]

    print()
    print("In {}".format(weather['title']))
    print("The current time is: {}".format(weather['time']))
    print("The sunset is at: {}".format(weather['sun_set']))
    print("And the current temp is: {} degrees".format(temp0['the_temp']))

except IndexError:
    print("Capital not valid")

