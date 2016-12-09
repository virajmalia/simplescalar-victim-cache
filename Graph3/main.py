#!/usr/bin/env python

from os import chdir as changeDirectory
from os import listdir
from os import remove
from def_cache_bm1 import run_def_cache_bm1

from vic_cache_1 import run_vic_cache_1
from vic_cache_2 import run_vic_cache_2
from vic_cache_4 import run_vic_cache_4
from vic_cache_8 import run_vic_cache_8
from vic_cache_16 import run_vic_cache_16

from cd import collectData
from plot import plotData

changeDirectory("/home/viraj/Documents/SimpleScalar/simplesim-alpha/results")
filelist = listdir("/home/viraj/Documents/SimpleScalar/simplesim-alpha/results")
for f in filelist:
	remove(f)

changeDirectory("/home/viraj/Documents/SimpleScalar/simplesim-alpha")

run_def_cache_bm1()

run_vic_cache_1()
run_vic_cache_2()
run_vic_cache_4()
run_vic_cache_8()
run_vic_cache_16()

print ('Benchmarking complete!')

collectData()
plotData()
