import urllib2
import json

locu_api = '9fb8cd70cb34cab8e83690473133f51943b5c93f'

url = 'http://api.locu.com/v1_0/venue/search/?locality=New+York&category=restaurant&api_key=9fb8cd70cb34cab8e83690473133f51943b5c93f'

json_obj = urllib2.urlopen(url)

data = json.load(json_obj)

restaurants = []

def locu_search(query):
    api_key = locu_api
    url = 'http://api.locu.com/v1_0/venue/search/?api_key=' + api_key
    locality = query.replace(' ', '%20')
    final_url = url + '&locality=' + locality + '&category=restaurant'
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)

    for item in data['objects']:
       restaurants.append(item['name'])

    return restaurants

print locu_search("New York")
    
