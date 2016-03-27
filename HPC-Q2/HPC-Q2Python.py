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
import math

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
U=output.communicate()[0]
#Convert string to array
U=[float(s) for s in U.split()] 
U=np.array(U)

#Create time array
T=[]
for i in range(0,Nt):
    T.append(i*dt)
T=np.array(T)

#Calculate Analytical Solution
Ut=[]
for i in range(0,Nt):
    t=T[i]
    Utt=[]
    for n in range(1,101):
        Utt.append((8*math.sin(n*math.pi/2)**2/(math.pi**3*n**3))*math.sin(n*math.pi/2)*math.exp(-alpha*t*n**2*math.pi**2/L**2))
    Ut.append(np.sum(Utt))
Ut=np.array(Ut)

#Numerical Solution: Plot U against T
plt.plot(T,U,'b',label="Numerical Solution")
#Analysitcal Solution: Plot Ut against T
plt.plot(T,Ut,'r--',label="Analytical Solution")
#Plot Configurations
plt.grid(b=None, which='major', axis='both')
plt.legend(loc='best')
plt.title('Numerical Solution vs Analytical Solution of 1D Heat Equation')
plt.xlabel('Time (s)')
plt.ylabel('Solution U')