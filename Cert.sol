pragma solidity ^0.4.0;
contract Certificate {
    address mNode;
    
    struct sNode {
        address nodeAddress;
        uint init;
        string password;
        uint valid;
    }
    
    mapping(address => sNode) connectedNodes;
    
    function Certificate () {
        mNode = msg.sender;
    }
    
    function init() {
        
    }
}
