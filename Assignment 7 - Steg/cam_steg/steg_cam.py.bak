import sys
import os


##### CLEAN UP REDUNDANCIES IN RETRIEVAL CAMERON PLEASE ITS GROSS #####
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

if byte:
	#### BYTE METHOD
	
	# set sentinel value for bytes
	SENTINEL = bytearray("EOF", "UTF-8")
	
	# read in bytes from files
	f = open(wrapper, 'rb')
	wrapme = bytearray(f.read())
	f.close()
	
	if store:
		f = open(secret, 'rb')
		hideme = bytearray(f.read())
		f.close()

	# get number of bytes in files, may not be neccessary
	wSize = os.path.getsize(f"./{wrapper}")
	hSize = os.path.getsize(f"./{secret}")
	
	if store:
		## STORAGE

		# run loop to hide bytes in wrapper
		for i in range(0, len(hideme)):
			wrapme[offset] = hideme[i]
			offset += interval
			i += 1
			
		for j in range(0, len(SENTINEL)):
			wrapme[offset] = SENTINEL[j]
			offset += interval
			j += 1

		sys.stdout.buffer.write(wrapme)
	
	elif retrieve:
		## EXTRACTION
		sent_found = False
		empty = bytearray()
		pos_sent_buff = bytearray()
		b = bytearray(1)
		while (offset < len(wrapme) and sent_found == False):
			b[0] = wrapme[offset]
			
			# if b matches first SENTINEL byte and SENTINEL not found
			if ((b[0] == SENTINEL[0]) and (sent_found == False)):
				# create a buffer for possible SENTINEL bytes
				# set SENTINEL index
				# increment offset
				# set possibility of SENTINEL to true
				pos_sent_buff.extend(b)
				sent_i = 1
				offset += interval
				sent_pos = True
				# while a SENTINEL is possible and not found yet
				while ((sent_pos) and (sent_found == False)):
					b[0] = wrapme[offset]
					# if b matches the next SENTINEL byte, continue search
					if (b[0] == SENTINEL[sent_i]):
						pos_sent_buff.extend(b)
						offset += interval
						sent_i += 1
					# else if it does not match, break off search for now and add buffer to file
					elif (b[0] != SENTINEL[sent_i]):
						sent_pos = False
						empty.extend(pos_sent_buff)
					# if possible SENTINEL equals SENTINEL set it to found, otherwise...
					if (pos_sent_buff == SENTINEL):
						sent_found = True
						break
						
			# add byte to hidden file and increase index
			if not sent_found:				
				empty.extend(b)
				offset += interval
		
		# write to stdout
		sys.stdout.buffer.write(empty)


elif bit:
	### BIT METHOD
	if store:
		## STORAGE
		placeholder = ""


	elif retrieve:
		## EXTRACTION
		nothinghere = ""



