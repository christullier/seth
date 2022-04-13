import sys
import re
import zoneinfo
from hashlib import md5
from datetime import datetime
from tzlocal import get_localzone
from pytz import timezone

# get epoch from user via stdin
user_in = sys.stdin.readlines()
epoch = user_in[0][:-1]
epoch = epoch.split(" ")

# get local timezone
local = get_localzone()
# format
format = "%Y %m %d %H %M %S"
# get current time
# now = datetime.now(local)
now = datetime(2017, 3, 23, 18, 2, 6)
time_cur = now.strftime(format).split(" ")

# string representations of above lists for
# current and epoch times
epocStr = " "
epocStr = epocStr.join(epoch)
timeCurStr = " "
timeCurStr = timeCurStr.join(time_cur)
# date-time objects
d1 = datetime.strptime(epocStr, format)
d2 = datetime.strptime(timeCurStr, format)
# calculate number of seconds elapsed
days_elapsed = abs(d2 - d1).days
seconds_elapsed = abs(d2 - d1).seconds
seconds_elapsed += (days_elapsed * 86400)
# check for dst
dst_date2 = datetime(2017, 3, 23, 18, 2, 6, tzinfo = zoneinfo.ZoneInfo(key = 'US/Central'))
if(dst_date2.dst()):
	seconds_elapsed -= 3600
# find distance to beginning of 60-second interval
modQuotient = seconds_elapsed%60

# create hash using MD5
hash1 = md5(str(seconds_elapsed-modQuotient).encode())
time_hash = hash1.hexdigest()
hash1 = md5(str(time_hash).encode())
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