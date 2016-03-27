# -*- coding: utf-8 -*-
"""
Spyder Editor

HPC-Q2 Python Script to call C++ Script
"""

import subprocess
import matplotlib
import matplotlib.pylab as plt
import numpy
import numpy as np 

#Inputs
L=1
Nx=20
T=1
Nt=1000
alpha=1

#Initial Calculations
dt=T/Nt

#Convert inputs to string to run C++ program
inputs='./a.out'+' '+repr(L)+' '+repr(Nx)+' '+repr(T)+' '+repr(Nt)+' '+repr(alpha)

#Compile C++ program
subprocess.call('g++ main.cpp',shell=True)
#Run C++ program and obtain output results
output=subprocess.Popen(inputs, shell=True, stdout=subprocess.PIPE)
u=output.communicate()[0]
#Convert string to array
u=[float(s) for s in u.split()] 
U=np.array(u)

#Create time array
t = [];
for i in range(0,Nt):
    t.append(i*dt)
T=np.array(t)


