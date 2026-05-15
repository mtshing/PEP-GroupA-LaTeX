import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.colors as colors

def field(x, y, z):

    r = np.sqrt(x**2 + y**2 + z**2)
    x_hat = np.divide(-y, r**3, out=np.zeros_like(x), where=(np.abs(r)>1e-5))
    y_hat = np.divide(x, r**3, out=np.zeros_like(y), where=(np.abs(r)>1e-5))

    return x_hat, y_hat, np.zeros_like(x)

delta = 0.5
#x = np.arange(-1, 1+delta, delta)
#y = np.arange(-1, 1+delta, delta)

#X, Y, Z = np.meshgrid(x, y, z)

r = np.linspace(0, 1.2, 6)
theta = np.linspace(0, 2*np.pi, 15) # Angular coordinate from 0 to 2π

# sph coor looks bad
# phi = np.linspace(0, np.pi, 15)
# R, Theta, Phi = np.meshgrid(r, theta, phi)
# X = R * np.cos(Theta)*np.sin(Phi)
# Y = R * np.sin(Theta)*np.sin(Phi)
# Z = R * np.cos(Phi)

# cyl coor looks better, but need extra ring
z = np.arange(-2*delta, 3*delta, delta)
R, Theta, Z = np.meshgrid(r, theta, z)
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

U, V, W = field(X,Y,Z)
Mag = (X**2+Y**2+Z**2 < 1.5)*np.sqrt(U**2 + V**2 + W**2)
Mag = np.power(Mag, 1/3)
Mag = (Mag.ravel() - Mag.min())/(Mag.max()-Mag.min())

'''
r2 = 0.75 #np.linspace(1.25, 1.5, 2)
R2, Theta2, Z2 = np.meshgrid(r2, theta, [-delta, 0, delta])
X2 = R2 * np.cos(Theta2)
Y2 = R2 * np.sin(Theta2)

U2, V2, W2 = field(X2, Y2, Z2)
Mag2 = np.sqrt(U2**2 + V2**2 + W2**2)
Mag2 = np.power(Mag2, 1/3)
Mag2 = (Mag2.ravel() - Mag2.min())/(Mag2.max()-Mag2.min())
'''#


# Repeat for each body line and two head lines
C = np.concatenate((Mag, np.repeat(Mag, 2)))
#C2 = np.concatenate((Mag2, np.repeat(Mag2, 2)))

# Colormap
C = plt.cm.jet(C)
#C2 = plt.cm.jet(C2)




fig, ax = plt.subplots(subplot_kw={"projection": "3d"})



'''
Q2 = ax.quiver(X2*10, Y2*10, Z2*10, U2, V2, W2, #colors=C, 
              linewidth=(Mag**2.5)*5, 
              arrow_length_ratio=0.5, 
              pivot="middle",
              length=2.7,
              normalize=True
              )
'''


Q = ax.quiver(X*10, Y*10, Z*10, U, V, W, #colors=C, 
              linewidth=(Mag**2.5)*5, 
              arrow_length_ratio=0.5, 
              pivot="middle",
              length=2.7,
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
ax.quiver(0, 0, 0, 0, 0, axis_length*0.9, 
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
ax.view_init(25, 45)


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