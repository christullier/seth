import sys
import re
from hashlib import md5


# take stdin as input for epoch
user_in = sys.stdin.readlines()
epoch = user_in[0][:-1]

# set current time using variable
time_cur = "2013 05 06 07 43 25"

# split the times into arrays using spaces
vals_e = epoch.split(" ")
vals_c = time_cur.split(" ")

# initialize variable for seconds elapsed
seconds_elapsed = 0

# calculate number of seconds elapsed
for i in range(0, 6):
	if i == 0:
		val = 31557600
	elif i == 1:
		val = 2629800
	elif i == 2:
		val = 86400
	elif i == 3:
		val = 3600
	elif i == 4:
		val = 60
	elif i == 5:
		val = 1
	
	seconds_elapsed += (int(vals_c[i]) - int(vals_e[i])) * val

# check for daylight savings time (somehow)
# idk

# create hash using MD5
hash1 = md5(str(seconds_elapsed).encode())
time_hash = hash1.hexdigest()
time_hash_rev = time_hash[::-1]

# use regex to get code
match1 = re.findall(r'[a-z]{1}', time_hash)
match2 = re.findall(r'\d{1}', time_hash_rev)
code = match1[0] + match1[1] + match2[0] + match2[1]

# output variables
print("Time elapsed: " + str(seconds_elapsed))
print("Hash: " + time_hash)
print("Code: " + code)

