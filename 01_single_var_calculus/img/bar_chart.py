# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 04:25:14 2025

@author: mings
"""

import numpy as np
import matplotlib.pyplot as plt

data = [165, 165, 166, 167, 167, 167, 168, 168, 169, 169, 169, 169, 170, 170, 172, 172, 172, 173, 174, 174]

counts, bins = np.histogram(data, bins=np.arange(163.5,176.5))
plt.figure()
#plt.hist(bins[:-1], bins, weights=counts, rwidth=1)
plt.stairs(counts, bins)
#plt.plot((bins[:-1]+bins[1:])/2, counts, "r")
plt.show()