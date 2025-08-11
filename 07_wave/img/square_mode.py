# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 00:14:14 2025

@author: mings
"""

import numpy as np
import matplotlib.pyplot as plt

L = 10

x = np.linspace(0,L,num=1000)

f = lambda x: 2*(x<(L/2))-1

f1 = lambda x: 4/np.pi*np.sin(2*np.pi/L*x)

f2 = lambda x: 4/np.pi*(np.sin(2*np.pi/L*x) + np.sin(2*np.pi/L*3*x)/3)

f3 = lambda x: 4/np.pi*(np.sin(2*np.pi/L*x) + np.sin(2*np.pi/L*3*x)/3 + np.sin(2*np.pi/L*5*x)/5)


fig = plt.figure(figsize=(12,6))
ax = plt.subplot(111)
ax.axhline(0, c="k")
ax.axvline(0, c="k")
ax.axvline(L, c="k")
ax.plot(x,f(x), label="Square wave", c="r", lw="3")
ax.plot(x,f1(x), label="First mode")
ax.plot(x,f2(x), label="First 2 modes")
ax.plot(x,f3(x), label="First 3 modes")
ax.axis("off")


box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

