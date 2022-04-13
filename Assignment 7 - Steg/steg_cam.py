import sys


#### BYTE METHOD
## STORAGE
#SENTINEL = 


# initialize user set flags
offset = 0
interval = 1
store = False
retrieve = False
bit = False
byte = False
wrapper = ""
secret = ""

# take in user input from flags
for flag in sys.argv:
	if flag == "-s":
		store = True
	elif flag == "-r":
		retrieve = True
	elif flag == "-b":
		bit = True
	elif flag == "-B":
		byte = True
	elif flag[:2] == "-o":
		offset = int(flag[2:])
	elif flag[:2] == "-i":
		interval = int(flag[2:])
	elif flag[:2] == "-w":
		wrapper = flag[2:]
	elif flag[:2] == "-h":
		secret = flag[2:]

# read in bytes from files
f = open(wrapper, 'rb')
wrap_file = f.read()
f.close()

f = open(secret, 'rb')
hide_file = f.read()
f.close()

sys.stdout.buffer.write(wrap_file)

for i in range(0, len(hideme)):
	wrapme[offset] = hideme[i]
	offset += interval
	i += 1
	
for j in range(0, len(SENTINEL)):
	wrapme[offset] = SENTINEL[i]
	offset += interval
	i += 1
	
	
## EXTRACTION



### BIT METHOD
## STORAGE



## EXTRACTION



