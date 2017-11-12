import requests
import json


def main():
	url = "http://localhost:8545"
	headers = {'content-type': 'application/json'}
	method = "eth_call"
	params = [{"to":"0xa58b477d13e2085e12c21f94c6fff908d691a368",
	"data":"0x84aabc90"}]
	payload = {
	    "method": method,
	    "params": [{"to":"0xa58b477d13e2085e12c21f94c6fff908d691a368",
	"data":"0x84aabc90"}, "latest"],
	    "jsonrpc": "2.0",
	    "id": 1,
	}
	
	
	response = requests.post(url, data=json.dumps(payload), headers=headers).json()
	print response
	
	print "Output of check ttl"
	
	payload = {
	    "method": method,
	    "params": [{"to":"0xa58b477d13e2085e12c21f94c6fff908d691a368",
	"data":"0x89097ac3"}, "latest"],
	    "jsonrpc": "2.0",
	    "id": 1,
	}
	print response
		
if __name__ == "__main__":
    main()
