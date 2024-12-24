import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()

# ==============================================================================================
#                                         data reading     
# ==============================================================================================

# 创建画布
fig = plt.figure(figsize=(8, 6), dpi = 256)
lwid = 1.8


# ==============================================================================================

data = np.loadtxt("0.dat", dtype = float)
plt.plot(data[:,0], data[:,1] - data[:,2], ls = "-", color = 'black', label = '$\mathrm{k_B T = 0}$', linewidth = lwid)

data = np.loadtxt("1.dat", dtype = float)
plt.plot(data[:,0], data[:,1] - data[:,2], ls = "--", color = 'black', label = 'test', linewidth = lwid)

data2 = np.loadtxt("0.txt", dtype = float)
plt.plot(data2[:,0], data2[:,1], "o", color = 'black')

data3 = np.loadtxt("0.1.dat", dtype = float)
plt.plot(data3[:,0], data3[:,1] - data3[:,2], ls = "-", color = 'purple', label = '$\mathrm{k_B T/Δ = 0.1}$', linewidth = lwid)

data3 = np.loadtxt("2.dat", dtype = float)
plt.plot(data3[:,0], data3[:,1] - data3[:,2], ls = "--", color = 'purple', label = 'test', linewidth = lwid)

data4 = np.loadtxt("0.1.txt", dtype = float)
plt.plot(data4[:,0], data4[:,1], "o", color = 'purple')

data5 = np.loadtxt("0.167.dat", dtype = float)
plt.plot(data5[:,0], data5[:,1] - data5[:,2], ls = "-", color = 'green', label = '$\mathrm{k_B T/Δ = 0.167}$', linewidth = lwid)

data5 = np.loadtxt("3.dat", dtype = float)
plt.plot(data5[:,0], data5[:,1] - data5[:,2], ls = "--", color = 'green', label = 'test', linewidth = lwid)

data6 = np.loadtxt("0.167.txt", dtype = float)
plt.plot(data6[:,0], data6[:,1], "o", color = 'green')

# data7 = np.loadtxt("0.25.dat", dtype = float)
# plt.plot(data7[:,0], data7[:,1] - data7[:,2], ls = "-", color = 'red', label = '$\mathrm{k_B T/Δ = 0.25}$', linewidth = lwid)
# 
# data8 = np.loadtxt("0.25.txt", dtype = float)
# plt.plot(data8[:,0], data8[:,1], "o", color = 'red')
# 
# data9 = np.loadtxt("0.5.dat", dtype = float)
# plt.plot(data9[:,0], data9[:,1] - data9[:,2], ls = "-", color = 'navy', label = '$\mathrm{k_B T/Δ = 0.5}$', linewidth = lwid)
# 
# data0 = np.loadtxt("0.5.txt", dtype = float)
# plt.plot(data0[:,0], data0[:,1], "o", color = 'navy')

# ==============================================================================================
#                                      plotting set up     
# ==============================================================================================

time = 40.0             # x-axis range: (0, time)
y1, y2 = -0.2, 1.0     # y-axis range: (y1, y2)

# ==============================================================================================

from matplotlib.pyplot import MultipleLocator, tick_params
font_L = {'family':'Times New Roman', 'weight': 'roman', 'size': 18}

# scale for major and minor locator
x_major_locator = MultipleLocator(10)
x_minor_locator = MultipleLocator(2)
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
ax.set_ylabel('P(t)', font = 'Times New Roman', size = 18)
# ax.set_title('Spin Bath 3', font = 'Times New Roman', size = 18)

# legend location, font & markersize
ax.legend(loc = 'upper right', prop = font_L, markerscale = 1, frameon = False)
# plt.legend()

plt.savefig("figure1.png")

#plt.show()