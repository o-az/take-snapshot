import base64
import json
import csv
from constants import OUTPUT_FILE_TYPE


def prettyPrint(jsonObject):
    pretty = json.dumps(jsonObject, indent=2, default=str)
    return print(pretty)

def b64Encode(s):
    bStr = s.encode("ascii")
    return base64.b64encode(bStr)


"""
    data shape is:
    {
        "<address>" : <balance>,
        ...
    }
"""
def writeToFile(data, fileType=OUTPUT_FILE_TYPE):
    match fileType:
        case "json":
            with open("data.json", "w") as f:
                json.dump(data, f, indent=2)
        case "csv":
            fieldnames, delimiter = ["address", "balance"], ","
            with open("data.csv", "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames, delimiter, quoting=csv.QUOTE_ALL)
                writer.writeheader()
                for address, balance in data.items():
                    writer.writerow({"address": address, "balance": balance})