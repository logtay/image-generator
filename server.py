import zmq
import requests
import random

api_key = "wJSmo-AyvJ17QPhrBrdAT_JQSWw9rLcLlH9Mbv6Fc08"

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    keyword = socket.recv_string()
    endpoint = f"https://api.unsplash.com/search/photos?query={keyword}&per_page={10}&client_id={api_key}" # unsplash search
    response = requests.get(endpoint)

    if response.status_code == 200: # request was successful
        results = response.json()
        total = results["total"] # number of results found

        if total > 0:
            images = results["results"] # collects all results given
            random.shuffle(images) # shuffle images to prevent duplicate responses
            image = images[0] # take the first image
            url = image["urls"]["regular"]

            socket.send_string(url) # send the url back
        else:

            socket.send_string(f"No images found matching {keyword}") # no images were found to match search
    else:
        socket.send_string("Error:", response.status_code) # server error occurred
