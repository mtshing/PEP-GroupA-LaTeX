import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from copy import deepcopy

#%%

# reading the image
image = plt.imread('./sun.png')
image_box = OffsetImage(image, zoom=0.01)
sun = AnnotationBbox(image_box, (0, 0), frameon=False, zorder=-2)

def polar2cart(r,theta):
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x,y

# fix r_0 = 1
r0 = 1

#%%


# circle
theta = np.arange(0, np.pi*2,0.01)
r = np.ones_like(theta)*r0

x,y = polar2cart(r,theta)


fig, ax = plt.subplots(1, 1, figsize=(8, 6))



# center and trajectory
ax.plot(x, y, c="k", zorder=-1)
#ax.scatter(0,0, fc="k", zorder=5)
new_sun = deepcopy(sun)
ax.add_artist(new_sun)


# plot axis
ax.annotate("", xytext=(-2, 0), xy=(2, 0), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#cccccc", shrinkA=0, shrinkB=0))
ax.annotate("", xytext=(0, -1.5), xy=(0, 1.5), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#cccccc", shrinkA=0, shrinkB=0))


# plot red line for a
ax.annotate('', xy=(1, -0.1), xytext=(0, -0.1), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec="r", shrinkA=0, shrinkB=0))
ax.text(0.5,-0.2,r"$a = r_0$", ha="center",color="r")


# plot blue line for b
ax.annotate('', xy=(-0.1, 1), xytext=(-0.1, 0), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec=u'#1f77b4', shrinkA=0, shrinkB=0))
ax.text(-0.25,0.5,r"$b = r_0$", ha="center", color=u'#1f77b4')



#ax.set_xticks(np.pi/180*np.arange(0,360,90))
#ax.grid(False)
ax.axis('off')
ax.set_xlim([-2,2])
ax.set_ylim([-1.5,1.5])
ax.set_aspect('equal')
plt.show()
plt.savefig("circle.png",bbox_inches='tight')


#%%
# ellipse
# take epsilon = 0.4
eps = 0.4

theta = np.arange(0, np.pi*2,0.01)

r = r0/(eps*np.cos(theta)+1)
a = r0/(1-eps**2)
b = r0/np.sqrt(1-eps**2)

x,y = polar2cart(r,theta)


fig, ax = plt.subplots(1, 1, figsize=(8, 6))

# center and trajectory
ax.plot(x, y, c="k", zorder=-1)
ax.scatter(-a*eps,0, marker="x", fc="#cccccc", zorder=-2)
new_sun = deepcopy(sun)
ax.add_artist(new_sun)

# plot axis
ax.annotate("", xytext=(-2, 0), xy=(2, 0), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#cccccc", shrinkA=0, shrinkB=0))
ax.annotate("", xytext=(0, -1.5), xy=(0, 1.5), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#cccccc", shrinkA=0, shrinkB=0))

# plot red line for a
ax.annotate('', xy=(-a*eps+a, -0.1), xytext=(-a*eps, -0.1), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec="r", shrinkA=0, shrinkB=0))
ax.text(-a*eps+a/2, -0.2, r"$a$", ha="center",color="r")

ax.annotate('', xy=(-a*eps-a, -0.1), xytext=(-a*eps, -0.1), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec="r", shrinkA=0, shrinkB=0))
ax.text(-a*eps-a/2, -0.2, r"$a$", ha="center",color="r")


# annotate for aphelion, perihelion
ax.annotate('Perihelion', xy=(-a*eps+a, 0), xytext=(30, 40), zorder=0, textcoords="offset points", c="#ff7f0e", ha="center",
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#ff7f0e", shrinkB=5))

ax.annotate('Aphelion', xy=(-a*eps-a, 0), xytext=(-30, 40), zorder=0, textcoords="offset points", c="#ff7f0e", ha="center",
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#ff7f0e", shrinkB=5))

# plot blue line for r0
ax.annotate('', xy=(0.05, 1), xytext=(0.05, 0), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec=u'#1f77b4', shrinkA=0, shrinkB=0))
ax.text(0.12, 0.5, r"$r_0$", ha="center", color=u'#1f77b4')


# plot blue line for b
ax.annotate('', xy=(-a*eps-0.05, b), xytext=(-a*eps-0.05, 0), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec=u'#1f77b4', shrinkA=0, shrinkB=0))
ax.text(-a*eps, 0.5*b, r"$b$", ha="center", color=u'#1f77b4')


