import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.colors as colors

def field(x, y, z):

    r = np.sqrt(x**2 + y**2 + z**2)
    x_hat = np.divide(3*z*x, r**5, out=np.zeros_like(x), where=(np.abs(r)>1e-5))
    y_hat = np.divide(3*z*y, r**5, out=np.zeros_like(y), where=(np.abs(r)>1e-5))
    z_hat = np.divide(3*z**2-r**2, r**5, out=np.zeros_like(z), where=(np.abs(r)>1e-5))

    return x_hat, y_hat, z_hat

delta = 0.25
#x = np.arange(-1, 1+delta, delta)
#y = np.arange(-1, 1+delta, delta)


#r = np.linspace(0, 1, 4)          # Radial distance from 0 to 5
r = [0, 0.4, 0.65, 0.85, 1, 1.1]
theta = np.linspace(0, 2*np.pi, 15) # Angular coordinate from 0 to 2π
z = np.arange(-1, 1+delta, delta)

R, Theta, Z = np.meshgrid(r, theta, z)

#X, Y, Z = np.meshgrid(x, y, z)
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

U, V, W = field(X,Y,Z)
Mag = np.sqrt(U**2 + V**2 + W**2)

Mag = np.power(Mag,1/3)
#U = np.divide(U, 0.5*Mag**(3), out=np.zeros_like(U), where=(Mag>1e-5))
#V = np.divide(V, 0.5*Mag**(3), out=np.zeros_like(V), where=(Mag>1e-5))
#W = np.divide(W, 0.5*Mag**(3), out=np.zeros_like(W), where=(Mag>1e-5))



Mag = (Mag.ravel() - Mag.min())/(Mag.max()-Mag.min())
# Repeat for each body line and two head lines
C = np.concatenate((Mag, np.repeat(Mag, 2)))
# Colormap
C = plt.cm.jet(C)


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})




Q = ax.quiver(X*10, Y*10, Z*10, U, V, W, #colors=C, 
              linewidth=(Mag**2.4)*5, 
              arrow_length_ratio=0.5, 
              pivot="middle",
              length=1.7,
              normalize=True
              )


#ax.annotate("", xytext=(-1.5, 0), xy=(1.5, 0), zorder=-1,
#            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#000000", shrinkA=0, shrinkB=0))
#ax.annotate("", xytext=(0, -1.5), xy=(0, 1.5), zorder=-1,
#            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#000000", shrinkA=0, shrinkB=0))


#ax.axhline(0, color='k', lw=2)
#ax.axvline(0, color='k', lw=2)
#ax.set_xlim(-1.5, 1.5)
#ax.set_ylim(-1.5, 1.5)

axis_length = 35
ax.quiver(0, 0, 0, 0, 0, axis_length*0.7, 
          color="k",
          linewidth=1,  
          pivot="middle",
          arrow_length_ratio=1/axis_length,)
ax.quiver(0, 0, 0, 0, axis_length, 0, 
          color="k",
          linewidth=1,  
          pivot="middle",
          arrow_length_ratio=1/axis_length,)
ax.quiver(0, 0, 0, axis_length, 0, 0,
          color="k",
          linewidth=1,  
          pivot="middle",
          arrow_length_ratio=1/axis_length,)

ax.set_aspect('equal')
ax.axis('off')
ax.view_init(15, 43)


# Define the continuous normalization (vmin and vmax define the data range)
##norm = mpl.colors.Normalize(vmin=0, vmax=np.max(C)/10)

# Choose a continuous colormap
cmap = cm.jet

# Create a ScalarMappable object with the norm and cmap
#mappable = cm.ScalarMappable(norm=norm, cmap=cmap)
#mappable.set_array([]) # set_array([]) is often needed to avoid warnings


# Create the colorbar using the ScalarMappable
#cbar = fig.colorbar(mappable, ax=ax, location='right', ticks=[0.1, np.max(C)/10])
#cbar.ax.set_yticklabels(['0', 'strongest'])  

plt.show()