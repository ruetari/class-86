from hash import generateHash
import json
from time import time

class Block:
    #create a class variable index and set it to 0
    

    # Remove index from list of parameters
    def __init__(self, index, timestamp, transaction, previousHash):
        # Set self.index using Block.index
        self.index = index
        self.transaction = transaction
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.currentHash = self.calculateHash()
        # Increment Block.index by 1
        

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

chain = []

transaction1 = { 
        "sender": 'Sam', 
        "receiver": 'Adam', 
        "amount": 10000
    }

blockData1 = {
        'timestamp': time(),
        'transaction': transaction1,
        'previousHash': "No Prevoius Hash Present. Since this is the first block.",
    }
#Remove index from arguments
block1 = Block(
                1,
                 blockData1["timestamp"], 
                 blockData1["transaction"], 
                 blockData1['previousHash'])


transaction2 = { 
        "sender": 'Prince', 
        "receiver": 'John', 
        "amount": 9000
    }

blockData2 = {
        'timestamp': time(),
        'transaction': transaction1,
        'previousHash': "No Prevoius Hash Present. Since this is the first block.",
    }
#Remove index from arguments
block2 = Block(  2,
                 blockData2["timestamp"], 
                 blockData2["transaction"], 
                 blockData2['previousHash'])

transaction3 = { 
        "sender": 'Mike', 
        "receiver": 'Anny', 
        "amount": 1800
    }


blockData3 = {
        'timestamp': time(),
        'transaction': transaction3,
        'previousHash': "No Prevoius Hash Present. Since this is the first block.",
    }

#Remove index from arguments
block3 = Block(
                 3,
                 blockData3["timestamp"], 
                 blockData3["transaction"], 
                 blockData3['previousHash'])

chain.append(block1)
chain.append(block2)
chain.append(block3)

print("********************Blockchain********************")
for block in chain:
    block.showBlockDetails()