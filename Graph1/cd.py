#!/usr/bin/env python

from os import listdir
import re

def collectData():
	parameter = 'ul2.accesses'
	sorted_list = sorted(listdir("/home/viraj/Documents/SimpleScalar/simplesim-alpha/results"), key=lambda x: (int(re.sub('\D','',x)),x))

	with open("/home/viraj/Documents/Graph1/data.out", "w") as f:
		for filename in sorted_list:
			with open('/home/viraj/Documents/SimpleScalar/simplesim-alpha/results/' + filename) as currentFile:
				for line in currentFile:
					if parameter in line:
						f.write(filename + ',' + line)
	print ('Data collection complete!')
	return 0
