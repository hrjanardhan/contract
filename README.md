# contract

Smart contract to enforce password change in IoT devices

# Installation
1. Download go-ethereum from https://geth.ethereum.org/downloads/
2. Download node.js https://nodejs.org/en/download/package-manager/
```linux
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
```
```
sudo apt-get install -y build-essential
```
3. Install python 3.2

# Setup
1. Create a directory where you want to store the blockchain Eg. ~/Ethereum
2. Create a *genesis.json*
```
{
    "config": {
        "chainId": 15,
        "homesteadBlock": 0,
        "eip155Block": 0,
        "eip158Block": 0
    },
    "difficulty": "40",
    "gasLimit": "2100000",
    "alloc": {
        "0xce17ebbb2f5432efdfdc17a63d051e56f3b82ec7": { "balance": "300000" }
    }
}
```
3. Initialize the blockchain - Run ```geth --datadir . init genesis.json```.
4. Start the block chain ```geth --datadir . console```
Use appropriate switches as mentioned in https://github.com/ethereum/go-ethereum
5. Create an account - From the console, run ```personal.newAccount("private_key")```

# API Information
The application can be divided into two parts:
* Smart Contract - Resides on the blockchain
* Python code - Resides on the device

## Smart Contract
The smart contract is deployed on the block chain. Miners run the smart contract to create transactions(update state of devices) and fetch device details.

#### getMasterNode() returns (address)()
Args: None
Returns: Address of the master node on the network

#### init(address newNode) returns (string)()
Args: Address of the new node to be initialized
Returns: Address "Success" or "Failure" stuatus while trying to add a device to the network

#### get_pki(address Address) returns (string)
Args: Address of the node whose public key is required
Returns: The public key of the node

#### send_pki(string pki)
Args: Public key to be stored on blockchain
Returns: None

#### send_cert(address Address, string cert)
Args: Address to which the certificate is to be sent, certificate
Returns: None

#### check_ttl()
Args: None
Returns: None
Description: Decrements the time to live on the network for the nodes. If the ttl of nodes reach zero, they will be marked dirty and will be banned from the network.
