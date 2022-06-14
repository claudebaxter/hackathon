from algosdk import algod, transaction, account, mnemonic
from algosdk.v2client import algod

import os
import base64
from algosdk.future.transaction import *

appID = 95223182
actual = logic.get_application_address(appID)

print(actual)
