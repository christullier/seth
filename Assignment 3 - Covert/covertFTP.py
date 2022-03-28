import os
from ftplib import FTP


IP = "138.47.99.64"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "7"
USE_PASSIVE = True

BITS = 7
METHOD = 'decode'


#
def encode_ftp():
	counter = 0
	user_in = input('Enter message to be encoded: ')

	for c in user_in:
		cmod = ""
		bin_c = (bin(ord(c)))
		cmod += str(int("00" + bin_c[2:3],2))
		cmod += str(int(bin_c[3:6],2))
		cmod += str(int(bin_c[6:9],2))
		
		os.system(f"touch file{counter}")
		os.system(f"chmod {cmod} file{counter}")
		counter += 1


# ripped from binary decoder, could maybe import for easier reading
def decode_bin(bin_size, text):
	# initializes needed variables
	counter = 0
	bin_char = ""
	ascii_word = ""

	# goes through all 1's and 0's
	for char in text:
		if char == "1" or char == "0":
			# concatenates the bits until it reaches the binary length we set
			if counter < bin_size:
				bin_char = bin_char + char
				counter += 1
		# once the length is hit, convert the binary character into an ASCII character,
		# then append to the ASCII text, also set counters to 0
		if counter == bin_size:
		    ascii_char = chr(int(bin_char, 2))
		    ascii_word = ascii_word + ascii_char
		    bin_char = ""
		    counter = 0

	# output the final word or phrase
	print(f"{bin_size} bit: {ascii_word}")


# currently only decodes 7 bit, need to make it decode 7 and 10
def decode_ftp():
	perms = ''
	perms_bin = ''
	for f in files:
		perms = f[3:10]
		if (f[:3] == '---'):
			for char in perms:
				if char == 'r' or char == 'w' or char == 'x':
					perms_bin += '1'
				elif char == '-':
					perms_bin += '0'
	
	decode_bin(7, perms_bin)


# creates FTP instance, connects via IP, and logs in using credentials
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# copies contents of FOLDER location to files list (with permissions)
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# quits the FTP instance
ftp.quit()

decode_ftp()

