import requests
import json
import sys
import binascii


def main():
	url = "http://localhost:8590"
	headers = {'content-type': 'application/json'}
	method = "eth_sendTransaction"
	contract = "0x975fe870924f9f59eb61bf8ad5cf2a058f014c46"
	"""  params = [{"to":"0x1c3ffad5507350dc196fef7d9f1633850383adfc",
	"data":"0x19ab453c"}]  """
	
	address = raw_input("Enter the address to initialize: ")
	data = "0x19ab453c" + "0" * 24 + address[2:]
	
	payload = {
	    "method": method,
	    "params": [{"from":"0x4c8550f577da8c3a4e3916b545947fcd6cb04c14", "to":contract,
	    "gas":"0x30d40",
	"data":data}],
	    "jsonrpc": "2.0",
	    "id": 1,
	}
	#print data
	try:
		response = requests.post(url, data=json.dumps(payload), headers=headers).json()
		updateMainBC(address + " has been added to the blockchain")
	except requests.ConnectionError:
		response = "Unable to connect to local blockchain"
		updateMainBC(response)
	print "Local blockchain Response"
	print response
	
	
def updateMainBC(message):
	url = "http://localhost:8545"
	headers = {'content-type': 'application/json'}
	
	# Preparing the argument for the main blockchain's addTransaction() function. Refer MainNet.sol
	# Refer Contract ABI - https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI for more details on how to prepare the arguments
	data = "0x517715f00000000000000000000000000000000000000000000000000000000000000020"
	
	message_len = str(hex(len(message)))[2:]
	message = binascii.hexlify(message)
	param1 = (64 - len(message_len)) * "0" + str(message_len)
	data += param1
	message += (64 - (len(message) % 64))*"0"
	data += message
	
	payload = {
	    "method": "eth_sendTransaction",
	    "params": [{"from":"0xe660933aaf71862c60390ea88f95514b95c565af", "to":"0x625edaaa2e127a6a1580d927ae7a9d1c16c86cfc",
	    "gas":"0xf0d40",
	"data":data}],
	    "jsonrpc": "2.0",
	    "id": 1,
	}
	try:
		response = requests.post(url, data=json.dumps(payload), headers=headers).json()
	except requests.ConnectionError:
		response = "Unable to connect to main blockchain"
	print "Main blockchain response"
	print response
		
if __name__ == "__main__":
    main()

