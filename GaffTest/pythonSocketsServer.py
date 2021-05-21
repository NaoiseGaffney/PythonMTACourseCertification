import socket

ip = socket.gethostbyname("www.google.com")
print(ip)
ip = socket.gethostbyname("localhost")
print(ip)

# first of all import the socket library
import socket

# next create a socket object
s = socket.socket()
print ("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)
print ("socket is listening")

iteration = 0
# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print ("Got connection from", addr )

    iteration = iteration +1
    print("Iteration: ", iteration)
    # send a thank you message to the client.
    clientMessage = f"Thank you, {addr}, for connecting. You are connection number {iteration}."
    clientMessageBytes = bytes(clientMessage, "utf-8")
    c.send(clientMessageBytes)
    # c.send(b"Thank you for connecting.")

# Close the connection with the client
c.close()
