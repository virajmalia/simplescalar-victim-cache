#!/usr/bin/env python

from os import chdir as changeDirectory
from os import listdir
from os import remove

from def_cache_bm1 import run_def_cache_bm1
from def_cache_bm2 import run_def_cache_bm2
from def_cache_bm3 import run_def_cache_bm3
#from def_cache_bm4 import run_def_cache_bm4
from def_cache_bm5 import run_def_cache_bm5

from miss_cache_bm1 import run_miss_cache_bm1
from miss_cache_bm2 import run_miss_cache_bm2
from miss_cache_bm3 import run_miss_cache_bm3
#from miss_cache_bm4 import run_miss_cache_bm4
from miss_cache_bm5 import run_miss_cache_bm5

from vic_cache_bm1 import run_vic_cache_bm1
from vic_cache_bm2 import run_vic_cache_bm2
from vic_cache_bm3 import run_vic_cache_bm3
#from vic_cache_bm4 import run_vic_cache_bm4
from vic_cache_bm5 import run_vic_cache_bm5


from cd import collectData
from plot import plotData

changeDirectory("/home/viraj/Documents/SimpleScalar/simplesim-alpha/results")
filelist = listdir("/home/viraj/Documents/SimpleScalar/simplesim-alpha/results")
for f in filelist:
	remove(f)

changeDirectory("/home/viraj/Documents/SimpleScalar/simplesim-alpha")

run_def_cache_bm1()
run_def_cache_bm2()
run_def_cache_bm3()
#run_def_cache_bm4()
run_def_cache_bm5()

run_miss_cache_bm1()
run_miss_cache_bm2()
run_miss_cache_bm3()
#run_miss_cache_bm4()
run_miss_cache_bm5()

run_vic_cache_bm1()
run_vic_cache_bm2()
run_vic_cache_bm3()
#run_vic_cache_bm4()
run_vic_cache_bm5()

print ('Benchmarking complete!')

collectData()
plotData()
