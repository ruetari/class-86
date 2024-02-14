Display the Data On the Web Page
============================


In this activity, you will learn to prepare the data for the block and display the data on the web page.


<img src= "https://media.slid.es/uploads/1525749/images/10644036/pasted-from-clipboard.png" width = "521" height = "233">


Follow the given steps to complete this activity:


* Open the file `app.py`.


* Import the block class from the blockchain.py file.

```sh
    from blockchain import Block
```
    

* Create the newBlock using the data stored in the blockData.

```sh
    newBlock = Block(
                    blockData["index"], 
                    blockData["timestamp"], 
                    blockData["transaction"],
                    blockData["previousHash"])
```

* Pass the newBlock data instead of blockData in the variable named blockData to the index.html file to display the data on the HTML page.
 
```sh
    return render_template('index.html', originalData = originalData, blockData = newBlock)
```
   	 

* Open the file `index.html` from the template folder.

* Display the data inside the newBlock by accessing the data from the blockData object in an HTML page. 

```sh
    <div id="indexData">Index: {{ blockData.index }}</div>
	<div id="senderData">Sender: {{ blockData.transaction["sender"] }}</div>
	<div id="receiverData">Receiver: {{ blockData.transaction["receiver"] }}</div>
	<div id="amountData">Amount: {{ blockData.transaction["amount"] }}</div>
	<div id="previousHashData">Previous Hash: {{ blockData.previousHash }}</div>
	<div id="timestampData">Timestamp: {{ blockData.timestamp}}</div>
```
   
* Save and run the code to check the output.
