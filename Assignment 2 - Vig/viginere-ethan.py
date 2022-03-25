#####################################################################################################################
#                                                                                                                   #
#       Program 2: Viginere Cypher                                                                                  #
#       Group Name: Seth                                                                                            #
#       Group Members:  Ethan Clapp, Cameron Thomas, Dylan Weaver, Ghufran Aldawood,                                #
#                       Chris Tullier, David Mains, Will Shepherd                                                   #
#                                                                                                                   #
#####################################################################################################################

# Import used for taking in command line arguments
import sys

############################################       MINOR METHODS       ############################################

# split(String): takes a string and splits it into characters. Not really sure why this is a method, but it does tidy up the code a little
def split(word):
    wordArray = list(word)
    return wordArray

# modulus(char, char, int): takes a character and encrypts/decrypts it. Kind of a bulky method, definitely could use some rewriting.
# The first argument is the message char, the second is the key char, and the final arg dictates if the final calculation encrypts or decrypts
def modulus(msg, key, encryption):

    # this checks if the message is a capital letter. If so, converts the letter to its respective number (0-25) and flags a capitalization variable
    if (msg >= 65 and msg <= 90):
        capitalization = 0
        msg = msg - 65

    # the same as the above statement, but lowercase instead
    elif (msg >= 97 and msg <= 122):
        capitalization = 1
        msg = msg - 97
    
    # this checks if the input message char is not a letter. If so, just returns the message char without change
    else:
        return msg

    # checks if the key char is upper case and converts the char to its respective number (0-25)
    if (key >= 65 and key <= 90):
        key = key - 65

    # the same as the above if statement, but lower case. No capitalization flag is needed since capitalization of the key is ignored by assignment instructions
    else:
        key = key - 97
    
    # if the encryption flag (3rd arg from the method call) is set, adds and mods out by 26, i.e. encrypts the msg char with the given key char
    if (encryption == 1):
        output = (msg + key) % 26

    # if the encryption flag is set to false, decrypts instead. Nifty that python can handle negative moduli
    else:
        output = (msg - key) % 26

    # if the capitalization flag is set to true, turns the output message char to upper case
    if (capitalization == 0):
        output += 65

    # if the capitalization flag is set to false, turns the output msg char to lower case
    else:
        output += 97
    
    return output

    
############################################       ENCODER/DECODER       ############################################

# encoder(String, String): takes a message string and key string and encrypts the message with the given key. In hindsight, there was no need for separate methods
# for encrypt/decrypt since the actual operation is done in a separate method, which has an encrypt/decrypt flag anyways. It is what it is
def encoder(msg, key):
    encodedArray = []

    msgArray = split(msg)
    keyArray = split(key)

    a = 0
    b = 0

    while (True):
        # converts the msg char and the key char into an integer and sends them off to the modulus function. Following line adds whatever the output is into the
        # final message list
        encodedMsg = modulus(ord(msgArray[a]), ord(keyArray[b]), 1)
        encodedArray.append(chr(encodedMsg))
        a += 1

        # this checks if the msg char that was sent to the modulus function was a letter char. If so, moves on to the next char in the key.
        # Does not increment if the msg char was a space or punctuation mark so that the key does not get off beat with the msg
        if ((encodedMsg >= 97 and encodedMsg <= 122) or (encodedMsg >= 65 and encodedMsg <= 90)):
            b += 1

        # if the end of the msg array is reached, breaks the while loop. If the end of the key is reached, wraps back around to the beginning of the key
        if (a >= len(msgArray)):
            break
        if (b >= len(keyArray)):
            b = 0

    encodedMsg = "".join(encodedArray)

    return encodedMsg

# decoder(String, String): imagine literally everything is the same as above, but you decode instead of encode. Originally split since the choice of encode/decode
# was built into these methods, but later moved to the modulus method
def decoder(msg, key):
    decodedArray = []

    msgArray = split(msg)
    keyArray = split(key)

    a = 0
    b = 0

    while (True):
        decodedMsg = modulus(ord(msgArray[a]), ord(keyArray[b]), 1)
        decodedArray.append(chr(decodedMsg))
        a += 1
        if (decodedMsg != 32):
            b += 1
        if (a >= len(msgArray)):
            break
        if (b >= len(keyArray)):
            b = 0
    
    decodedMsg = "".join(decodedArray)

    return decodedMsg

############################################       MAIN       ############################################

# takes in the arguments given in the command line
args = sys.argv

# takes the key (the 3rd and final arg given at runtime) and turns it into a string without spaces
key = args[2].replace(" ", "")

# checks if the arg for encryption was given. If so, encrypts with the given key
if (args[1] == "-e"):
    while (True):
        message = input()
        encryptedMsg = encoder(message, key)
        print(encryptedMsg)

# if the arg for decryption was given, decrypts with the given key
elif (args[1] == "-d"):
    while (True):
        message = input()
        decryptedMsg = decoder(message, key)
        print(decryptedMsg)

# returns an error message if the 2nd arg was not '-e' or '-d'
else:
    print("Sorry, {} is not an accepted argument. Use '-e' for encrypting and '-d' for decrypting.")