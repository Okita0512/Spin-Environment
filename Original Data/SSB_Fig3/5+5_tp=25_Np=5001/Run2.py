import matplotlib.pyplot as plt
import numpy as np

# ======================================================================================
#                                   Global Setting
# ======================================================================================

# Ohmic-like Spectral density
def J_ohm(x, alpha, omega_c, s):
    return (np.pi / 2) * alpha * x**s * omega_c**(1-s) * np.exp(- x / omega_c) * np.heaviside(x, 0)

# ======================================================================================

class parameter:

    T = 0                               # temperature
    omega_c = 1                         # cutoff frequency
    s = 1                               # s = 1 for Ohmic, s < 1 for sub-Ohmic, s > 1 for super-Ohmic
    alpha = 0.5                          # coupling strength

    t_p = 20                            # the plateau time for TCF
    N_p = 10001                         # dimensionality for discretization, should be odd, e.g. 10001
    t_0 = np.linspace(0, t_p, N_p)      # Set the plateau time for TCF

    w_p = 10000 * omega_c                 # the plateau frequency for spectral density
    Nw_p = 100 * w_p                   # dimensionality for discretization
    w = np.linspace(- w_p, w_p, Nw_p)

    #   number of terms for TCF real and imaginary part fitting
    K_r = 8
    K_i = 7

# ======================================================================================
#                                      Auxiliaries
# ======================================================================================

# Zero temperature TCF
# def Ohmic_0(t, alpha, omega_c, s):
#     return alpha * omega_c**2 * gamma(s+1) / (2 * (1 + 1j * omega_c * t)**(s+1))
# Zero temperature TCF discretization
# def tcfd_ohmic(t_0, alpha, omega_c, s, temperature):
#     if temperature == 0:
#         return Ohmic_0(t_0, alpha, omega_c, s)

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

# (Finite temperature) Fourier transform
def fft_J (scale, n, temperature):

    scale_fft = parameter.w_p
    n_fft = parameter.Nw_p

    n_rate = (scale_fft * scale / (4 * n))      # n_rate need to be large
    print(n_rate)
    n_rate = int(n_rate)

    w = np.linspace(0, scale_fft * np.pi, n_fft + 1)[:-1]
    dw = w[1] - w[0]

    # choose the spectral density
    jw = J_ohm(w, alpha, omega_c, s)

    if temperature == 0:
        cw1 = jw * np.ones(len(w))
        cw2 = 0. * np.ones(len(w))

    else:
        beta = 1. / temperature

        # Effective spectral density for the SSB model
        def J_eff(x, alpha, omega_c, s):
            return J_ohm(x, alpha, omega_c, s) * np.tanh(beta * x / 2.0)

        # SSB model, using the effective spectral density. Turn off to return to SBB model
        jw = J_eff(w, alpha, omega_c, s)

        cw1 = jw / (1 - np.exp(- beta * w))
        cw2 = jw / (1 - np.exp(+ beta * w))

    del jw

    cw1[0] = (cw1[1] + cw2[1]) / 4
    cw2[0] = (cw1[1] + cw2[1]) / 4
    fft_ct = (np.fft.fft(cw1) * dw - np.fft.ifft(cw2) * len(cw2) * dw) / np.pi
    fft_t = 2 * np.pi * np.fft.fftfreq(len(cw1), dw)
    del cw1, cw2

    fft_ct = fft_ct[(scale>=fft_t) & (fft_t >= 0)][::n_rate]
    fft_t = fft_t[(scale>=fft_t) & (fft_t >= 0)][::n_rate]

    np.savetxt("fft_t", fft_t)
    np.savetxt("fft_ct", fft_ct)

    return fft_ct, fft_t 

# ======================================================================================
#                                      Analysis
# ======================================================================================

t_0 = parameter.t_0
K_r, K_i = parameter.K_r, parameter.K_i
alpha, omega_c, s = parameter.alpha, parameter.omega_c, parameter.s
temperature = parameter.T

if __name__ == '__main__':

    # TCF discretization
    fft_t = np.loadtxt("fft_t", dtype = float)
    fft_ct = np.loadtxt("fft_ct", dtype = complex)

    etal = np.loadtxt("etal", dtype = complex)
    expn = np.loadtxt("expn", dtype = complex)

    etal_r, etal_i = np.real(etal), np.imag(etal)
    expn_r, expn_i = np.real(expn), np.real(expn)

# ====== plot the spectral density ======

    def plot_Jw ():

        Jw = J_ohm
        w = parameter.w
        alpha, omega_c, s = parameter.alpha, parameter.omega_c, parameter.s

        plt.plot(w, Jw(w, alpha, omega_c, s))
        plt.show()

        return 0

# ====== Compare the TCF fitting ======

    def plot_Ct ():

        fig = plt.figure(figsize=(10, 4), dpi = 512)
        plt.subplot(1,2,1)
        plt.plot(t_0, fit_p(t_0, etal_r, expn_r).real, label = "fitted")
        plt.plot(fft_t, np.real(fft_ct), ls='--', label = "original")

        plt.legend(frameon = False)
#        plt.show()

        plt.subplot(1,2,2)
        plt.plot(t_0, fit_p(t_0, etal_i, expn_i).real, label = "fitted")
        plt.plot(fft_t, np.imag(fft_ct), ls='--', label = "original")

        plt.legend(frameon = False)
#        plt.show()
        plt.savefig("model.pdf")

        return 0

# ====== Compare the spectrum fitting ======

#    def plot_Cw ():
#
#        len_ = 1000000
#        spe_wid = 10
#        w = np.linspace(-spe_wid, spe_wid, len_)
#
#        jw = gen_jw(w)
#        jw1 = jw / (1 - np.exp(-beta * w))
#        # plt.plot(w, jw)
#        plt.plot(w, jw1)
#        fft_ct[0] = fft_ct[0] / 2
#        plt.plot(2 * np.pi * np.fft.fftfreq(len(fft_ct), fft_t[1] - fft_t[0]),
#                 len(fft_ct) * (fft_t[1] - fft_t[0]) * np.fft.ifft(fft_ct))
#        plt.xlim(-10, 10)
#        fft_ct[0] = fft_ct[0] * 2
#
#        fft_ct
#
#        plt.legend(frameon = False)
#        plt.show()
#
#        return 0
#
# ======================================================================================

#    plot_Jw ()
    plot_Ct ()
#    plot_Cw ()

