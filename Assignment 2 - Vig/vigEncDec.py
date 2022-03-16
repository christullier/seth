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
			cipherNum = (((asciiKey[i] + asciiMessage[i])) % 26) + 97
			print(cipherNum)
			cipherText.append(chr(cipherNum))

		print(cipherText)
		cipher = ""
		# pop elements into string
		while(len(cipherText) != 0):
			cipher += str(cipherText.pop(0))

		print(cipher)
		# update cipher
		self._cipher = cipher

		# return cipher
		return cipher

	def decode(self):
		# get length of key
		lengthKey = len(self._key)
		# get integer-based representations of the key and cipher
		asciiKey = [ord(i) for i in self._key]
		asciiCipher = [ord(i) for i in self._cipher]
		# plain text list representing individual integer-based representations of characters
		plainText = []

		for i in range(0, lengthKey):
			plainText.append(chr((((26 + asciiCipher[i] - asciiKey[i])%26)+97)))

		plain = ""
		# pop elements into string
		while(len(plainText) != 0):
			plain += str(plainText.pop(0))

		# return original message
		return plain

# message to be encoded
message = "howdoesthiswork"
lengthMes = len(message)
# create key automatically, due to redundancy
key = ""
# note -- it does not necessarily need to be "vigenere;" however, the process is the same. just replace
# the vig text with another base key
vig = "vigenere"
lengthVig = len(vig)
while(lengthMes >= lengthVig):
	lengthMes -= lengthVig
	key += vig
# key "vigenere" matching length of message
key += vig[0:lengthMes]

# create Vigenere object for encryption/decryption of messages
EncDec = Vigenere(message, key)
print(EncDec.encode())
print(EncDec.decode())