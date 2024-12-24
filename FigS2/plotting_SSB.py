import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots() # 创建图实例
from matplotlib.pyplot import MultipleLocator, tick_params
plt.rcParams['font.family'] = 'DeJavu Serif'
plt.rcParams["font.family"] = "Helvetica"

lw = 2.5
legendsize = 32         # size for legend
font_legend = {'weight': 'roman', 'size':18}
color1 = 'red'            # 
color2 = 'navy'


# ==============================================================================================
#                                      Fig 1a    
# ==============================================================================================

Unitlen = 5
fig, ax = plt.subplots(1, 3, figsize=(3.5 * Unitlen, 1 * Unitlen), dpi = 512, sharex = 'all')
fig.subplots_adjust(hspace = 0, wspace = 0.2)

ax1 = plt.subplot(1, 3, 1)        # corresponds to Fig 1a in Ref

data = np.loadtxt("DEOM_alpha=0.1.dat", dtype = float)
A, = plt.plot(data[:,0], data[:,1] - data[:,7], "-", linewidth = lw, color = color1, label = r"DEOM")

data2 = np.loadtxt("TCL2_alpha=0.1.txt", dtype = float)
B, = plt.plot(data2[:,0], data2[:,1] - data2[:,7], "--", linewidth = lw, color = color2, label = r"TCL-2")

# plt.text(9, 0.65, r"$\alpha = 0.1$", fontdict = font_legend)
# ==============================================================================================

time = 15.0             # x-axis range: (0, time)
y1, y2 = -0.1, 1.0     # y-axis range: (y1, y2)

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

plt.tick_params('x', labelsize = 20, which = 'both', direction = 'in')
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
ax.set_xlabel('tΔ', font = 'Times New Roman', size = 18)
ax.set_ylabel('P(t)', size = 18) # , font = 'Times New Roman'

# legend location, font & markersize
ax.legend(handles = [A, B], loc = 'lower right', frameon = False, prop = font_legend) # lower right
plt.legend(title = '(a)', frameon = False, title_fontsize = legendsize)

# ==============================================================================================
#                                      Fig 1b     
# ==============================================================================================

ax2 = plt.subplot(1, 3, 2)

data = np.loadtxt("DEOM_alpha=0.2.dat", dtype = float)
A, = plt.plot(data[:,0], data[:,1] - data[:,7], "-", linewidth = lw, color = color1, label = r"DEOM")

data2 = np.loadtxt("TCL2_alpha=0.2.txt", dtype = float)
B, = plt.plot(data2[:,0], data2[:,1] - data2[:,7], "--", linewidth = lw, color = color2, label = r"TCL-2")

# plt.text(9, 0.65, r"$\alpha = 0.2$", fontdict = font_legend)
# ==============================================================================================

time = 15.0             # x-axis range: (0, time)
y1, y2 = -0.1, 1.0     # y-axis range: (y1, y2)

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

plt.tick_params('x', labelsize = 20, which = 'both', direction = 'in')
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
ax.set_xlabel('tΔ', font = 'Times New Roman', size = 18)

# ax.legend(handles = [A, B], loc = 'lower right', frameon = False, prop = font_legend) # lower right
plt.legend(title = '(b)', frameon = False, title_fontsize = legendsize)

# ==============================================================================================
#                                      Fig 1c 
# ==============================================================================================

ax3 = plt.subplot(1, 3, 3)

data = np.loadtxt("DEOM_alpha=0.4.dat", dtype = float)
A, = plt.plot(data[:,0], data[:,1] - data[:,7], "-", linewidth = lw, color = color1, label = r"DEOM")

data2 = np.loadtxt("TCL2_alpha=0.4.txt", dtype = float)
B, = plt.plot(data2[:,0], data2[:,1] - data2[:,7], "--", linewidth = lw, color = color2, label = r"TCL-2")

# plt.text(9, 0.65, r"$\alpha = 0.4$", fontdict = font_legend)
# ==============================================================================================

time = 15.0             # x-axis range: (0, time)
y1, y2 = -0.1, 1.0     # y-axis range: (y1, y2)

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

plt.tick_params('x', labelsize = 20, which = 'both', direction = 'in')
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
ax.set_xlabel('tΔ', font = 'Times New Roman', size = 18)

# ax.legend(handles = [A, B], loc = 'lower right', frameon = False, prop = font_legend) # lower right
plt.legend(title = '(c)', frameon = False, title_fontsize = legendsize)



plt.savefig("figure_S2.pdf", bbox_inches='tight')
#plt.show()