# plot green line for c
ax.annotate('', xy=(-a*eps, 0.05), xytext=(0, 0.05), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec="#2ca02c", shrinkA=0, shrinkB=0))
ax.text(-a*eps/2, 0.1, r"$c$", ha="center",color="#2ca02c")


#ax.set_xticks(np.pi/180*np.arange(0,360,90))
#ax.grid(False)
ax.axis('off')
ax.set_xlim([-2,2])
ax.set_ylim([-1.5,1.5])
ax.set_aspect('equal')
plt.show()
plt.savefig("ellipse.png",bbox_inches='tight')


#%%
# parabola
# take epsilon = 1
eps = 1

theta = np.arange(0, np.pi*2,0.01)

r = r0/(eps*np.cos(theta)+1)
x,y = polar2cart(r,theta)


fig, ax = plt.subplots(1, 1, figsize=(8, 6))

# center and trajectory
ax.plot(x, y, c="k", zorder=-1)
#ax.scatter(-a*eps,0, marker="x", fc="#cccccc", zorder=-2)
new_sun = deepcopy(sun)
ax.add_artist(new_sun)

# plot axis
ax.annotate("", xytext=(-2, 0), xy=(2, 0), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#cccccc", shrinkA=0, shrinkB=0))
ax.annotate("", xytext=(0, -1.5), xy=(0, 1.5), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#cccccc", shrinkA=0, shrinkB=0))


# plot red line for r0/2
ax.annotate('', xy=(r0/2, -0.1), xytext=(0, -0.1), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec="r", shrinkA=0, shrinkB=0))
ax.text(r0/4, -0.25, r"$\frac{r_0}{2}$", ha="center",color="r")

# annotate for perihelion
ax.annotate('Perihelion', xy=(r0/2, 0), xytext=(30, 40), zorder=0, textcoords="offset points", c="#ff7f0e", ha="center",
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#ff7f0e", shrinkB=5))


# plot blue line for r0
ax.annotate('', xy=(-0.05, 1), xytext=(-0.05, 0), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec=u'#1f77b4', shrinkA=0, shrinkB=0))
ax.text(-0.12, 0.5, r"$r_0$", ha="center", color=u'#1f77b4')



ax.axis('off')
ax.set_xlim([-2,2])
ax.set_ylim([-1.5,1.5])
ax.set_aspect('equal')
plt.show()
plt.savefig("parabola.png",bbox_inches='tight')


#%%
# hyperbola
# take epsilon = 1.8
eps = 1.8

theta = np.arange(0, np.pi*2,0.01)
theta1 = theta[np.cos(theta)>-1/eps]
theta2 = theta[np.cos(theta)>1/eps]

r1 = r0/(eps*np.cos(theta1)+1)
r2 = r0/(eps*np.cos(theta2)-1)
a = r0/(1-eps**2)

x1,y1 = polar2cart(r1,theta1)
x2,y2 = polar2cart(r2,theta2)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))


# center and trajectory
ax.plot(x1, y1, c="k", zorder=-1)
ax.plot(x2, y2, c="k", zorder=-1, ls="dashed")
ax.scatter(-a*eps,0, marker="x", fc="#cccccc", zorder=-2)
new_sun = deepcopy(sun)
ax.add_artist(new_sun)

