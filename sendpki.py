import requests
import json
import sys

"""Send PKI 0x1e368cd9
"""

def main():
	url = "http://localhost:8545"
	headers = {'content-type': 'application/json'}
	method = "eth_sendTransaction"
	
	print "Updating public key"
	
	payload = {
	    "method": method,
	    "params": [{"from":"0x000ab7f233e6b95e91c372f61ba6c3c18807f3d3", "to":"0xfcd34247ed83dc0cfd3b9e73cba2bfaaa8c366a7",
	    "gas":"0x30d40",
	"data":"0x1e368cd90000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000d4141414141414141414141414100000000000000000000000000000000000000"}],
	    "jsonrpc": "2.0",
	    "id": 1,
	}
	
	try:
		response = requests.post(url, data=json.dumps(payload), headers=headers).json()
	except requests.ConnectionError:
		response = "Unable to connect"
	print response
	print sys.getsizeof(url) + sys.getsizeof(headers) + sys.getsizeof(payload)
		
if __name__ == "__main__":
    main()
    
    
    
"""
000000000000000000000000000000000000000000000000000000000000000d
48656c6c6f2c20776f726c642100000000000000000000000000000000000000
"""
