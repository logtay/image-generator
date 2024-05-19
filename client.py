import zmq

def get_image(keyword):
    """Get an image from Unsplash based on a keyword."""
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    print(f"Sending {keyword} search request...")
    socket.send_string(keyword) # send the request for the keyword

    print(f"Waiting for response...")
    response = socket.recv_string()
    print(response)

keyword = input("Enter the keyword you want to search for: ")
get_image(keyword)
