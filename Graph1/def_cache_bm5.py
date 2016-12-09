#!/usr/bin/env python

import fileinput
import os
import gc

def run_def_cache_bm5():
	cmd = './sim-cache -redir:sim '
	sim_file = 'results/sim_dc5.out'		#change 3 with benchmark of choice, dc-->Default Cache
	bm_dir = ' /home/viraj/Documents/SimpleScalar/simplesim-alpha/benchmarks/'
	bm = '5.alpha '					#change 3 with benchmark of choice
	bm_in = '</home/viraj/Documents/SimpleScalar/simplesim-alpha/benchmarks/1stmt.i>'
	asm_out = 'OUTdc5'				#change 3 with benchmark of choice, dc-->Default Cache
	run_cmd = cmd + sim_file + bm_dir + bm + bm_in + asm_out
	
	path = '/home/viraj/Documents/SimpleScalar/simplesim-alpha/'

	

	print ('Running ' + bm + 'for Default Cache config')
	os.system(run_cmd)

	second = "statistics"
	count = 0

	with open(path + sim_file,'r') as myFile:
		for num, line in enumerate(myFile, 1):
			found=False		
			if second in line:
				count+=1
				found = True
				#print ('found at line:', num)
				if count == 2:
					break

	if found == 1:
		for line in fileinput.input(path + sim_file, inplace = True):
			if fileinput.lineno() <= num:
				continue
			else:
				print (line, end='')

            
	for line in fileinput.input(path + sim_file, inplace = True):
		if " " in line:
			line = line.replace(' ',',',1)
			line = line.replace(' ','')
		if "#" in line:
			line = line.replace('#',',',1)
			print (line, end='')
		else:
			print (line, end='')
	return '0'
	gc.collect()
	
