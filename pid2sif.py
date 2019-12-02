#!/home/dmerrell/envs/py27/bin/python2.7

import sys

fname = sys.argv[1]

f = open(fname, "r")

for line in f:
	parts = line.rstrip().split("\t")
	if len(parts) == 3:
		print "\t".join([parts[0], parts[2], parts[1]])
		

