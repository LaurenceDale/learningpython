

import requests
import json
from requests.auth import HTTPBasicAuth
import time
import os

# Authenticate and get session JWT
print("Fetching Session Token...")
time.sleep(2)

auth=requests.post(
   'https://api-uat.atradius.com/authenticate/v1/tokens',
    auth=HTTPBasicAuth('167c959ccf254cee966cd0c62528c036','26353dc6-d9a5-4794-80cb-be1d10398891'),
    headers= {
        'Atradius-App-Key': '86ab4a4e-40a0-43a3-be78-c5d0cab2a301',
        'Tag': 'ITSTest',
    })

print(auth.text)
print("\nToken Extracted")

parsed = json.loads(auth.text)
token = parsed["data"]["accessToken"]

print(token)
time.sleep(2)
print("\nFetching Policies")
time.sleep(2)
# Sample request to get policies

sampleReq = requests.get(
    'https://api-uat.atradius.com/creditinsurance/policymanagement/v1/policies?customerId=20302876',
    headers= {
        'Atradius-App-Key': '86ab4a4e-40a0-43a3-be78-c5d0cab2a301',
        'Tag': 'ITSTest',
        'Authorization': 'Bearer ' + token
    })

print(sampleReq.text)
