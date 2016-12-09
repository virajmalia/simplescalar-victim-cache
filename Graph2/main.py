#!/usr/bin/env python

from os import chdir as changeDirectory
from os import listdir
from os import remove
from def_cache_bm1 import run_def_cache_bm1

from miss_cache_1 import run_miss_cache_1
from miss_cache_2 import run_miss_cache_2
from miss_cache_4 import run_miss_cache_4
from miss_cache_8 import run_miss_cache_8
from miss_cache_16 import run_miss_cache_16

from cd import collectData
from plot import plotData

changeDirectory("/home/viraj/Documents/SimpleScalar/simplesim-alpha/results")
filelist = listdir("/home/viraj/Documents/SimpleScalar/simplesim-alpha/results")
for f in filelist:
	remove(f)

changeDirectory("/home/viraj/Documents/SimpleScalar/simplesim-alpha")

run_def_cache_bm1()

run_miss_cache_1()
run_miss_cache_2()
run_miss_cache_4()
run_miss_cache_8()
run_miss_cache_16()

print ('Benchmarking complete!')

collectData()
plotData()
