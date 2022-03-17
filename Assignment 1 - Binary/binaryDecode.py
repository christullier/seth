import sys

# Not pretty, sorry bout that lol

# reads the file and takes off the newline at the end
lines = sys.stdin.readlines()
[line.rstrip('\n') for line in lines]
text = lines[0]

# initializes needed variables
counter = 0
bin_size = 0
bin_char = ""
ascii_word = ""

# calculates the 'size' (number of digits) in the file
# idk why len(text) didn't work but this does, oh well
size = 0
for char in text:
    if char == "1" or char == "0":
        size += 1

# sets the binary character length based on the size of the file
if (size % 7) == 0:
    bin_size = 7
else:
    bin_size = 8

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
print(ascii_word)
