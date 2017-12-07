import requests
import json
import sys
"""Send PKI 0x1e368cd9
"""

def main():
	url = "http://localhost:8545"
	headers = {'content-type': 'application/json'}
	method = "eth_call"

	payload = {
	    "method": "eth_call",
	    "params": [{"to":"0x975fe870924f9f59eb61bf8ad5cf2a058f014c46",
	    "gas":"0x30d40",
	"data":"0x98faf31b000000000000000000000000000ab7f233e6b95e91c372f61ba6c3c18807f3d3"}, "latest"],
	    "jsonrpc": "2.0",
	    "id": 1,
	}
	
	try:
		response = requests.post(url, data=json.dumps(payload), headers=headers).json()
	except requests.ConnectionError:
		response = "Unable to connect"
	print response
	print sys.getsizeof(response)
		
if __name__ == "__main__":
    main()
