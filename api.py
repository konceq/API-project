import urllib2
import json

tracks_api = "5f23a4113ba32c15f16e22cdceb0d0ca9073d462" #.
locu_api = '9fb8cd70cb34cab8e83690473133f51943b5c93f'

def locu_search(query):
    restaurants = []
    api_key = locu_api
    #http://api.locu.com/v1_0/venue/search/?api_key=9fb8cd70cb34cab8e83690473133f51943b5c93f&locality=New%20York&category=restaurant
    url = 'http://api.locu.com/v1_0/venue/search/?api_key=' + api_key
    locality = query.replace(' ', '%20')
    final_url = url + '&locality=' + locality + '&category=restaurant'
    print(final_url)
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)

    for item in data['objects']:
       restaurants.append(item['name'])

    return restaurants


def createJSON(url):
    request = urllib2.urlopen(url+"&api_key=5f23a4113ba32c15f16e22cdceb0d0ca9073d462f")
    resultstring = request.read()
    return json.loads(resultstring)
    
def tracks_search(query):
    url='http://8tracks.com/mix_sets/tags:'+ query +'.json?include=mixes'
    print url+"&api_key=5f23a4113ba32c15f16e22cdceb0d0ca9073d462f"
    results = createJSON(url)
    if "mixes" in results:
        if len(results["mixes"]) > 0:
            return_list = []
            return_list.append(results["mixes"][0]["id"])
            return_list.append(results["mixes"][0]["name"])
            return_list.append(results["mixes"][0]["user"]["login"])
            return return_list
    return None

#print tracks_search('Jazz')

