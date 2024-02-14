from flask import Flask, render_template, request
import os
from hash import generateHash
#Import time from time
from time import time
STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

@app.route("/", methods= ["GET", "POST"])
def home():
    validation = None
    if request.method == "GET":
        return render_template('index.html')
    elif request.args.get("form") == "f1":
        sender = request.form.get("sender")
        receiver = request.form.get("receiver")
        amount = request.form.get("amount")
       
        originalData = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount
            }
        
        sender = generateHash(sender)
        receiver = generateHash(receiver)

        # Change the name encryptedData to transaction
        transaction = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount,
            }
        
        # Create blockData with index, timestamp, transaction, previousHash
        blockData={
            'index':1,
            'timestamp':time(),
            'transaction':transaction,
            'previousHash':"No previous Has Present.As this is first Block"
        }
        # Print the blockData
        print(blockData)
         
     # Instead of encryptedData return the blockData
    return render_template('index.html', originalData = originalData, blockData = blockData)
    
if __name__ == '__main__':
    app.run(debug = True, port=4000)