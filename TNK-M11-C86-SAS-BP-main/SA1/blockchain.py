import hashlib
import json
from time import time
class Block:
    def __init__(self, index, timestamp, transaction, previousHash):
        self.index = index
        self.transaction = transaction
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.currentHash = self.calculateHash()
    def calculateHash(self):
        blockString = str(self.index) + str(self.timestamp) + str(self.previousHash) + json.dumps(transaction)
        return hashlib.sha256(blockString.encode()).hexdigest()
    def showBlockDetails(self):
        print("Block Index", self.index)
        print("Timestamp", self.timestamp)
        print("Transaction", self.transaction)
        print( "Previous Hash",self.previousHash)
        print( "Current Hash",self.currentHash)

# SA1:        
transaction = {
        'sender': 'Satoshi',
        'receiver': 'Mike',
        'amount': '1000'
    }

sender = hashlib.sha256(transaction["sender"].encode()).hexdigest()
receiver = hashlib.sha256(transaction["receiver"].encode()).hexdigest()
transaction["sender"] = sender
transaction["receiver"] = receiver

# SA1
blockData = {
        'index': 1,
        'timestamp': time(),
        'transaction': transaction,
        'previousHash': "No Prevoius Hash Present. Since this is the first block.",
    }

newBlock = Block(
    blockData["index"],
    blockData["timestamp"],
    blockData["transaction"],
    blockData["previousHash"])
transaction2 = {
        'sender': 'Vishal',
        'receiver': 'Kunal',
        'amount': '1000'
    }
sender = hashlib.sha256(transaction2["sender"].encode()).hexdigest()
receiver = hashlib.sha256(transaction2["receiver"].encode()).hexdigest()
newBlock.showBlockDetails()