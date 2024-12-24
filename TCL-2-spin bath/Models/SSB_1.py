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

def get_Qs(NStates):

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
    
#    ε, Δ, β, ωc, alpha, ndof, t = 1, 1, 0.25, 1, 0.4, 300, 15       # Fig 4a
#    ε, Δ, β, ωc, alpha, ndof, t = 1, 1, 1.0, 2, 0.4, 300, 15        # Fig 4b
    ε, Δ, β, ωc, alpha, ndof, t = 1, 1, 5.0, 2, 0.4, 300, 15        # Fig 4c

# ====================================================================================================

    # propagation
    dt = 0.0025             # integration time step
    NSteps = int(t / dt)    # number of steps
    nskip = 10              # interval for data recording

    # produce the Hamiltonian, initial RDM
    hams = get_Hs(ε, Δ)
    rho0 = get_rho0(NStates)

    nmod = 1         # number of dissipation modes
    C_ab = np.zeros((nmod, NSteps), dtype = complex)    # bare-bath TCFs
    coeff = np.zeros((nmod, ndof), dtype = complex)
    for n in range(nmod):
        coeff[n, :], ω  = bathParam(ωc, alpha, ndof)
        for i in range(NSteps):
            C_ab[n, i] = 0.25 * np.sum((coeff[n, :]**2 / (2 * ω)) * (- 1.0j * np.tanh(β * ω / 2) * np.sin(ω * i * dt) + np.cos(ω * i * dt)))
    
    qmds = np.zeros((nmod, NStates, NStates), dtype = complex)
    qmds[0, :, :] = get_Qs(NStates)