# plot axis
ax.annotate("", xytext=(-2, 0), xy=(2, 0), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#cccccc", shrinkA=0, shrinkB=0))
ax.annotate("", xytext=(0, -1.5), xy=(0, 1.5), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#cccccc", shrinkA=0, shrinkB=0))


# plot red line for a
ax.annotate('', xy=(-a*eps+a, 0.02), xytext=(-a*eps, 0.02), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec="r", shrinkA=0, shrinkB=0))
ax.text(-a*eps+a/2, 0.05, r"$a$", ha="center",color="r")

ax.annotate('', xy=(-a*eps-a, 0.02), xytext=(-a*eps, 0.02), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec="r", shrinkA=0, shrinkB=0))
ax.text(-a*eps-a/2, 0.05, r"$a$", ha="center",color="r")


# annotate for perihelion
ax.annotate('Perihelion', xy=(-a*eps+a, 0.02), xytext=(-a*eps, 0.5), zorder=0, c="#ff7f0e", ha="center",
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#ff7f0e", shrinkB=5))

ax.annotate('', xy=(-a*eps-a, 0.02), xytext=(-a*eps, 0.46), zorder=0, c="#ff7f0e", ha="center",
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#ff7f0e", shrinkB=5))

# plot blue line for r0
ax.annotate('', xy=(-0.05, 1), xytext=(-0.05, 0), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec=u'#1f77b4', shrinkA=0, shrinkB=0))
ax.text(-0.12, 0.5, r"$r_0$", ha="center", color=u'#1f77b4')


# plot green line for c
ax.annotate('', xy=(-a*eps, -0.05), xytext=(0, -0.05), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec="#2ca02c", shrinkA=0, shrinkB=0))
ax.text(-a*eps/2, -0.15, r"$c$", ha="center",color="#2ca02c")


# annotate for attractive/repulsive path
ax.text(0.3,-1.2, "Path for\n attractive force", ha="center")
ax.text(-2*a*eps-0.3,-1.2, "Path for\n repulsive force", ha="center")


ax.axis('off')
ax.set_xlim([-2,2])
ax.set_ylim([-1.5,1.5])
ax.set_aspect('equal')
plt.show()
plt.savefig("hyperbola.png",bbox_inches='tight')


#%%
# plot all

fig, ax = plt.subplots(1, 1, figsize=(8, 6))

# center
new_sun = deepcopy(sun)
ax.add_artist(new_sun)

# plot axis
ax.annotate("", xytext=(-2, 0), xy=(2, 0), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#cccccc", shrinkA=0, shrinkB=0))
ax.annotate("", xytext=(0, -1.5), xy=(0, 1.5), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#cccccc", shrinkA=0, shrinkB=0))


# circle
theta = np.arange(0, np.pi*2,0.01)
r = np.ones_like(theta)*r0

x,y = polar2cart(r,theta)

ax.plot(x, y, c="#1f77b4", zorder=-1, label="Circle")



# ellipse
eps = 0.4

theta = np.arange(0, np.pi*2,0.01)

r = r0/(eps*np.cos(theta)+1)
x,y = polar2cart(r,theta)

ax.plot(x, y, c="#ff7f0e", zorder=-1, label="Ellipse")




# parabola
eps = 1

theta = np.arange(0, np.pi*2,0.01)

r = r0/(eps*np.cos(theta)+1)
x,y = polar2cart(r,theta)

ax.plot(x, y, c="#2ca02c", zorder=-1, label="Parabola")


# hyperbola
eps = 1.8

theta = np.arange(0, np.pi*2,0.01)
theta1 = theta[np.cos(theta)>-1/eps]
theta2 = theta[np.cos(theta)>1/eps]

r1 = r0/(eps*np.cos(theta1)+1)
r2 = r0/(eps*np.cos(theta2)-1)
a = r0/(1-eps**2)

x1,y1 = polar2cart(r1,theta1)
x2,y2 = polar2cart(r2,theta2)

ax.plot(x1, y1, c="#d62728", zorder=-1, label="Hyperbola")
ax.plot(x2, y2, c="#d62728", zorder=-1, ls="dashed")





ax.axis('off')
ax.set_xlim([-2,2])
ax.set_ylim([-1.5,1.5])
ax.set_aspect('equal')
ax.legend(loc=0)
plt.show()
plt.savefig("all_traj.png",bbox_inches='tight')