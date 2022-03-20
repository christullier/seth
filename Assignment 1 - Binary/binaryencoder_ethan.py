# this allows for redirecting a file of a string of 0's and 1's, sets this string to msg
msg = input()

# breaks the string from msg into 7-bit and 8-bit chunks respectively
charArray7 = [msg[i:i+7] for i in range(0, len(msg), 7)]
charArray8 = [msg[i:i+8] for i in range(0, len(msg), 8)]

# initialization stuff
msgList7 = []
msgList8 = []

# converts the binary chunk into an integer and converts the integer to a character
for j in range(0, len(charArray7)):
    msgList7.append(chr(int(charArray7[j], 2)))

for h in range(0, len(charArray8)):
    msgList8.append(chr(int(charArray8[h], 2)))

# joins the array of characters into a string for output
final7 = "".join(msgList7)
final8 = "".join(msgList8)

# final output
print("7 bit decoder output: {}\n8 bit decoder output: {}".format(final7, final8))