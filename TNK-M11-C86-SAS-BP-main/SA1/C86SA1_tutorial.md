Prepare the Data for the Block
==============================

In this activity, you will learn to prepare the data for the block and print it.


<img src= "https://media.slid.es/uploads/2071954/images/10647404/Gif_1.gif" width = "521" height = "321">


Follow the given steps to complete this activity.


* Open file app.py.


* Import the time module from the time file.

```sh
	from time import time
```

* Rename the encryptedData to the transaction, which contains sender, receiver, and amount information.

```sh
	transaction = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount }
```


* Create an object blockData and add the transaction data and other data such as an index, timestamp, and hash.

```sh
	blockData = {
		'index': 1,
		'timestamp': time(),
		'transaction': transaction,
		'previousHash': "No Previous Hash Present. Since this is the first block." }
```
       
* Display the data inside the blockData to see the values in it.

```sh
	print(blockData)
```

*Pass the blockData instead of encryptedData to the HTML file to display it on the web page.

```sh
	return render_template('index.html', originalData = originalData, blockData = blockData)
```

* Save and run the code to check the output.
