import requests
from constants import BASE_URL, NATIVE_TOKEN


def getAccountBalance(address):
    url = f"{BASE_URL}/cosmos/bank/v1beta1/balances/{address}"
    response = requests.get(url)
    jsonify = response.json()
    if response.status_code != 200:
        print(f"Error: {jsonify['message']}")
        raise Exception(jsonify)
    return jsonify


"""
CHAIN      | NATIVE TOKEN
Terra      | uluna, uusd
Cosmos Hub | uatom
Osmosis    | uosmo
"""


def getTokenBalance(address):
    balances, _ = getAccountBalance(address).values()
    if len(balances) == 0:
        return "0"
    isToken = lambda v: v["denom"] == NATIVE_TOKEN
    token = next(filter(isToken, balances), None)
    if token:
        return token["amount"]
    return "0"
