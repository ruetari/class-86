from hash import generateHash
import json
from time import time

# Cretae Block class
class Block:
    # Define __init__ method with index, timestamp, transaction, previousHash parameters
    def __init__(self, index, timestamp, transaction, previousHash):
        # Store index, transaction, timeStamp, previousHash in respective object variables
        self.index = index
        self.transaction = transaction
        self.timestamp= timestamp
        self.previousHash = previousHash
    
        # Calculate currentHash using the currentHash() method
        self.currentHash = self.calculateHash()
    
    # Create currentHash() method
    def calculateHash(self):
        # Create a variable blockString and store a string made by concatinating index, timestamp, previousHash and transaction 
        blockString=str(self.index)+str(self.timestamp)+str(self.previousHash)+str(self.transaction)
        # Generating hash for blockString and return it
        return generateHash(blockString)
        
    
sender = "Mike"
receiver = "Sam"
sender = generateHash(sender)
receiver = generateHash(receiver)

transaction = { 
        "sender": sender, 
        "receiver": receiver, 
        "amount": 1000
    }

blockData = {
        'index': 1,
        'timestamp': time(),
        'transaction': transaction,
        'previousHash': "No Previous Hash Present. Since this is the first block.",
    }

# Use Block class and blockData to create a newBlock object.
newBlock=Block(blockData["index"],
               blockData["transaction"], 
               blockData["timestamp"],
               blockData["previousHash"],
)

# Display content fo the newBlock
print(newBlock.index)
print(newBlock.timestamp)
print(newBlock.transaction)
print(newBlock.previousHash)
print(newBlock.currentHash)