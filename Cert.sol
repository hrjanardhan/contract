pragma solidity ^0.4.0;

contract Certificate {
    address mNode;
    
    struct sNode {
        address nodeAddress;
        uint initialized;
        string public_key;
        bool pki_changed;
        string cert;
        bool valid;
        uint ttl;
    }
    
    mapping(address => sNode) connectedNodes;
    address[] nodeAddresses;
    
    function getMasterNode() returns (address) {
        return mNode;
    }
    
    function getNodeDetails(address Address) returns (address, uint, string, bool, string, bool, uint) {
        return (connectedNodes[Address].nodeAddress, connectedNodes[Address].initialized,
        connectedNodes[Address].public_key, connectedNodes[Address].pki_changed, connectedNodes[Address].cert,
        connectedNodes[Address].valid, connectedNodes[Address].ttl);
    }
    
    function Certificate () {
        mNode = msg.sender;
    }
    
    // Only master can add new nodes to the network
    // Two days time is given to change password
    function init(address newNode) {
        if(mNode == msg.sender) {
            connectedNodes[newNode].nodeAddress = newNode;
            connectedNodes[newNode].initialized = 1;
            connectedNodes[newNode].valid = true;
            connectedNodes[newNode].ttl = 2;
            nodeAddresses.push(newNode);
            return;
        }
        return;
    }
    
    // The sNode sends public_key to the master
    function send_pki(string pki) {
        if(connectedNodes[msg.sender].valid == true) {
            connectedNodes[msg.sender].public_key = pki;
            connectedNodes[msg.sender].ttl = 30;
            connectedNodes[msg.sender].pki_changed = true;
        }
    }
    
    // Master node sends a certificate to nodes
    function send_cert(address Address, string cert) {
        if(msg.sender == mNode) {
            if(connectedNodes[Address].pki_changed) {
               connectedNodes[Address].pki_changed = false;
               connectedNodes[Address].cert = cert;
            }
            return;
        }
        return;
    }
    
    // Get the PKI of the node
    function get_pki(address Address) returns (string){
        if(connectedNodes[Address].valid) {
            return connectedNodes[Address].public_key;
        }
        return "INVALID";
    }
    
    // Check and decrement TTL. Mark invalid for expired TTLs
    function check_ttl() {
        for(uint i = 0; i < nodeAddresses.length; i++) {
            if(connectedNodes[nodeAddresses[i]].valid == true) {
                connectedNodes[nodeAddresses[i]].ttl -= 1;
                if(connectedNodes[nodeAddresses[i]].ttl <= 0) {
                    connectedNodes[nodeAddresses[i]].valid = false;
                }
            }
        }
        
    }
}

library StringUtils {
    /// @dev Does a byte-by-byte lexicographical comparison of two strings.
    /// @return a negative number if `_a` is smaller, zero if they are equal
    /// and a positive numbe if `_b` is smaller.
    function compare(string _a, string _b) returns (int) {
        bytes memory a = bytes(_a);
        bytes memory b = bytes(_b);
        uint minLength = a.length;
        if (b.length < minLength) minLength = b.length;
        //@todo unroll the loop into increments of 32 and do full 32 byte comparisons
        for (uint i = 0; i < minLength; i ++)
            if (a[i] < b[i])
                return -1;
            else if (a[i] > b[i])
                return 1;
        if (a.length < b.length)
            return -1;
        else if (a.length > b.length)
            return 1;
        else
            return 0;
    }
    /// @dev Compares two strings and returns true iff they are equal.
    function equal(string _a, string _b) returns (bool) {
        return compare(_a, _b) == 0;
    }
    /// @dev Finds the index of the first occurrence of _needle in _haystack
    function indexOf(string _haystack, string _needle) returns (int)
    {
    	bytes memory h = bytes(_haystack);
    	bytes memory n = bytes(_needle);
    	if(h.length < 1 || n.length < 1 || (n.length > h.length)) 
    		return -1;
    	else if(h.length > (2**128 -1)) // since we have to be able to return -1 (if the char isn't found or input error), this function must return an "int" type with a max length of (2^128 - 1)
    		return -1;									
    	else
    	{
    		uint subindex = 0;
    		for (uint i = 0; i < h.length; i ++)
    		{
    			if (h[i] == n[0]) // found the first char of b
    			{
    				subindex = 1;
    				while(subindex < n.length && (i + subindex) < h.length && h[i + subindex] == n[subindex]) // search until the chars don't match or until we reach the end of a or b
    				{
    					subindex++;
    				}	
    				if(subindex == n.length)
    					return int(i);
    			}
    		}
    		return -1;
    	}	
    }
}
