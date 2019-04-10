import http.client
import json

# -- API information
HOSTNAME = "http://www.ensembl.org"

#MY NOTES:
# /index.html->MAIN PAGE
#/Multi/Search/Results?q=FRAT1;site=ensembl->DIF. OPTIONS WHEN YOU SEARCH SOMETHING
#/Homo_sapiens/Gene/Summary?db=core;g=ENSG00000165879;r=10:97319267-97321915->FRAT1 WEBPAGE
# FORGET

# in api rest
#GET info/genomes/:genome_name 	Find information about a given genome


# Choosing a capital
capital = input("Please enter a capital: ")

ENDPOINT1 = "/api/location/search/?query=" + capital


METHOD = "GET"


def city_weather(endpoint):

    headers = {'User-Agent': 'http-client'}
    conn = http.client.HTTPSConnection(HOSTNAME)

    conn.request(METHOD, endpoint, None, headers)

    r1 = conn.getresponse()

    text_json = r1.read().decode("utf-8")
    conn.close()

    result = json.loads(text_json)
    return result


try:
    # --Calculating the woeid number of the citysession-19/exercise2.py:25
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
