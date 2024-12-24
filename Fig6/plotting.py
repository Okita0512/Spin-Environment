import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
from matplotlib.pyplot import MultipleLocator, tick_params

# exponential decay basis for TCF, used in plotting
def fit_p(x,etal,expn):
    f = np.zeros_like(x,dtype=complex)
    for k in range(len(etal)):
        f += etal[k]*np.exp(-expn[k]*x)
    return f

# FT for exponential decay basis for correlation spectrum, used in plotting
def C_w_fit(x,etal,expn):
    f = np.zeros_like(x, dtype=complex)
    for k in range(len(etal)):
        f += etal[k]/(expn[k]-1j*x)
    return f

# ==============================================================================================

t_0 = np.linspace(0, 20, 10001)
fft_t = np.loadtxt("fft_t", dtype = float)
fft_ct = np.loadtxt("fft_ct", dtype = complex)

etal2 = np.loadtxt("etal_2", dtype = complex)
expn2 = np.loadtxt("expn_2", dtype = complex)
etal3 = np.loadtxt("etal_3", dtype = complex)
expn3 = np.loadtxt("expn_3", dtype = complex)
etal4 = np.loadtxt("etal_4", dtype = complex)
expn4 = np.loadtxt("expn_4", dtype = complex)
etal5 = np.loadtxt("etal_5", dtype = complex)
expn5 = np.loadtxt("expn_5", dtype = complex)

# ==============================================================================================

lw = 2.0
legendsize = 32         # size for legend
font_legend = {'family':'Times New Roman', 'weight': 'roman', 'size':18}

color1 = 'purple'
color2 = 'green'
color3 = 'red'
color4 = 'navy'
color5 = 'black'

unitlen = 6
fig = plt.figure(figsize=(2 * unitlen, 2 * unitlen), dpi = 512)

# ==============================================================================================
#                                      Fig S1a    
# ==============================================================================================

plt.subplot(2,2,1)
plt.plot(t_0, fit_p(t_0, etal2, expn2).real, linewidth = lw, color = color1, label = "$t$-PFD = 2 + 2")
plt.plot(t_0, fit_p(t_0, etal3, expn3).real, linewidth = lw, color = color2, label = "$t$-PFD = 3 + 3")
plt.plot(t_0, fit_p(t_0, etal4, expn4).real, linewidth = lw, color = color3, label = "$t$-PFD = 4 + 4")
plt.plot(t_0, fit_p(t_0, etal5, expn5).real, linewidth = lw, color = color4, label = "$t$-PFD = 5 + 5")
plt.plot(fft_t, np.real(fft_ct), ls='--', linewidth = lw, color = color5, label = "exact")
plt.legend(frameon = False)

origin = -0.5
time = 15.0
y1, y2 = -1.0, 7.0     # y-axis range: (y1, y2)
# scale for major and minor locator
x_major_locator = MultipleLocator(5)
x_minor_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(2)
y_minor_locator = MultipleLocator(1)

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
plt.xlim(origin, time)
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
ax.set_ylabel('Re[C(t)]', font = 'Times New Roman', size = 18)
ax.legend(loc = 'upper center', frameon = False, prop = font_legend)
plt.legend(title = '(a)', frameon = False, title_fontsize = legendsize)

# ==============================================================================================
#                                      Fig S1b    
# ==============================================================================================

plt.subplot(2,2,2)
plt.plot(t_0, fit_p(t_0, etal2, expn2).imag, linewidth = lw, color = color1, label = "$t$-PFD = 2 + 2")
plt.plot(t_0, fit_p(t_0, etal3, expn3).imag, linewidth = lw, color = color2, label = "$t$-PFD = 3 + 3")
plt.plot(t_0, fit_p(t_0, etal4, expn4).imag, linewidth = lw, color = color3, label = "$t$-PFD = 4 + 4")
plt.plot(t_0, fit_p(t_0, etal5, expn5).imag, linewidth = lw, color = color4, label = "$t$-PFD = 5 + 5")
plt.plot(fft_t, np.imag(fft_ct), ls='--', linewidth = lw, color = color5, label = "exact")
plt.legend(frameon = False)

y1, y2 = -3.5, 1.0     # y-axis range: (y1, y2)

# scale for major and minor locator
x_major_locator = MultipleLocator(5)
x_minor_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(2)
y_minor_locator = MultipleLocator(1)

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
plt.xlim(origin, time)
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
ax.set_ylabel('Im[C(t)]', font = 'Times New Roman', size = 18)
ax.legend(loc = 'lower center', frameon = False, prop = font_legend)
plt.legend(title = '(b)', frameon = False, title_fontsize = legendsize)

# ==============================================================================================
# ==============================================================================================

color5 = 'black'
color1 = 'purple'
color2 = 'green'
color3 = 'red'
color4 = 'navy'

fft_t_h = np.loadtxt("fft_t_4_0.5", dtype = float)
fft_ct_h = np.loadtxt("fft_ct_4_0.5", dtype = complex)
fft_t_1 = np.loadtxt("fft_t_4_1", dtype = float)
fft_ct_1 = np.loadtxt("fft_ct_4_1", dtype = complex)
fft_t_2 = np.loadtxt("fft_t_4_2", dtype = float)
fft_ct_2 = np.loadtxt("fft_ct_4_2", dtype = complex)
fft_t_5 = np.loadtxt("fft_t_4_5", dtype = float)
fft_ct_5 = np.loadtxt("fft_ct_4_5", dtype = complex)

