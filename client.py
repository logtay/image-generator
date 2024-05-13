import zmq

def get_image(keyword):
    """Get an image from Unsplash based on a keyword."""
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    socket.send_string(keyword) # send the request for the keyword

    response = socket.recv_string()
    print(response)

keyword = input("Enter the keyword you want to search for: ")
get_image(keyword)
