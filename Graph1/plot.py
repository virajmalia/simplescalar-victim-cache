#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import cd
import fileinput
from matplotlib.ticker import FormatStrFormatter

def plotData():
	N = 4
	ind = np.arange(N)  # the x locations for the groups
	width = 0.3       # the width of the bars
	parameter = []
	dc_value = []
	mc_value = []
	vc_value = []
	title = []
	sim_type = []
	with open('/home/viraj/Documents/Graph1/data.out', 'r') as f:
		for num, line in enumerate(f,0):
			if "," in line:
				sim,param,val,desc = line.split(",", 3)
				sim_type.append(sim)			
			if (sim == 'sim_dc1.out' or sim == 'sim_dc2.out' or sim == 'sim_dc3.out' or sim == 'sim_dc5.out'):# or sim == 'sim_dc4' ):
				dc_value.append(int(val))
			if (sim == 'sim_mc1.out' or sim == 'sim_mc2.out' or sim == 'sim_mc3.out' or sim == 'sim_mc5.out'):# or sim == 'sim_mc4' ):
				mc_value.append(int(val))
			if (sim == 'sim_vc1.out' or sim == 'sim_vc2.out' or sim == 'sim_vc3.out' or sim == 'sim_vc5.out'):# or sim == 'sim_mc4'):
				vc_value.append(int(val))
		parameter.append(param)
		title.append(desc)

	fig, (ax1,ax2) = plt.subplots(2,1,sharex = True)
	#ax1.yaxis.set_major_formatter(FormatStrFormatter('%d',useOffset=True))
	#ax2.yaxis.set_major_formatter(FormatStrFormatter('%d',useOffset=True))

	defaultCache = ax1.bar(ind, dc_value, width, color='r')
	missBuffer = ax1.bar(ind + width, mc_value, width, color='y')
	victimCache = ax1.bar(ind + 2*width, vc_value, width, color='b')
	
	defaultCache = ax2.bar(ind, dc_value, width, color='r')
	missBuffer = ax2.bar(ind + width, mc_value, width, color='y')
	victimCache = ax2.bar(ind + 2*width, vc_value, width, color='b')

	ax1.set_ylim(5000, 14000000)  # Top
	ax2.set_ylim(0, 5000)  # Bottom

	ax1.spines['bottom'].set_visible(False)
	ax2.spines['top'].set_visible(False)
	ax1.xaxis.tick_top()
	ax1.tick_params(labeltop='off')  # don't put tick labels at the top
	ax2.xaxis.tick_bottom()

# Make diagonals at Ticks
	d = .015  # how big to make the diagonal lines in axes coordinates
	# arguments to pass plot, just so we don't keep repeating them
	kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
	ax1.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
	ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

	kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
	ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
	ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

	
	ax1.set_title(title[0])
	ax2.set_xticks(ind + width)
	ax2.set_xticklabels(('CC1', 'Anagram', 'Compress95', 'Perl'))
	ax1.legend((defaultCache[0], missBuffer[0], victimCache[0]), ('Default Cache', 'Miss Buffer', 'Victim Cache'))


	def autolabel(rects):
	    # attach some text labels
		for rect in rects:
			height = rect.get_height()
			ax1.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%d' % int(height),ha='center', va='bottom')
			ax2.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%d' % int(height),ha='center', va='bottom')

	autolabel(defaultCache)
	autolabel(missBuffer)
	autolabel(victimCache)

	plt.show()
