#!/usr/bin/python
import sys
import argparse

#create seperate files for each hash type
f0= open("argon.hashes", "w+")
f1= open("md5crypt.hashes", "w+")
f2= open("SHA-256.hashes", "w+")
f3= open("SHA-512.hashes", "w+")
f4= open("pbkdf2.hashes", "w+")
f5= open("other.hashes", "w+")

fname = sys.argv[1]
fp = open(fname)
lines = fp.readlines()
for line in lines:
	if"$argon2" in line:
		f0.write(line)
	elif"$1$" in line:
		f1.write(line)
	elif"$5$" in line:
		f2.write(line)
	elif"$6$" in line:
		f3.write(line)
	elif"$pbkdf2" in line:
		f4.write(line)
	else:
		f5.write(line)

fp.close()
