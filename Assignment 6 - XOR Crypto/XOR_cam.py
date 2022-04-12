import sys


# take stdin as input for epoch
user_in = sys.stdin.buffer.read()

# take input from key file
f = open('key2', 'rb')
key = f.read()
f.close()

def byte_xor(ba1, ba2):
	return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

conversion = (byte_xor(user_in, key))

print(conversion)

