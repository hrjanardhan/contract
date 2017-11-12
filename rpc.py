import requests
import json


def main():
    url = "http://localhost:8545"
    headers = {'content-type': 'application/json'}

    # Example echo method
    while(1):
		method = raw_input("method: ")
		params = raw_input("params: ")
		params = params.replace(' ', '').split(",")
		
		payload = {
		    "method": method,
		    "params": params,
		    "jsonrpc": "2.0",
		    "id": 1,
		}
		response = requests.post(
		    url, data=json.dumps(payload), headers=headers).json()

	
		print response
		
if __name__ == "__main__":
    main()
