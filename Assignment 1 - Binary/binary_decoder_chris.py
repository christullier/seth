import sys

binary = []
output = ""


# get binary file from input
# should only be one line
for line in sys.stdin:
    # chop off the newline
    binary = (line[:-1])

# split binary
if len(binary) % 7 == 0:
    jump = 7
else:
    jump = 8

# https://stackoverflow.com/questions/43982938/split-string-into-groups-of-3-characters
# splits the long binary string into sections of length 'jump'
binary_split = [binary[i:i+jump] for i in range(0, len(binary), jump)]

# find the ascii value of each section adn convert it to legible text
for num in binary_split:
    # convert binary to int
    int_ascii = int(num, 2)

    # if backspace
    if int_ascii == 8:
        # remove the last character 
        output = output[:-1] 
        continue # skip rest of for loop

    converted_char = chr(int_ascii)
    output += converted_char
    
print(output) 
