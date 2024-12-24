import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots() # 创建图实例

# ==============================================================================================
#                                         data reading     
# ==============================================================================================

Ref = "MCTDH.txt"


# ==============================================================================================

data2 = np.loadtxt("prop-rho.dat", dtype = float) # _M1_focused
plt.plot(data2[:,0], (data2[:,1] - data2[:,2]), "k-", color = 'red', label = "dt = 0.001, ferr = 1e-5", linewidth = 1.5)

#data2 = np.loadtxt("1e-4.dat", dtype = float) # _M1_focused
#plt.plot(data2[:,0], (data2[:,1] - data2[:,2]), "k-", color = 'green', label = "dt = 0.0002, ferr = 1e-4", linewidth = 1.5)

data = np.loadtxt(Ref, dtype = float)
plt.plot(data[:,0], data[:,1], "k.", color = 'navy', label = "ML-MCTDH")

# ==============================================================================================
#                                      plotting set up     
# ==============================================================================================

time = 4.0             # x-axis range: (0, time)
y1, y2 = 0.0, 1.0     # y-axis range: (y1, y2)

# ==============================================================================================

from matplotlib.pyplot import MultipleLocator, tick_params
font = {'family':'Times New Roman', 'weight': 'roman', 'size':12}

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
ax.set_xlabel('time / a.u.', font = 'Times New Roman', size = 18)
ax.set_ylabel('P1 - P2', font = 'Times New Roman', size = 18)
# ax.set_title('Spin Bath 1', font = 'Times New Roman', size = 18)
ax.set_title('Spin Bath 2', font = 'Times New Roman', size = 18)

# legend location, font & markersize
ax.legend(loc = 'upper right', prop = font, markerscale = 1)
plt.legend()

plt.show()