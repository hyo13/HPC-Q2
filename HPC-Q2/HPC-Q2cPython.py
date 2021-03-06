# -*- coding: utf-8 -*-
"""
Spyder Editor

HPC-Q2c Python Script to call C++ Script
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
Nt=2000
alpha=1

#Compile C++ program
subprocess.call('g++ main.cpp',shell=True)

#Calculate RMS trendlines for Nx between 20 and 30 at increments of 2
while (Nx<=30):

    #Initialize dt and RMS array
    DT=[]
    RMS=[]
    
    #Calculate RMS Error for Nt between 2000 and 2400 at increments of 50
    Nt=2000
    while (Nt<=2400):
        #Initial Calculations
        dt=T/Nt
        DT.append(dt)
        
        #Convert inputs to string to run C++ program
        inputs='./a.out'+' '+repr(L)+' '+repr(Nx)+' '+repr(T)+' '+repr(Nt)+' '+repr(alpha)
        
        #Run C++ program and obtain output results
        output=subprocess.Popen(inputs, shell=True, stdout=subprocess.PIPE)
        U=output.communicate()[0]
        #Convert string to array
        U=[float(s) for s in U.split()] 
        U=np.array(U)
        
        #Create time array
        TIME=[]
        for i in range(0,Nt):
            TIME.append(i*dt)
        TIME=np.array(TIME)
        
        #Calculate Analytical Solution
        Ut=[]
        for i in range(0,Nt):
            t=TIME[i]
            Utt=[]
            for n in range(1,21):
                Utt.append((8*math.sin(n*math.pi/2)**2/(math.pi**3*n**3))*math.sin(n*math.pi/2)*math.exp(-alpha*t*n**2*math.pi**2/L**2))
            Ut.append(np.sum(Utt))
        Ut=np.array(Ut)
        
        #Calculate RMS Error
        RMS.append((np.sum((Ut-U)**2)/Nt)**0.5)    
        
        #Nt Increment
        print("Nt= ",Nt)
        Nt=Nt+50
        
    #Convert List to Array
    RMS=np.array(RMS)
    #Plot RMS vs DT
    name='Nx= '+repr(Nx)
    plt.plot(DT,RMS,label=name)
    
    #Nx Increment
    print("Nx= ",Nx)
    Nx=Nx+2

#Plot Configurations
plt.grid(b=None, which='major', axis='both')
plt.legend(loc='best')
plt.title('RMS vs dt at Different Values of Nx')
plt.xlabel('dt')
plt.ylabel('RMS')