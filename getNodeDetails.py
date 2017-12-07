import requests
import json
import binascii

def getCoinbase():
	# URL of the endpoint to connect to the blockchain
	url = "http://localhost:8590"
	headers = {'content-type': 'application/json'}
	
	# Get coinbase(address) of the device on the blockchain
	payload = {
	    "method": "eth_coinbase",
	    "params": [],
	    "jsonrpc": "2.0",
	    "id": 64}
	
	try:
		coinbase = requests.post(url, data=json.dumps(payload), headers=headers).json()
	except requests.ConnectionError:
		coinbase = "Unable to connect"
	
	return coinbase["result"]
	
def main():
	url = "http://localhost:8590"
	headers = {'content-type': 'application/json'}
	method = "eth_call"
	coinbase = getCoinbase()
	data = "0xbafb3581000000000000000000000000" + coinbase[2:]
	payload = {
	    "method": method,
	    # To: contract_address
	    "params": [{"to":"0x975fe870924f9f59eb61bf8ad5cf2a058f014c46",
	"data":data}, "latest"],
	    "jsonrpc": "2.0",
	    "id": 1,
	}
	
	
	response = requests.post(url, data=json.dumps(payload), headers=headers).json()
	#print response
	
	### Parsing the output ###
	print "Address: " + "0x" + response["result"][26:66]
	print "Update password in: " + str(int(response["result"][128:130], 16)) + " days"
	print "Initialized: " + response["result"][193:194]
	print "Valid: " + response["result"][257:258]
	print "PKI Changed: " + response["result"][321:322]
	print "Is Master: " + response["result"][385:386]
	key_length = 2 * int(response["result"][512:514], 16)
	print "Length of public key: " + str(key_length)
	key = response["result"][514:514 + key_length]
	print "Public Key in plaintext format: " + "0x" + key
	print "Public Key in plaintext format: " + binascii.unhexlify(key)
	
	#print sys.getsizeof(url) + sys.getsizeof(headers) + sys.getsizeof(data) + sys.getsizeof(payload)
	
###0x89097ac3000000000000000000000000000ab7f233e6b95e91c372f61ba6c3c18807f3d3

if __name__ == "__main__":
    main()
