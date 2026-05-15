import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm

def potential(x, y):

    r = np.sqrt(x**2 + y**2)
    y_hat = np.divide(y, r**2, out=np.zeros_like(y), where=(np.abs(r)>1e-3))

    return y_hat

delta = 0.02
x = np.arange(-10.0, 10.0+delta, delta)
y = np.arange(-10.0, 10.0+delta, delta)
X, Y = np.meshgrid(x, y)

Z = potential(X, Y)
print(np.max(Z), np.min(Z))

0
fig, ax = plt.subplots()#(subplot_kw={"projection": "3d"})
levels = np.linspace(-15,15,100)
CS = ax.contour(X, Y, Z, levels=levels, cmap='jet')

ax.annotate("", xytext=(-1.5, 0), xy=(1.5, 0), zorder=-1,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#000000", shrinkA=0, shrinkB=0))
ax.annotate("", xytext=(0, -1.5), xy=(0, 1.5), zorder=-1,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#000000", shrinkA=0, shrinkB=0))

#ax.axhline(0, color='k', lw=2)
#ax.axvline(0, color='k', lw=2)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

ax.set_aspect('equal')
ax.axis('off')


# Define the continuous normalization (vmin and vmax define the data range)
norm = mpl.colors.Normalize(vmin=-10, vmax=10)

# Choose a continuous colormap
cmap = cm.jet

# Create a ScalarMappable object with the norm and cmap
mappable = cm.ScalarMappable(norm=norm, cmap=cmap)
mappable.set_array([]) # set_array([]) is often needed to avoid warnings

# Create the colorbar using the ScalarMappable
cbar = fig.colorbar(mappable, ax=ax, location='right', ticks=[-10, 0, 10])
cbar.ax.set_yticklabels(['-ve', '0', '+ve'])  

plt.show()