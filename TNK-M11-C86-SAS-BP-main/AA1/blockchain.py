from hash import generateHash
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
        blockString = str(self.index) + str(self.timestamp) + str(self.previousHash) + str(self.transaction)
        return generateHash(blockString)
    
    def showBlockDetails(self):
        print("**********Block**************")
        print("Block Index", self.index)
        print("Timestamp", self.timestamp)
        print("Transaction", self.transaction)
        print( "Previous Hash",self.previousHash)
        print( "Current Hash",self.currentHash)
        print(" ")

#Create an empty list named chain


transaction1 = { 
        "sender": 'Sam', 
        "receiver": 'Adam', 
        "amount": 10000
    }

blockData1 = {
        'index': 1,
        'timestamp': time(),
        'transaction': transaction1,
        'previousHash': "No Prevoius Hash Present. Since this is the first block.",
    }

block1 = Block(blockData1["index"], 
                 blockData1["timestamp"], 
                 blockData1["transaction"], 
                 blockData1['previousHash'])


transaction2 = { 
        "sender": 'Prince', 
        "receiver": 'John', 
        "amount": 9000
    }

blockData2 = {
        'index': 2,
        'timestamp': time(),
        'transaction': transaction1,
        'previousHash': "No Prevoius Hash Present. Since this is the first block.",
    }

#Create block2 using blockData2



transaction3 = { 
        "sender": 'Mike', 
        "receiver": 'Anny', 
        "amount": 1800
    }

blockData3 = {
        'index': 3,
        'timestamp': time(),
        'transaction': transaction3,
        'previousHash': "No Prevoius Hash Present. Since this is the first block.",
    }

#Create block3 using blockData3


# Append the block1,2,3 to chain


print("********************Blockchain********************")
# Run loop for each block in the chain

    # Call block.showBlockdetails() method
    