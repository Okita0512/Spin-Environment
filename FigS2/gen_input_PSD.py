#!/usr/bin/env python
# coding: utf-8
# compatible with python2 environment

from __future__ import print_function, absolute_import
from builtins import range

import sys
sys.path.append('../scripts')

import json
import numpy as np
import armadillo as arma
import syst
import bath
from math import sqrt
import subprocess as sub
import os

if __name__ == '__main__':

    with open('default.json') as f:
        ini = json.load(f)

# ==============================================================================================================================

    temp    = 4

    # Ohmic spectral density
    alpha = 0.4
    gamma = 1.0

    nmod = 1 

# ==============================================================================================================================

	# bath
    etal = np.array([0.5 * alpha * gamma**2], dtype = complex)
    etar = etal
    etaa = np.abs(etal)
    expn = np.array([0.0], dtype = complex)
    delr = np.array([0.0])
    mode = np.zeros((1), dtype = int)

    arma.save(mode, 'inp_mode.mat')
    arma.save(delr, 'inp_delr.mat')
    arma.save(etal, 'inp_etal.mat')
    arma.save(etar, 'inp_etar.mat')
    arma.save(etaa, 'inp_etaa.mat')
    arma.save(expn, 'inp_expn.mat')

# ==============================================================================================================================

    # system Hamiltonian and dissipation operators
    hams = np.zeros((2,2),dtype=complex)
    hams[0,0] = 1.0
    hams[1,1] = -1.0
    hams[0,1] = hams[1,0] = 1.0

    qmds = np.zeros((nmod,2,2),dtype=complex)
    qmds[0,0,0] = 1.0
    qmds[0,1,1] = -1.0

    rho0 = np.zeros((2,2),dtype=complex)
    rho0[0,0] = 1.0

    arma.save (hams,ini['syst']['hamsFile'])
    arma.save (qmds,ini['syst']['qmdsFile'])
    arma.save (rho0,ini['syst']['rho0File'])
    
# ==============================================================================================================================

    # hidx
    ini['hidx']['trun'] = 0
    ini['hidx']['lmax'] = 10000
    ini['hidx']['nmax'] = 1000000
    ini['hidx']['ferr'] = 0.0 # 1e-08

    # proprho
    jsonInit = {"deom":ini,
                "rhot":{
                    "dt": 0.0025,
                    "nt": 6000,
                    "nk": 20,
					"xpflag": 1,
					"staticErr": 0,
                    "rho0File": "inp_rho0.mat",
                    "sdipFile": "inp_sdip.mat",
                    "pdipFile": "inp_pdip.mat",
					"bdipFile": "inp_bdip.mat"
                },
            }

# ==============================================================================================================================

    # dipoles
    sdip = np.zeros((2,2),dtype=float)
    arma.save(sdip,'inp_sdip.mat')

    pdip = np.zeros((nmod,2,2),dtype=float)
    pdip[0,0,1] = pdip[0,1,0] = 1.0
    arma.save(pdip,'inp_pdip.mat')

    bdip = np.zeros(3,dtype=complex)
#    bdip[0]=-complex(5.00000000e-01,8.66025404e-01)
#    bdip[1]=-complex(5.00000000e-01,-8.66025404e-01)
#    bdip[2]=-complex(7.74596669e+00,0.00000000e+00)
    arma.save(bdip,'inp_bdip.mat')

    with open('input.json','w') as f:
        json.dump(jsonInit,f,indent=4) 
