# imports
import sys

class Vigenere:

	def __init__(self, message, key, cipher = ""):
		self._message = message
		self._key = key
		self._cipher = cipher # aka encrypted message

	def encode(self):
		# get length of key
		lengthKey = len(self._key)
		# get integer-based representations of the key and message
		asciiKey = [ord(i) for i in self._key]
		asciiMessage = [ord(i) for i in self._message]
		# cipher list representing individual integer-based representations of characters
		cipherText = []

		for i in range(0, lengthKey):
			asciiKey[i] -= 97
			asciiMessage[i] -= 97
			cipherNum = (((asciiKey[i] + asciiMessage[i])) % 26) + 97
			cipherText.append(chr(cipherNum))

		cipher = ""

		# pop elements into string
		while(len(cipherText) != 0):
			cipher += str(cipherText.pop(0))

		# update cipher
		self._cipher = cipher

		# return cipher
		return cipher

	def decode(self):
		# get length of key
		lengthKey = len(self._key)
		# get integer-based representations of the key and cipher
		asciiKey = [ord(i) for i in self._key]

		if(len(self._cipher) == 0):
			self._cipher = self._message
		asciiCipher = [ord(i) for i in self._cipher]
		# plain text list representing individual integer-based representations of characters
		plainText = []

		for i in range(0, lengthKey):
			asciiKey[i] -= 97
			asciiCipher[i] -= 97
			plainText.append(chr((((26 + asciiCipher[i] - asciiKey[i]) % 26) + 97)))

		plain = ""
		# pop elements into string
		while(len(plainText) != 0):
			plain += str(plainText.pop(0))

		# return original message
		return plain

# def genKey(key):

length = len(sys.argv)

# too few arguments
if(length < 3):
	print("Usage: py Vig.py -[mode] [key] or py Vig.py -[mode] [key] [i/o red.] [file]")

# no i/o redirection, manual user input
if(length == 3):
	# get mode and key from arguments
	mode = sys.argv[1]
	key = sys.argv[2]
	try:
		key = key.replace(" ", "")
	except:
		pass
	lengthKey = len(key)

	while(True):
		# message to be encoded
		message = input("")
		lengthMes = len(message)
		messKey = ""

		# generate key automatically, due to redundancy
		while(lengthMes >= lengthKey):
			lengthMes -= lengthKey
			messKey += key
		
		# key "vigenere" matching length of message
		messKey += key[0:lengthMes]
		# create Vigenere object for encryption/decryption of messages
		EncDec = Vigenere(message, messKey)

		if(mode == "-e"):
			print(EncDec.encode())

		elif(mode == "-d"):
			print(EncDec.decode())

elif(length == 5):
	# get mode, key, io red., and file from arguments
	mode = sys.argv[1]
	key = sys.argv[2]
	try:
		key = key.replace(" ", "")
	except:
		pass
	ioRed = sys.argv[3]
	ioFile = sys.argv[4]
	lengthKey = len(key)
	message = ""

	# try to read file
	try:
		with open(ioFile) as f:
		    for line in f:
		        message += line
	except:
		pass

	lengthMes = len(message)
	messKey = ""

	# generate key automatically, due to redundancy
	while(lengthMes >= lengthKey):
		lengthMes -= lengthKey
		messKey += key
	
	# key "vigenere" matching length of message
	messKey += key[0:lengthMes]
	# create Vigenere object for encryption/decryption of messages
	EncDec = Vigenere(message, messKey)

	if(mode == "-e"):
		print(EncDec.encode())

	elif(mode == "-d"):
		print(EncDec.decode())

