from balance import getTokenBalance
from accounts import getChainAccounts
from utilities import prettyPrint, b64Encode, writeToFile


def getAddresses():
    response = getChainAccounts()
    # totalAccountsCount is all accounts in the chain
    totalAccountsCount, nextKey = response["pagination"].values()

    """Tinker with these values below to get more addresses, etc."""
    pageLimit, count = 2, 2

    addressesList = []
    while count > 0:
        if nextKey:
            pageKey = b64Encode(nextKey)
            response = getChainAccounts(pageKey, pageLimit)
            accounts, pagination = response["accounts"], response["pagination"]
            addresses = [account["address"] for account in accounts]
            addressesList.extend(addresses)
            nextKey = pagination["next_key"]
            count -= 1
    return addressesList


def main():
    addresses = getAddresses()
    balances = [getTokenBalance(address) for address in addresses]
    hashed = dict(zip(addresses, balances))
    writeToFile(hashed, fileType="json")
    return hashed


prettyPrint(main())
