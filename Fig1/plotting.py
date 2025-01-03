import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
from matplotlib.pyplot import MultipleLocator, tick_params

lw = 2.0
legendsize = 32         # size for legend
font_legend = {'family':'Times New Roman', 'weight': 'roman', 'size':18}
color1 = 'black'            # 
color2 = 'r'


# ==============================================================================================
#                                      Fig 1a    
# ==============================================================================================

Unitlen = 5
fig = plt.figure(figsize=(3.5 * Unitlen, 2 * Unitlen), dpi = 512)

plt.subplot(2, 3, 1)        # corresponds to Fig 1a in Ref

data = np.loadtxt("a.dat", dtype = float)
A, = plt.plot(data[:,0], data[:,1] - data[:,2], "-", linewidth = lw, color = color1, label = "DEOM")

data2 = np.loadtxt("a.txt", dtype = float)
B, = plt.plot(data2[:,0], data2[:,1], ".", color = color2, label = "ML-MCTDH")

# ==============================================================================================

time = 40.0             # x-axis range: (0, time)
y1, y2 = -1.0, 1.0     # y-axis range: (y1, y2)

# scale for major and minor locator
x_major_locator = MultipleLocator(10)
x_minor_locator = MultipleLocator(2)
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
ax.legend(handles = [A, B], loc = 'upper center', frameon = True, prop = font_legend) # lower right
plt.legend(title = '(a)', frameon = False, title_fontsize = legendsize)

# ==============================================================================================
#                                      Fig 1b     
# ==============================================================================================

plt.subplot(2, 3, 2)

data = np.loadtxt("b.dat", dtype = float)
A, = plt.plot(data[:,0], data[:,1] - data[:,2], "-", linewidth = lw, color = color1, label = "DEOM")

data = np.loadtxt("b.txt", dtype = float)
B, = plt.plot(data[:,0], data[:,1], ".", color = color2, label = "ML-MCTDH")

# ==============================================================================================

time = 20.0             # x-axis range: (0, time)
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

plt.legend(title = '(b)', frameon = False, title_fontsize = legendsize)

# ==============================================================================================
#                                      Fig 1c 
# ==============================================================================================

plt.subplot(2, 3, 3)

data = np.loadtxt("c.dat", dtype = float)
A, = plt.plot(data[:,0], data[:,1] - data[:,2], "-", linewidth = lw, color = color1, label = "DEOM")

data = np.loadtxt("c.txt", dtype = float)
B, = plt.plot(data[:,0], data[:,1], ".", color = color2, label = "ML-MCTDH")

# ==============================================================================================

time = 30.0             # x-axis range: (0, time)
y1, y2 = -0.7, 1.0     # y-axis range: (y1, y2)

# scale for major and minor locator
x_major_locator = MultipleLocator(10)
x_minor_locator = MultipleLocator(2)
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

plt.legend(title = '(c)', frameon = False, title_fontsize = legendsize)

# ==============================================================================================
#                                      Fig 1d    
# ==============================================================================================

plt.subplot(2, 3, 4)        # corresponds to Fig 1a in Ref

data = np.loadtxt("d.dat", dtype = float)
A, = plt.plot(data[:,0], data[:,1] - data[:,2], "-", linewidth = lw, color = color1, label = "DEOM")

data = np.loadtxt("d.txt", dtype = float)
B, = plt.plot(data[:,0], data[:,1], ".", color = color2, label = "ML-MCTDH")

# ==============================================================================================

time = 40.0             # x-axis range: (0, time)
y1, y2 = -0.1, 1.0     # y-axis range: (y1, y2)

# scale for major and minor locator
x_major_locator = MultipleLocator(10)
x_minor_locator = MultipleLocator(2)
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

plt.legend(title = '(d)', frameon = False, title_fontsize = legendsize)

# ==============================================================================================
#                                      Fig 1e     
# ==============================================================================================

plt.subplot(2, 3, 5)

data = np.loadtxt("e.dat", dtype = float)
A, = plt.plot(data[:,0], data[:,1] - data[:,2], "-", linewidth = lw, color = color1, label = "DEOM")

data = np.loadtxt("e.txt", dtype = float)
B, = plt.plot(data[:,0], data[:,1], ".", color = color2, label = "ML-MCTDH")

# ==============================================================================================

time = 40.0             # x-axis range: (0, time)
y1, y2 = 0.0, 1.0     # y-axis range: (y1, y2)

# scale for major and minor locator
x_major_locator = MultipleLocator(10)
x_minor_locator = MultipleLocator(2)
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

plt.legend(title = '(e)', frameon = False, title_fontsize = legendsize)

# ==============================================================================================
#                                      Fig 1c 
# ==============================================================================================

plt.subplot(2, 3, 6)

data = np.loadtxt("f.dat", dtype = float)
A, = plt.plot(data[:,0], data[:,1] - data[:,2], "-", linewidth = lw, color = color1, label = "DEOM")

data = np.loadtxt("f.txt", dtype = float)
B, = plt.plot(data[:,0], data[:,1], ".", color = color2, label = "ML-MCTDH")

# ==============================================================================================

time = 40.0             # x-axis range: (0, time)
y1, y2 = -0.1, 1.0     # y-axis range: (y1, y2)

# scale for major and minor locator
x_major_locator = MultipleLocator(10)
x_minor_locator = MultipleLocator(2)
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

plt.legend(title = '(f)', frameon = False, title_fontsize = legendsize)

plt.savefig("figure_1.pdf", bbox_inches='tight')
#plt.show()
