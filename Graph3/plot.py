#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import cd
import fileinput
from matplotlib.ticker import FormatStrFormatter

def plotData():
	N = 5
	ind = np.arange(N)  # the x locations for the groups
	width = 0.3       # the width of the bars
	parameter = []
	dc_value = []	
	mc_value = []
	plot_value = []
	title = []
	sim_type = []
	with open('/home/viraj/Documents/Graph3/data.out', 'r') as f:
		for num, line in enumerate(f,0):
			if "," in line:
				sim,param,val,desc = line.split(",", 3)
				sim_type.append(sim)	
			if (sim == 'sim_dc1.out'):
				dc_value.append(int(val))
				for i in range(1,5):
					dc_value.append(int(val))
			if (sim == 'sim_vc1.out' or sim == 'sim_vc2.out' or sim == 'sim_vc4.out' or sim == 'sim_vc8.out' or sim == 'sim_vc16.out'):
				mc_value.append(int(val))
		parameter.append(param)
		title.append(desc)
	#print(dc_value)
	#print(mc_value)
	fig, (ax) = plt.subplots()
	#ax1.yaxis.set_major_formatter(FormatStrFormatter('%d',useOffset=True))
	#ax2.yaxis.set_major_formatter(FormatStrFormatter('%d',useOffset=True))
	plot_value = np.array(dc_value) - np.array(mc_value)
	missBuffer = ax.bar(ind + width, plot_value, width, color='y')
	
	ax.set_title('Reduction in number of ul2 accesses for Victim Cache ' + str(dc_value[0]))
	ax.set_xticks(ind + width)
	ax.set_xticklabels(('1','2','4','8','16'))
	#ax1.legend((defaultCache[0], missBuffer[0], victimCache[0]), ('Default Cache', 'Miss Buffer', 'Victim Cache'))


	def autolabel(rects):
	    # attach some text labels
		for rect in rects:
			height = rect.get_height()
			ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%d' % int(height),ha='center', va='bottom')

	autolabel(missBuffer)
	plt.show()
