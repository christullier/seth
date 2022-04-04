from socket import socket, AF_INET, SOCK_STREAM
from time import sleep

# set timings for bits
ZERO = 0.031
ONE = 0.11

# set port for server
ip = ""
port = 1337

# create socket and bind to port
s = socket(AF_INET, SOCK_STREAM)
s.bind((ip, port))

# set server to listen for connections
s.listen(0)
print("Server is listening...")

# save socket of connection to c
c, addr = s.accept()

# define overt message to be sent
msg = "BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH BLAH\n"

# define covert message to be encoded
msg_c = "Secret message" + "EOF"
msg_c_bin = ""

for char in msg_c:
	char_bin = bin(ord(char))[2:].zfill(8)
	msg_c_bin += char_bin

# send characters of message
n=0
for i in msg:
	# send overt character to client
	c.send(i.encode())
	
	# change sleep depending on bits to encode
	if msg_c_bin[n] == "0":
		sleep(ZERO)
	else:
		sleep(ONE)
	
	# increment n but stay within bounds of covert message length
	n = (n+1) % len(msg_c_bin)

# send EOF to finish message
c.send("EOF".encode())
print("Message sent...")
c.close()