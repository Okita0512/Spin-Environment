import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
from matplotlib.pyplot import MultipleLocator, tick_params

# ==============================================================================================
#                                         data reading     
# ==============================================================================================

lw = 2.0
Ref = "MCTDH.txt"
legendsize = 32         # size for legend
font_legend = {'family':'Times New Roman', 'weight': 'roman', 'size':18}

# ==============================================================================================
fig = plt.figure(figsize=(8, 6), dpi = 512)

data2 = np.loadtxt("2+2_nofilter_lmax=45.dat", dtype = float)
plt.plot(data2[:,0], (data2[:,1] - data2[:,2]), "--", color = 'green', label = "Bath terms = 4,   CPU time: 3 min", linewidth = lw)

data2 = np.loadtxt("3+3_nofilter_lmax=45.dat", dtype = float)
plt.plot(data2[:,0], (data2[:,1] - data2[:,2]), "--", color = 'blue', label = "Bath terms = 6,   CPU time: 180 min", linewidth = lw)

data2 = np.loadtxt("4+4_nofilter_lmax=45.dat", dtype = float)
plt.plot(data2[:,0], (data2[:,1] - data2[:,2]), "-", color = 'black', label = "Bath terms = 8,   CPU time: 6800 min", linewidth = lw)

data = np.loadtxt(Ref, dtype = float)
plt.plot(data[:,0], data[:,1], ".", color = 'red', label = "ML-MCTDH")

# ==============================================================================================
#                                      plotting set up     
# ==============================================================================================

time = 7.0             # x-axis range: (0, time)
y1, y2 = 0.5, 1.0     # y-axis range: (y1, y2)

# ==============================================================================================

# scale for major and minor locator
x_major_locator = MultipleLocator(2)
x_minor_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(0.1)
y_minor_locator = MultipleLocator(0.05)

# x-axis and LHS y-axis
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.xaxis.set_minor_locator(x_minor_locator)
ax.yaxis.set_major_locator(y_major_locator)
ax.yaxis.set_minor_locator(y_minor_locator)
ax.tick_params(which = 'major', length = 8, labelsize = 10)
ax.tick_params(which = 'minor', length = 4)

x1_label = ax.get_xticklabels()
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
y1_label = ax.get_yticklabels()
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]

plt.tick_params(labelsize = 20, which = 'both', direction = 'in')
plt.xlim(0.0, time)
plt.ylim(y1, y2)

# RHS y-axis
ax2 = ax.twinx()
ax2.yaxis.set_major_locator(y_major_locator)
ax2.yaxis.set_minor_locator(y_minor_locator)
ax2.tick_params(which = 'major', length = 8)
ax2.tick_params(which = 'minor', length = 4)
ax2.axes.yaxis.set_ticklabels([])

plt.tick_params(which = 'both', direction = 'in')
plt.ylim(y1, y2)

# name of x, y axis and the panel
ax.set_xlabel('tΔ', font = 'Times New Roman', size = 18)
ax.set_ylabel('P(t)', font = 'Times New Roman', size = 18)

# legend location, font & markersize
ax.legend(loc = 'upper center', prop = font_legend, markerscale = 1, frameon = False)

plt.savefig("Spin_boson_0K.pdf", bbox_inches='tight')
# plt.show()