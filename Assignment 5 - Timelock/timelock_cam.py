import sys
import re
import backports.zoneinfo as zoneinfo
from hashlib import md5
from datetime import datetime, timedelta
from tzlocal import get_localzone
from pytz import timezone
import time


# take stdin as input for epoch
user_in = sys.stdin.readlines()
epoch = user_in[0][:-1]
epoch = epoch.split(" ")

# get local timezone
local = get_localzone()

# format
formats = "%Y %m %d %H %M %S"

## get current time
now = datetime(2013, 5, 6, 7, 43, 25) # was 25
time_cur = now.strftime(formats).split(" ")

# something something comment
epocStr = " "
timeCurStr = " "

# blah blah blha blahh
epocStr = epocStr.join(epoch)
timeCurStr = timeCurStr.join(time_cur)

# datetime objects
d1 = datetime.strptime(epocStr, formats)
d2 = datetime.strptime(timeCurStr, formats)

# calc seconds elapsed
days_elapsed = abs(d2 - d1).days
seconds_elapsed = abs(d2 - d1).seconds
seconds_elapsed += (days_elapsed * 86400)

# check for daylight savings
dst_date2 = datetime(2013, 5, 6, 7, 43, 25, tzinfo=zoneinfo.ZoneInfo(key='US/Central'))
if (dst_date2.dst()):
	seconds_elapsed -= 3600

modQuotient = seconds_elapsed%60

# create hash using MD5
hash1 = md5(str(seconds_elapsed-modQuotient).encode())
hash1000 = hash1.hexdigest()
hash2 = md5(str(hash1000).encode())
time_hash = hash2.hexdigest()
time_hash_rev = time_hash[::-1]

# use regex to get code
match1 = re.findall(r'[a-z]{1}', time_hash)
match2 = re.findall(r'\d{1}', time_hash_rev)
code = match1[0] + match1[1] + match2[0] + match2[1]

# output variables
print("Time elapsed: " + str(seconds_elapsed))
print("Hash: " + time_hash)
print("Code: " + code)

