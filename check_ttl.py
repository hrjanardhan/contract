import requests
import json
import sys
"""Send PKI 0x1e368cd9
"""

def main():
	url = "http://localhost:8590"
	headers = {'content-type': 'application/json'}
	method = "eth_sendTransaction"
	
	print "Decrementing TTL"
	
	payload = {
	    "method": method,
	    "params": [{"from":"0x4c8550f577da8c3a4e3916b545947fcd6cb04c14", "to":"0x975fe870924f9f59eb61bf8ad5cf2a058f014c46",
	    "gas":"0x30d40",
	"data":"0x89097ac3"}],
	    "jsonrpc": "2.0",
	    "id": 1,
	}
	
	try:
		response = requests.post(url, data=json.dumps(payload), headers=headers).json()
	except requests.ConnectionError:
		response = "Unable to connect"
	print response
	"""print sys.getsizeof(url) + sys.getsizeof(headers) + sys.getsizeof(payload)"""
		
if __name__ == "__main__":
    main()
