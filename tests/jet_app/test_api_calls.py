import requests_mock
from jet_app import api_calls


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
                    },
                    "logoUrl": "https://www.example.com/logo.jpg"
                }
            ]
        })

        result = api_calls.get_restaurants_from_jet("TE1 1ST")
        assert result[0]['name'] == 'Test Restaurant'


def test_process_restaurants():
    restaurants = [
        {
            "name": "Test Restaurant",
            "cuisines": [{"name": "Italian"}],
            "rating": {"starRating": 4.5},
            "address": {
                "firstLine": "123 Test St",
                "postalCode": "TE1 1ST",
                "city": "Test City"
            },
            "logoUrl": "https://www.example.com/logo.jpg"
        }
    ]

    result = api_calls.process_restaurants(restaurants)
    assert result[0]['name'] == 'Test Restaurant'


def test_process_restaurants_empty_list():
    restaurants = []
    result = api_calls.process_restaurants(restaurants)
    assert result == []


def test_process_restaurants_multiple_restaurants():
    restaurants = [
        {
            "name": "Test Restaurant 1",
            "cuisines": [{"name": "Italian"}],
            "rating": {"starRating": 4.5},
            "address": {
                "firstLine": "123 Test St",
                "postalCode": "TE1 1ST",
                "city": "Test City"
            },
            "logoUrl": "https://www.example.com/logo.jpg"
        },
        {
            "name": "Test Restaurant 2",
            "cuisines": [{"name": "Chinese"}],
            "rating": {"starRating": 4.0},
            "address": {
                "firstLine": "456 Test Ave",
                "postalCode": "TE1 2ND",
                "city": "Test City"
            },
            "logoUrl": "https://www.example.com/logo.jpg"
        }
    ]

    result = api_calls.process_restaurants(restaurants)
    assert len(result) == 2
    assert result[0]['name'] == 'Test Restaurant 1'
    assert result[1]['name'] == 'Test Restaurant 2'


def test_process_restaurants_no_cuisines():
    restaurants = [
        {
            "name": "Test Restaurant",
            "cuisines": [],
            "rating": {"starRating": 4.5},
            "address": {
                "firstLine": "123 Test St",
                "postalCode": "TE1 1ST",
                "city": "Test City"
            },
            "logoUrl": "https://www.example.com/logo.jpg"
        }
    ]

    result = api_calls.process_restaurants(restaurants)
    assert result[0]['cuisines'] == ''


def test_process_restaurants_multiple_cuisines():
    restaurants = [
        {
            "name": "Test Restaurant",
            "cuisines": [{"name": "Italian"}, {"name": "Chinese"}],
            "rating": {"starRating": 4.5},
            "address": {
                "firstLine": "123 Test St",
                "postalCode": "TE1 1ST",
                "city": "Test City"
            },
            "logoUrl": "https://www.example.com/logo.jpg"
        }
    ]

    result = api_calls.process_restaurants(restaurants)
    assert result[0]['cuisines'] == 'Italian, Chinese'
