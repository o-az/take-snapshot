import requests
from constants import BASE_URL


def getChainAccounts(pageKey=None, pageLimit=None):
    url = f"{BASE_URL}/cosmos/auth/v1beta1/accounts"
    params = {"pagination.key": pageKey, "pagination.limit": pageLimit}
    response = requests.get(url, params)
    jsonify = response.json()
    if response.status_code != 200:
        print(f"Error: {jsonify['message']}")
        raise Exception(jsonify)
    return jsonify
