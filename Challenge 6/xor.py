#####################################################################################################################
#                                                                                                                   #
#       Program 6: XOR Crypto	                                                                           		    #
#       Group Name: Seth                                                                                            #
#       Group Members:  Ethan Clapp, Cameron Thomas, Dylan Weaver, Ghufran Aldawood,                                #
#                       Chris Tullier, David Mains, Will Shepherd                                                   #
#                                                                                                                   #
#####################################################################################################################

# imports
import sys

# get ciphertext from stdin
user_in = sys.stdin.buffer.read()

# get key
f = open('file1', 'rb')
key = f.read()
f.close()

# xor byte conversion
conversion = bytes([_a ^ _b for _a, _b in zip(user_in, key)])

# output conversion to user
sys.stdout.buffer.write(conversion)
