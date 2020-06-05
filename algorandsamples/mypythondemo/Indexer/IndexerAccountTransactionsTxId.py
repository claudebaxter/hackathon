import json
# requires Python SDK version 1.3 or higher
from algosdk.v2client import indexer

data = {
    "indexer_token": "",
    "indexer_address": "http://localhost:8980"
}

# instantiate indexer client
myindexer = indexer.IndexerClient(**data)
# gets tranactins for an account after a timestamp


# min/max rounds
data = {
    "address": "XIU7HGGAJ3QOTATPDSIIHPFVKMICXKHMOR2FJKHTVLII4FAOA3CYZQDLG4",
    "txid": "QZS3B2XBBS47S6X5CZGKKC2FC7HRP5VJ4UNS7LPGHP24DUECHAAA"
    }
response = myindexer.search_transactions_by_address(**data)
print("txid: QZS3B2XBBS47S6X5CZGKKC2FC7HRP5VJ4UNS7LPGHP24DUECHAAA = " +
      json.dumps(response, indent=2, sort_keys=True))
