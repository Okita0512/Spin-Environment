import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots() # 创建图实例
from matplotlib.pyplot import MultipleLocator, tick_params

lw = 2.5
legendsize = 32         # size for legend
font_legend = {'family':'Times New Roman', 'weight': 'roman', 'size':18}
color1 = 'red'            # 
color2 = 'navy'


# ==============================================================================================
#                                      Fig 1a    
# ==============================================================================================

Unitlen = 5
fig, ax = plt.subplots(2, 3, figsize=(3.5 * Unitlen, 2 * Unitlen), dpi = 512, sharex = 'all')
fig.subplots_adjust(hspace = 0, wspace = 0.2)

ax1 = plt.subplot(2, 3, 1)        # corresponds to Fig 1a in Ref

data = np.loadtxt("1_SSB.dat", dtype = float)
A, = plt.plot(data[:,0], data[:,1] - data[:,4], "-", linewidth = lw, color = color1, label = "SSB")

data2 = np.loadtxt("1_SBB.dat", dtype = float)
B, = plt.plot(data2[:,0], data2[:,1] - data2[:,2], "-", linewidth = lw, color = color2, label = "spin-boson")

# ==============================================================================================

time = 15.0             # x-axis range: (0, time)
y1, y2 = -0.4, 1.0     # y-axis range: (y1, y2)

# scale for major and minor locator
x_major_locator = MultipleLocator(5)
x_minor_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(0.5)
y_minor_locator = MultipleLocator(0.1)

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

plt.tick_params('x', labelsize = 0, which = 'both', direction = 'in')
plt.tick_params('y', labelsize = 20, which = 'both', direction = 'in')
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
# ax.set_xlabel('tΔ', font = 'Times New Roman', size = 18)
ax.set_ylabel('P(t)', size = 18) # , font = 'Times New Roman'

# legend location, font & markersize
ax.legend(handles = [A, B], loc = 'upper center', frameon = False, prop = font_legend) # lower right
plt.legend(title = '(a)', frameon = False, title_fontsize = legendsize)

# ==============================================================================================
#                                      Fig 1b     
# ==============================================================================================

ax2 = plt.subplot(2, 3, 2)

data = np.loadtxt("2_SSB.dat", dtype = float)
A, = plt.plot(data[:,0], data[:,1] - data[:,4], "-", linewidth = lw, color = color1, label = "SSB")

data2 = np.loadtxt("2_SBB.dat", dtype = float)
B, = plt.plot(data2[:,0], data2[:,1] - data2[:,2], "-", linewidth = lw, color = color2, label = "spin-boson")

# ==============================================================================================

time = 15.0             # x-axis range: (0, time)
y1, y2 = -1.0, 1.0     # y-axis range: (y1, y2)

# scale for major and minor locator
x_major_locator = MultipleLocator(5)
x_minor_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(0.5)
y_minor_locator = MultipleLocator(0.1)

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

plt.tick_params('x', labelsize = 0, which = 'both', direction = 'in')
plt.tick_params('y', labelsize = 20, which = 'both', direction = 'in')
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
# ax.set_xlabel('tΔ', font = 'Times New Roman', size = 18)

plt.legend(title = '(b)', frameon = False, title_fontsize = legendsize)

# ==============================================================================================
#                                      Fig 1c 
# ==============================================================================================

ax3 = plt.subplot(2, 3, 3)

data = np.loadtxt("3_SSB.dat", dtype = float)
A, = plt.plot(data[:,0], data[:,1] - data[:,4], "-", linewidth = lw, color = color1, label = "SSB")

data2 = np.loadtxt("3_SBB.dat", dtype = float)
B, = plt.plot(data2[:,0], data2[:,1] - data2[:,2], "-", linewidth = lw, color = color2, label = "spin-boson")

# ==============================================================================================

time = 15.0             # x-axis range: (0, time)
y1, y2 = -1.0, 1.0     # y-axis range: (y1, y2)

# scale for major and minor locator
x_major_locator = MultipleLocator(5)
x_minor_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(0.5)
y_minor_locator = MultipleLocator(0.1)

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

plt.tick_params('x', labelsize = 0, which = 'both', direction = 'in')
plt.tick_params('y', labelsize = 20, which = 'both', direction = 'in')
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
# ax.set_xlabel('tΔ', font = 'Times New Roman', size = 18)

plt.legend(title = '(c)', frameon = False, title_fontsize = legendsize)

# ==============================================================================================
#                                      Fig 1d    
# ==============================================================================================

plt.subplot(2, 3, 4)        # corresponds to Fig 1a in Ref

data = np.loadtxt("1_S_SSB.dat", dtype = float)
A, = plt.plot(data[:,0], data[:,1], "-", linewidth = lw, color = color1, label = "SSB")

data2 = np.loadtxt("1_S_SBB.dat", dtype = float)
B, = plt.plot(data2[:,0], data2[:,1], "-", linewidth = lw, color = color2, label = "spin-boson")
# ==============================================================================================

time = 15.0             # x-axis range: (0, time)
y1, y2 = 0.0, 0.75     # y-axis range: (y1, y2)

# scale for major and minor locator
x_major_locator = MultipleLocator(5)
x_minor_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(0.2)
y_minor_locator = MultipleLocator(0.1)

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
ax.set_ylabel('$S_\mathrm{vN}$(t)', size = 18) # , font = 'Times New Roman'

# plt.legend(title = '(d)', frameon = False, title_fontsize = legendsize)

# ==============================================================================================
#                                      Fig 1e     
# ==============================================================================================

plt.subplot(2, 3, 5)

data = np.loadtxt("2_S_SSB.dat", dtype = float)
A, = plt.plot(data[:,0], data[:,1], "-", linewidth = lw, color = color1, label = "SSB")

data2 = np.loadtxt("2_S_SBB.dat", dtype = float)
B, = plt.plot(data2[:,0], data2[:,1], "-", linewidth = lw, color = color2, label = "spin-boson")
# ==============================================================================================

time = 15.0             # x-axis range: (0, time)
y1, y2 = 0.0, 0.75     # y-axis range: (y1, y2)

# scale for major and minor locator
x_major_locator = MultipleLocator(5)
x_minor_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(0.2)
y_minor_locator = MultipleLocator(0.1)

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

# plt.legend(title = '(e)', frameon = False, title_fontsize = legendsize)

# ==============================================================================================
#                                      Fig 1c 
# ==============================================================================================

plt.subplot(2, 3, 6)

data = np.loadtxt("3_S_SSB.dat", dtype = float)
A, = plt.plot(data[:,0], data[:,1], "-", linewidth = lw, color = color1, label = "SSB")

data2 = np.loadtxt("3_S_SBB.dat", dtype = float)
B, = plt.plot(data2[:,0], data2[:,1], "-", linewidth = lw, color = color2, label = "spin-boson")
# ==============================================================================================

time = 15.0             # x-axis range: (0, time)
y1, y2 = 0.0, 0.75     # y-axis range: (y1, y2)

# scale for major and minor locator
x_major_locator = MultipleLocator(5)
x_minor_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(0.2)
y_minor_locator = MultipleLocator(0.1)

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

# plt.legend(title = '(f)', frameon = False, title_fontsize = legendsize)

plt.savefig("figure_4.pdf", bbox_inches='tight')
#plt.show()