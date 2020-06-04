import json
# requires version 1.3 or higher of the Python SDK
from algosdk.v2client import indexer

data = {
    "indexer_token": "",
    "indexer_address": "http://localhost:8980"
}

# instanciate indexer client
myindexer = indexer.IndexerClient(**data)

# this sample will loop thru all transactions in the search result
# using next_page to paginate

nexttoken = ""
numtx = 1
responseall = ""
# loop until there are no more tranactions in the response
# for the limit (max is 1000  per request)

while (numtx > 0):
    data = {
        "min_amount": 100000000000000,
        "limit": 10,
        "next_page": nexttoken
    }
    response = myindexer.search_transactions(**data)
    transactions = response['transactions']
    numtx = len(transactions)
    if (numtx > 0):
        nexttoken = response['next-token']
        # concatinate response
        responseall = responseall + json.dumps(response)
        
# Pretty Printing JSON string 
print(json.dumps(responseall, indent=4, sort_keys=True))

