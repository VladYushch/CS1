import sys
import base64
from string import ascii_letters

alphabet = ascii_letters+"0123456789+/"
print(alphabet)
file = open(input("Select File\n"), "rb")
raw = file.read()
literal_sin = ""
sin_count = 0
basedoutput = ""
quartet = ""

for i in raw:
	thebin = bin(i)[2:]	#this was supposed to remove the binary indicators
	print(thebin, "bin")
	one_sin = "0"* (8-len(thebin)) + thebin # Don't ask. Edit: I'd better explain it. It makes all bytes 8 bits total, since senior 0's are ommited.
	literal_sin += one_sin
	print(one_sin)
for i in range(0, len(literal_sin)):	#seems about right
	quartet += literal_sin[i]
	if len(quartet) == 24:
		for j in range(0, 4):	#Problem is not here. No, BS.
			qlen = len(quartet)
			letterstart = j*6
			letterstop = j*6+6
			letteridbin = quartet[letterstart:letterstop]
			letterid = int(letteridbin, base=2)
			letter = alphabet[letterid]
			basedoutput += letter
			sin_count += 1
		quartet = ""
if len(quartet) == 8:
	while len(quartet) != 12:
		quartet += "0"
	basedoutput += alphabet[int(quartet[0:5], 2)]
	basedoutput += alphabet[int(quartet[6:11], 2)]
	basedoutput += "=="
if len(quartet) == 16:
	while len(quartet) != 18:
		quartet += "0"
	basedoutput += alphabet[int(quartet[0:5], 2)]
	basedoutput += alphabet[int(quartet[6:11], 2)]
	basedoutput += alphabet[int(quartet[12:17], 2)]
	basedoutput += "="

print("Sins commited:", sin_count)
print(basedoutput)
newfile = open("based64_" + file.name, "w+")
newfile.write(basedoutput)
file.close()
newfile.close()

