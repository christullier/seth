# use Python 3
import socket
from time import sleep

# set the port for client connections
port = 1337

# create the socket and bind it to the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))

# listen for clients
# this is a blocking call
s.listen(0)
print("Server is listening...")

# a client has connected!
c, addr = s.accept()

# set the message
msg = "Some message...\n"

# send the message, one letter at a time
for i in msg:
	c.send(i.encode())
	# delay a bit in between each letter
	sleep(0.1)

# send EOF and close the connection to the client
c.send("EOF".encode())
print("Message sent...")
c.close()

