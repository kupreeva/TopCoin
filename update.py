import json
import requests

def mn_count(self):
    url = "http://1:2@127.0.0.1:17196"
    headers = {'content-type': 'text/plain'}
    payload = {
        "method": "masternode",
        "params": ["count"],
        "jsonrpc": "1.0",
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    return response['result']