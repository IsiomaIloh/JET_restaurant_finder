import requests
def get_restaurants_postcode(postcode):
#using a python function to fetch the postcode from JET API
    url = f'https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/EC4M7RF'
    response = requests.get(url)
    return response.json()