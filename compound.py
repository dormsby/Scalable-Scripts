#!/usr/bin/python
import sys

f0= open("8CharCom.txt", "w+")
fname = sys.argv[1]
fp = open(fname)
lines = fp.readlines()
lines2 = lines
for line in lines:
	for line2 in lines2:
		s=""
		s+=line.rstrip("\n")
		s+=line2
		f0.write(s)
fp.close()
