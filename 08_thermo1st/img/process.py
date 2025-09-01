import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from copy import deepcopy


#%%
fig, ax = plt.subplots(1, 1, figsize=(8, 8))


ax.annotate("V", xy=(-0.2, 0), xytext=(1, 0), zorder=-5, size=20,
            arrowprops=dict(arrowstyle="<-, head_length=0.6, head_width=0.3", ec="k", shrinkA=0, shrinkB=0))
ax.annotate("P", xy=(0, -0.2), xytext=(0, 1), zorder=-5, size=20,
            arrowprops=dict(arrowstyle="<-, head_length=0.6, head_width=0.3", ec="k", shrinkA=0, shrinkB=0))


ax.axis('off')
ax.set_xlim([-0.5,1.2])
ax.set_ylim([-0.5,1.2])
ax.set_aspect('equal')
plt.show()