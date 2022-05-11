import os

size = "b"

# starting
offset = "1"
interval = "1"

filename = "9.bmp"
output = ""

# offset change
offset_change = 2
interval_change = 2

for i in range(10):
    for j in range(10):
        output = f"{size}_{offset}_{interval}.png"
        
        command = f"python steg.py -{size} -o{offset} -i{interval} -w{filename} > out/{output}"
        os.system(command)

        interval = str(int(interval) * interval_change)
    interval = "1"
    offset = str(int(offset) * offset_change)
