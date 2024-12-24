import numpy as np
from scipy.linalg import expm

# ====== Redfield tensor plus the coherent term ======
def func(tn, rho_ad, par): 
    
    NStates = par.NStates
    nmod = par.nmod
    qmds = par.qmds
    hams = par.hams
    dt = par.dt
    istep = int(tn / dt)
    C_ab = par.C_ab
    R_ten_1 = par.R_ten_1
    R_ten_2 = par.R_ten_2
    R_ten_3 = par.R_ten_3
    R_ten_4 = par.R_ten_4

    # initialize with coherent commutator
    R_rho = - 1.0j * (hams @ rho_ad - rho_ad @ hams)

    # further add the non-Markovian relaxation terms, the positive terms
    R_rho += np.einsum('ijkl, kj', R_ten_2, rho_ad) + np.einsum('ijkl, kj', R_ten_3, rho_ad)
    
    # further add the non-Markovian relaxation terms, the negative terms
    R_rho += - np.einsum('ijjk, kl', R_ten_1, rho_ad) - np.einsum('ij, jkkl', rho_ad, R_ten_4)

    # update the Redfield tensors
    for m in range(nmod):
        for n in range(nmod):
            Sm = qmds[m, :, :]
            Sn = qmds[n, :, :]
            Sn_tau = expm(- 1.0j * hams * tn) @ Sn @ expm(1.0j * hams * tn)
            TCF = C_ab[m, n, istep]
            R_ten_1 += TCF * dt * np.kron(Sm, Sn_tau).reshape(NStates, NStates, NStates, NStates)
            R_ten_2 += TCF * dt * np.kron(Sn_tau, Sm).reshape(NStates, NStates, NStates, NStates)
            R_ten_3 += TCF.conjugate() * dt * np.kron(Sm, Sn_tau).reshape(NStates, NStates, NStates, NStates)
            R_ten_4 += TCF.conjugate() * dt * np.kron(Sn_tau, Sm).reshape(NStates, NStates, NStates, NStates)

    par.R_ten_1 = R_ten_1
    par.R_ten_2 = R_ten_2
    par.R_ten_3 = R_ten_3
    par.R_ten_4 = R_ten_4
    
    return R_rho
