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

subprocess.call('g++ main.cpp',shell=True)
subprocess.call('./a.out 1 20 1 1000 1', shell=True)


