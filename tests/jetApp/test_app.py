import pytest
import requests_mock
from jetApp.api_calls import get_restaurants_from_jet


def test_get_restaurants():
    with requests_mock.Mocker() as m:
        m.get('https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/TE1 1ST', json={
            "restaurants": [
                {
                    "name": "Test Restaurant",
                    "cuisines": [{"name": "Italian"}],
                    "rating": {"starRating": 4.5},
                    "address": {
                        "firstLine": "123 Test St",
                        "postalCode": "TE1 1ST",
                        "city": "Test City"
                    }
                }
            ]
        })

        result = get_restaurants_from_jet("TE1 1ST")
        assert result[0]['name'] == 'Test Restaurant'
