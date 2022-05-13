################################################################################
# Name: Team Chariot- Ahmed Mudhish, Andre Caver, Avery Miller, Brianna Stewart
# Garrett Gresham, Kevin Oubre, Sydney Holland
# Date: 04/05/2021
# Description: 03- FTP (storage) Covert Channel Program | Ver: 3.8.5
#
# A Python program that can extract a covert message from the file permissions
# of a FTP server.
################################################################################
from sys import stdin
# FTP site specifics variables (ip address, port, directory, method)
# IP = "138.47.102.106"
# PORT = 8008
# USER = "thesun"
# PASSWORD = "myfirstchallenge"
METHOD = 7
# DIRECTORY = "/.secretstorage/.folder2/.howaboutonemore/"
# USE_PASSIVE = True

# converts a string of permissions to a string of binary data
def ConvertPermsToBinary(str):
    converted = ""
    # read every character in the permissions
    for char in str:
        # if the character is a dash (no permission), then represent it as 0
        if(char == "-"):
            converted += "0"
        # otherwise, represent it as 1
        else:
            converted += "1"

    return converted

# using 7-bit conversion, this function converts a list of permissions into a message using
# ConvertPermsToBinary() and returns the message
def SevenBitConversion(data):
    message = ""
    # read each line of permissions in data
    for permission in data:
        # if the first 3 characters in the permissions are dashes, then convert
        if(permission[:3] == "---"):
            message += chr(int(ConvertPermsToBinary(permission), 2))
        # otherwise, ignore the other permissions
        else:
            continue

    return message

# using 10-bit conversion, this function converts a list of permission into a message using
# ConvertPermsToBinary() and returns the message
def TenBitConversion(data):
    # concatenate all of the coverted binary permissions in a string
    binaryData = ""
    for permission in data:
        binaryData += ConvertPermsToBinary(permission)

    # separate the binary permissions into 7-bits and add them to a list
    modifiedData = []
    str = ""
    count = 0

    for char in binaryData:
        # if the current character is the 6 of 7 bit
        if(count == 6):
            # then add the last character to str, append the 7-bits to the list, and reset str and count
            str += char
            modifiedData.append(str)
            str = ""
            count = 0
        # otherwise, add the character to str and increment the counter
        else:
            str += char
            count += 1

    # convert the list of binary permissions into a message using ConvertPermsToBinary()
    message = ""
    for permission in modifiedData:
        message += chr(int(permission, 2))

    return message

################
##### MAIN #####
################
text = stdin.read().rstrip("\n")
files = text.split("\n")

# isolate permissions
data = []
for line in files:
	data.append(line[:10])

# decode permissions
# if the reading mode is 7-bit, then output the message as 7-bit ASCII
if(METHOD == 7):
    message = SevenBitConversion(data)
    print(message)
# otherwise (10-bit), output the message as 7-bit ASCII
else:
    message = TenBitConversion(data)
    print(message)