etal4_h = np.loadtxt("etal_4_0.5", dtype = complex)
expn4_h = np.loadtxt("expn_4_0.5", dtype = complex)
etal4_1 = np.loadtxt("etal_4_1", dtype = complex)
expn4_1 = np.loadtxt("expn_4_1", dtype = complex)
etal4_2 = np.loadtxt("etal_4_2", dtype = complex)
expn4_2 = np.loadtxt("expn_4_2", dtype = complex)
etal4_5 = np.loadtxt("etal_4_5", dtype = complex)
expn4_5 = np.loadtxt("expn_4_5", dtype = complex)

# ==============================================================================================
#                                      Fig S1c    
# ==============================================================================================

plt.subplot(2,2,3)
plt.plot(t_0, fit_p(t_0, etal5, expn5).real, linewidth = lw, color = color5, label = "$\mathrm{T = 0}$")
plt.plot(fft_t, np.real(fft_ct), ls='--', linewidth = lw, color = color5)
plt.plot(t_0, fit_p(t_0, etal4_h, expn4_h).real, linewidth = lw, color = color1, label = "$\mathrm{k_B T / Δ = 0.5}$")
plt.plot(fft_t_h, np.real(fft_ct_h), ls='--', linewidth = lw, color = color1)
plt.plot(t_0, fit_p(t_0, etal4_1, expn4_1).real, linewidth = lw, color = color2, label = "$\mathrm{k_B T / Δ = 1}$")
plt.plot(fft_t_1, np.real(fft_ct_1), ls='--', linewidth = lw, color = color2)
plt.plot(t_0, fit_p(t_0, etal4_2, expn4_2).real, linewidth = lw, color = color3, label = "$\mathrm{k_B T / Δ = 2}$")
plt.plot(fft_t_2, np.real(fft_ct_2), ls='--', linewidth = lw, color = color3)
plt.plot(t_0, fit_p(t_0, etal4_5, expn4_5).real, linewidth = lw, color = color4, label = "$\mathrm{k_B T / Δ = 5}$")
plt.plot(fft_t_5, np.real(fft_ct_5), ls='--', linewidth = lw, color = color4)
plt.legend(frameon = False)

y1, y2 = -1.0, 7.0     # y-axis range: (y1, y2)

# scale for major and minor locator
x_major_locator = MultipleLocator(5)
x_minor_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(2)
y_minor_locator = MultipleLocator(1)

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
plt.xlim(origin, time)
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
ax.set_ylabel('Re[C(t)]', font = 'Times New Roman', size = 18)
ax.legend(loc = 'upper center', frameon = False, prop = font_legend)
plt.legend(title = '(c)', frameon = False, title_fontsize = legendsize)

# ==============================================================================================
#                                      Fig S1d    
# ==============================================================================================

plt.subplot(2,2,4)
plt.plot(t_0, fit_p(t_0, etal5, expn5).imag, linewidth = lw, color = color5, label = "$\mathrm{T = 0}$")
plt.plot(fft_t, np.imag(fft_ct), ls='--', linewidth = lw, color = color5)
plt.plot(t_0, fit_p(t_0, etal4_h, expn4_h).imag, linewidth = lw, color = color1, label = "$\mathrm{k_B T / Δ = 0.5}$")
plt.plot(fft_t_h, np.imag(fft_ct_h), ls='--', linewidth = lw, color = color1)
plt.plot(t_0, fit_p(t_0, etal4_1, expn4_1).imag, linewidth = lw, color = color2, label = "$\mathrm{k_B T / Δ = 1}$")
plt.plot(fft_t_1, np.imag(fft_ct_1), ls='--', linewidth = lw, color = color2)
plt.plot(t_0, fit_p(t_0, etal4_2, expn4_2).imag, linewidth = lw, color = color3, label = "$\mathrm{k_B T / Δ = 2}$")
plt.plot(fft_t_2, np.imag(fft_ct_2), ls='--', linewidth = lw, color = color3)
plt.plot(t_0, fit_p(t_0, etal4_5, expn4_5).imag, linewidth = lw, color = color4, label = "$\mathrm{k_B T / Δ = 5}$")
plt.plot(fft_t_5, np.imag(fft_ct_5), ls='--', linewidth = lw, color = color4)
plt.legend(frameon = False)

y1, y2 = -3.5, 1.0     # y-axis range: (y1, y2)

# scale for major and minor locator
x_major_locator = MultipleLocator(5)
x_minor_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(2)
y_minor_locator = MultipleLocator(1)

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
plt.xlim(origin, time)
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
ax.set_ylabel('Im[C(t)]', font = 'Times New Roman', size = 18)
ax.legend(loc = 'lower center', frameon = False, prop = font_legend)
plt.legend(title = '(d)', frameon = False, title_fontsize = legendsize)

# plt.show()
plt.savefig("figure_6.pdf", bbox_inches='tight')

