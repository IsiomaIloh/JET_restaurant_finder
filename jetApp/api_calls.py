import requests


def get_restaurants_from_jet(postcode):
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.3",
        "Accept": "application/json",
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        restaurants = response.json()["restaurants"][:10]  # Gets the first 10 restaurants encountered

        # Checks if no restaurants found
        if not restaurants:
            return {"status": "No restaurants found"}

        return process_restaurants(restaurants)

    # Returns status code and message if the API call was unsuccessful or no data was found
    return {"status": response.reason, "code": response.status_code}


def process_restaurants(restaurants):
    processed_data = []
    # Iterates through the list of restaurants and processes the data
    for restaurant in restaurants:
        # Appends the processed data to the list
        processed_data.append({
            # builds a dictionary with the processed data
            "name": restaurant["name"],
            "cuisines": ", ".join([cuisine["name"] for cuisine in restaurant.get("cuisines", [])]),
            "rating": restaurant["rating"]["starRating"],
            "address": ", ".join([
                restaurant["address"]["firstLine"],
                restaurant["address"]["postalCode"],
                restaurant["address"]["city"]
            ]),
            "image": restaurant["logoUrl"] if restaurant["logoUrl"] else ""
        })
    return processed_data
