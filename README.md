## Image Generator Microservice

**Communication Contract**

### How to Request Data (with Example Call)
To request data, use the client.py code. The client code takes a keyword from the user. The keyword is then used in the get_image(keyword) function, sending the request through the pipeline using ZeroMQ. 

**Example Call:** get_image("spa")

### How to Receive Data

Once the server is running and listening for a request, you can begin using the micro service. The client.py file takes a keyword and sends it to the server which then interacts with the API. The image URL is then sent back to the client via the ZeroMQ pipeline. 

**Instructions:**
1. Download both server.py and client.py files. 
2. Open in your IDE of choice. I used PyCharm. 
3. Open two terminals. 
4. Run the server code using the command `python3 server.py`
5. Run the client code using the command `python3 client.py`
6. Enter the desired keyword and receive URL. 


### Other Notes

* You must have ZeroMQ installed using command `pip3 install pyzmq`

* You must create your own Unsplash API Key using [the Unsplash API developers site](https://unsplash.com/developers). Replace `your_api_key` in the server.py file with your key. 

### Diagram
![diagram](Diagram.jpg)
