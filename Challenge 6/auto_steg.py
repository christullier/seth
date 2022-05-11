# note: there needs to be an 'out' file
import os

b_method = "B"

# starting values
offset = "1"
interval = "1" 

filename = "e5532426b580be8ec82f0ab2f4fd4433.bmp"
# have it search for all filetypes that we're looking for
# eg. grab all .bmp files
output = ""

# offset change
offset_change = 2
interval_change = 2

for i in range(10):
    for j in range(10):
        output = f"{b_method}_{offset}_{interval}.txt"
        
        # -r for retrieving -s for storing
        # but we're only using the for retrieval
        # sample:
        # python steg.py -r -b -o2 -i2 -wName > output
        command = f"python steg.py -r -{b_method} -o{offset} -i{interval} -w{filename} > out/{output}"
        os.system(command)

        interval = str(int(interval) * interval_change)
    interval = "1"
    offset = str(int(offset) * offset_change)
