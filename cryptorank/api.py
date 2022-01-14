import requests

URL = "https://api.cryptorank.io/v1"


def get_currencies(API_KEY_CRYPTORANK, limit):
    params = {
        'api_key': API_KEY_CRYPTORANK,
        'limit': limit
    }
    response = requests.get(URL + '/currencies', params=params)

    return response
