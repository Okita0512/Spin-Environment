import numpy as np

def coth(x):
    return (1 + np.exp(-2 * x)) / (1 - np.exp(-2 * x))

def bathParam(ωc, alpha, ndof):     # for bath descritization

    c = np.zeros(( ndof ))
    ω = np.zeros(( ndof ))
    for d in range(ndof):

        ω[d] =  - ωc * np.log(1 - (d + 1)/(ndof + 1))
        c[d] =  np.sqrt(alpha * ωc / (ndof + 1)) * ω[d]

    return c, ω

def get_Hs(ε, Δ):

    Hs = np.zeros((2,2))

    Hs[0, 0] = ε
    Hs[1, 1] = - ε
    Hs[0, 1] = Hs[1, 0] = Δ

    return Hs

def get_sigmax(NStates):

    Qs = np.zeros((NStates, NStates), dtype = complex)
    Qs[0, 1] = 1.0
    Qs[1, 0] = 1.0

    return Qs

def get_sigmay(NStates):

    Qs = np.zeros((NStates, NStates), dtype = complex)
    Qs[0, 1] = - 1.0j
    Qs[1, 0] = 1.0j

    return Qs

def get_sigmaz(NStates):

    Qs = np.zeros((NStates, NStates), dtype = complex)
    Qs[0, 0] = 1.0
    Qs[1, 1] = - 1.0

    return Qs

def get_rho0(NStates):

    rho0 = np.zeros((NStates, NStates), dtype = complex)
    rho0[0, 0] = 1.0 + 0.0j

    return rho0

class parameters():

    # Model parameters
    NStates = 2      # number of states
    
    ε, Δ, β, ωc, alpha, ndof, t = 0, 1, np.inf, 1, 0.1, 300, 40       # Fig 4a
#    ε, Δ, β, ωc, alpha, ndof, t = 1, 1, 1.0, 2, 0.4, 300, 15        # Fig 4b
#    ε, Δ, β, ωc, alpha, ndof, t = 1, 1, 5.0, 2, 0.4, 300, 15        # Fig 4c

# ====================================================================================================

    # propagation
    dt = 0.0025             # integration time step
    NSteps = int(t / dt)    # number of steps
    nskip = 10              # interval for data recording

    # produce the Hamiltonian, initial RDM
    hams = get_Hs(ε, Δ)
    rho0 = get_rho0(NStates)

    nmod = 2         # number of dissipation modes
    coeff = np.zeros((ndof), dtype = complex)
    coeff, ω  = bathParam(ωc, alpha, ndof)

    C_ab = np.zeros((nmod, nmod, NSteps), dtype = complex)    # bare-bath TCFs
    for i in range(NSteps):
        C_ab[0, 0, i] = 0.25 * np.sum((coeff**2 / (2 * ω)) * (- 1.0j * np.tanh(β * ω / 2) * np.sin(ω * i * dt) + np.cos(ω * i * dt)))
        C_ab[1, 1, i] = 0.25 * np.sum((coeff**2 / (2 * ω)) * (- 1.0j * np.tanh(β * ω / 2) * np.sin(ω * i * dt) + np.cos(ω * i * dt)))
#        C_ab[2, 2, i] = 0.25 * np.sum((coeff**2 / (2 * ω)))
        C_ab[0, 1, i] = 0.25 * np.sum((coeff**2 / (2 * ω)) * (- 1.0j * np.tanh(β * ω / 2) * np.cos(ω * i * dt) - np.sin(ω * i * dt)))
        C_ab[1, 0, i] = - C_ab[0, 1, i]
    
    qmds = np.zeros((nmod, NStates, NStates), dtype = complex)
    qmds[0, :, :] = get_sigmax(NStates)
    qmds[1, :, :] = get_sigmay(NStates)
#    qmds[2, :, :] = get_sigmaz(NStates)
    
    # debug
    qmds = qmds
