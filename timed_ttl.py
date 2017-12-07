import requests
import json
import sys
import time
import binascii

def getCoinbase(url, headers):
		
	# Get coinbase
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
############################################################################################
############################################################################################
######### Calls addTransaction method from MainNet.sol to add transaction to 
###################################      Blockchain 2  #####################################
def updateMainBC(message):
	url = "http://localhost:8545"
	headers = {'content-type': 'application/json'}
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
############################################################################################
############################################################################################
def main():
	url = "http://localhost:8590"
	headers = {'content-type': 'application/json'}
	method = "eth_sendTransaction"
	contract = "0x975fe870924f9f59eb61bf8ad5cf2a058f014c46"
	coinbase = getCoinbase(url, headers) ######
	payload = {
	    "method": method,
	    "params": [{"from":coinbase,"to":contract,
	    "gas":"0x30d40",
	"data":"0x89097ac3"}],
	    "jsonrpc": "2.0",
	    "id": 1,
	}
	start = time.time()
	
	## This code runs every 75s and decrements the counter for passwords for devices on the network
	while(True):
		try:
			response = requests.post(url, data=json.dumps(payload), headers=headers).json()
			updateMainBC("Updated the validity of passwords for the nodes")
		except requests.ConnectionError:
			response = "Unable to connect to local blockchain"
			updateMainBC(response)
		print response
		print "Elapsed time: " + str(time.time() - start)
		start = time.time()
		time.sleep(75)

	try:
		response = requests.post(url, data=json.dumps(payload), headers=headers).json()
		updateMainBC("Updated the validity of passwords for the nodes")
	except requests.ConnectionError:
		response = "Unable to connect to local blockchain"
		updateMainBC(response)
	print response
		
if __name__ == "__main__":
    main()
