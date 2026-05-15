import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.colors as colors

def field(x, y):

    r = np.sqrt(x**2 + y**2)
    x_hat = np.divide(3*x*y, r**5, out=np.zeros_like(y), where=(np.abs(r)>1e-5))
    y_hat = np.divide(3*y**2-r**2, r**5, out=np.zeros_like(y), where=(np.abs(r)>1e-5))

    return x_hat, y_hat

delta = 0.05
x = np.arange(-1.5, 1.5+delta, delta)
y = np.arange(-1.5, 1.5+delta, delta)
X, Y = np.meshgrid(x, y)
U, V = field(X, Y)
C = np.sqrt(U**2 + V**2)
print(np.max(C), np.min(C))


fig, ax = plt.subplots()#(subplot_kw={"projection": "3d"})




Q = ax.streamplot(x, y, U, V, color=C, density=1.2, linewidth=1, cmap=cm.jet, norm=colors.LogNorm(vmin=0.1, vmax=np.max(C)/10))


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
norm = mpl.colors.Normalize(vmin=0, vmax=np.max(C)/10)

# Choose a continuous colormap
cmap = cm.jet

# Create a ScalarMappable object with the norm and cmap
mappable = cm.ScalarMappable(norm=norm, cmap=cmap)
mappable.set_array([]) # set_array([]) is often needed to avoid warnings


# Create the colorbar using the ScalarMappable
cbar = fig.colorbar(mappable, ax=ax, location='right', ticks=[0.1, np.max(C)/10])
cbar.ax.set_yticklabels(['0', 'strongest'])  

plt.show()