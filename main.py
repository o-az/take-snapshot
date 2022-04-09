from balance import getTokenBalance
from accounts import getChainAccounts
from utilities import b64Encode, writeToFile, prettyPrint


def getAddresses():
    response = getChainAccounts()
    # totalAccountsCount is all accounts in the chain
    nextKey, totalAccountsCount = response["pagination"].values()
    print(f"Total accounts count: {totalAccountsCount}")
    """Tinker with these values below to get more addresses, etc."""
    pageLimit, count = 6, 6
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


filterZeros = lambda item: item[1] != "0" and item[1] != 0


def main():
    addresses = getAddresses()
    balances = [getTokenBalance(address) for address in addresses]
    yeet = zip(addresses, balances)
    pairs = dict(filter(filterZeros, yeet))
    writeToFile(pairs)
    return pairs


# uncomment me
prettyPrint(main())
