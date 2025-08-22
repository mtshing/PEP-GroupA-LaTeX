import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from angle_annotation import AngleAnnotation 
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
# ellipse
# take epsilon = 0.4
eps = 0.4

fig, ax = plt.subplots(1, 1, figsize=(8, 6))

theta = np.arange(0, np.pi*2,0.01)

r = lambda theta: r0/(eps*np.cos(theta)+1)

x,y = polar2cart(r(theta),theta)
ax.plot(x, y, c="k", zorder=-1)


th0 = -0.5
th1 = 1
x0,y0 = polar2cart(r(th0),th0)
x1,y1 = polar2cart(r(th1),th1)
ax.plot([0,x0], [0,y0], c=u'#1f77b4', zorder=-4)
ax.plot([0,x1], [0,y1], c=u'#1f77b4', zorder=-4)

theta_00 = np.linspace(0,th0,50)
x00, y00 = polar2cart(r(theta_00), theta_00)
ax.fill_between(x00, y00, color=u'#1f77b4', zorder=-4)
ax.fill_between([0,x0], [0,y0], color=u'#1f77b4', zorder=-4)

theta_11 = np.linspace(1,th0,50)
x11, y11 = polar2cart(r(theta_11), theta_11)
ax.fill_between(x11, y11, color=u'#1f77b4', zorder=-4)
ax.fill_between([0,x1], [0,y1], color=u'#1f77b4', zorder=-4)


th2 = 3
th3 = 3.4
x2,y2 = polar2cart(r(th2),th2)
x3,y3 = polar2cart(r(th3),th3)
ax.plot([0,x2], [0,y2], c="r", zorder=-4)
ax.plot([0,x3], [0,y3], c="r", zorder=-4)

theta_22 = np.linspace(np.pi,th2,50)
x22, y22 = polar2cart(r(theta_22), theta_22)
ax.fill_between(x22, y22, color="r", zorder=-4)
ax.fill_between([0,x2], [0,y2], color="r", zorder=-4)

theta_33 = np.linspace(np.pi,th3,50)
x33, y33 = polar2cart(r(theta_33), theta_33)
ax.fill_between(x33, y33, color="r", zorder=-4)
ax.fill_between([0,x3], [0,y3], color="r", zorder=-4)


# center and trajectory

new_sun = deepcopy(sun)
ax.add_artist(new_sun)

# plot axis
ax.annotate("", xytext=(-2, 0), xy=(2, 0), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#cccccc", shrinkA=0, shrinkB=0))
ax.annotate("", xytext=(0, -1.5), xy=(0, 1.5), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#cccccc", shrinkA=0, shrinkB=0))


# text annotate
ax.text(1,-1, "If travelling time\n along arcs are the same,\n blue area = red area", ha="center")


#ax.set_xticks(np.pi/180*np.arange(0,360,90))
#ax.grid(False)
ax.axis('off')
ax.set_xlim([-2,2])
ax.set_ylim([-1.5,1.5])
ax.set_aspect('equal')
plt.show()
plt.savefig("kelper2.png",bbox_inches='tight')

#%%

# ellipse
# take epsilon = 0.4
eps = 0.6

theta = np.arange(0, np.pi*2,0.01)

r = lambda theta: r0/(eps*np.cos(theta)+1)

a = r0/(1-eps**2)
b = r0/np.sqrt(1-eps**2)

r_circle1 = np.ones_like(theta)*a
r_circle2 = np.ones_like(theta)*b

x,y = polar2cart(r(theta),theta)
xc1, yc1 = polar2cart(r_circle1, theta)
xc2, yc2 = polar2cart(r_circle2, theta)


fig, ax = plt.subplots(1, 1, figsize=(7.6, 8))

# center and trajectory
ax.plot(x, y, c="k", zorder=-1)
ax.plot(xc1-a*eps, yc1, c="r", ls="dashed", zorder=-2)
ax.text(-1.4,1.8, r"Dotted = A circle of radius $a$", ha="center",color="r", size=15)

#ax.plot(xc2-a*eps, yc2, c=u'#1f77b4', ls="dashed", zorder=-2)

ax.scatter(-a*eps,0, marker="x", fc="#cccccc", zorder=-2)
new_sun = deepcopy(sun)
ax.add_artist(new_sun)


# scatter point = orange
phi = 1.1
ax.scatter(a*np.cos(phi)-a*eps, b*np.sin(phi), s=60, fc="tab:green", zorder=10)
ax.annotate("(x,y)", (a*np.cos(phi)-a*eps, b*np.sin(phi)), xytext=(5,0), zorder=10,
            textcoords="offset points", color="tab:green")


# draw red lines
ax.scatter(a*np.cos(phi)-a*eps, a*np.sin(phi), s=60, fc="r")
ax.plot([-a*eps, a*np.cos(phi)-a*eps], [0,a*np.sin(phi)], c="r")
ax.plot([a*np.cos(phi)-a*eps, a*np.cos(phi)-a*eps], [0,a*np.sin(phi)], c="#ff7f0e", ls="dashed")

ax.text(a*np.cos(phi)/2-a*eps-0.1, a*np.sin(phi)/2, r"$a$", ha="center",color="r")


# phi's label
AngleAnnotation((-a*eps,0), (0,0), (a*np.cos(phi)-a*eps, a*np.sin(phi)), ax=ax,
                      size=75, text=r"$\varphi$", color="tab:orange",
                      text_kw={"color": "tab:orange", "size": 15, "xytext": (-4,-2),"textcoords":"offset points"})

# plot orange line for a\cos\phi - a\eps
ax.annotate('', xy=(-a*eps, -0.2), xytext=(a*np.cos(phi)-a*eps, -0.2), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec="#ff7f0e", shrinkA=0, shrinkB=0))

ax.text(a*np.cos(phi)/2-a*eps ,-0.35, r"$a\cos\varphi$", ha="center",color="#ff7f0e")

ax.annotate('', xy=(a*np.cos(phi)-a*eps, -0.2), xytext=(0, -0.2), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec="tab:green", shrinkA=0, shrinkB=0))

ax.text(a*np.cos(phi)/2-a*eps/2+0.15,-0.35, r"$a\epsilon - a\cos\varphi$", ha="center",color="tab:green")


# plot green line for c
ax.annotate('', xy=(-a*eps, -0.05), xytext=(0, -0.05), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec="r", shrinkA=0, shrinkB=0))
ax.text(-a*eps/2, -0.15, r"$a\epsilon$", ha="center",color="r")


# plot axis
ax.annotate("", xytext=(-2.8, 0), xy=(1, 0), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#cccccc", shrinkA=0, shrinkB=0))
ax.annotate("", xytext=(0, -2.1), xy=(0, 2.1), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#cccccc", shrinkA=0, shrinkB=0))


ax.axis('off')
ax.set_xlim([-2.8,1])
ax.set_ylim([-2.5,2.5])
ax.set_aspect('equal')
plt.show()
plt.savefig("ea1.png",bbox_inches='tight', transparent=True)



#%%

# ellipse
# take epsilon = 0.4
eps = 0.6

theta = np.arange(0, np.pi*2,0.01)

r = lambda theta: r0/(eps*np.cos(theta)+1)

a = r0/(1-eps**2)
b = r0/np.sqrt(1-eps**2)

r_circle1 = np.ones_like(theta)*a
r_circle2 = np.ones_like(theta)*b

x,y = polar2cart(r(theta),theta)
xc1, yc1 = polar2cart(r_circle1, theta)
xc2, yc2 = polar2cart(r_circle2, theta)


fig, ax = plt.subplots(1, 1, figsize=(7.6, 8))

# center and trajectory
ax.plot(x, y, c="k", zorder=-1)
ax.plot(xc2-a*eps, yc2, c="tab:blue", ls="dashed", zorder=-2)
ax.text(-1.4,1.8, r"Dotted = A circle of radius $b$", ha="center",color="tab:blue", size=15)


ax.scatter(-a*eps,0, marker="x", fc="#cccccc", zorder=-2)
new_sun = deepcopy(sun)
ax.add_artist(new_sun)


# scatter point = orange
phi = 1.2
ax.scatter(a*np.cos(phi)-a*eps, b*np.sin(phi), s=60, fc="tab:green", zorder=10)

ax.annotate("(x,y)", (a*np.cos(phi)-a*eps, b*np.sin(phi)), xytext=(3,8), zorder=10,
            textcoords="offset points", color="tab:green")


# draw blue lines
ax.plot([b*np.cos(phi)-a*eps, b*np.cos(phi)-a*eps], [0,b*np.sin(phi)], c="tab:orange", ls="dashed")

ax.annotate('', xy=(b*np.cos(phi)-a*eps+0.12, 0), xytext=(b*np.cos(phi)-a*eps+0.12 ,b*np.sin(phi)), zorder=0,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec="tab:green", shrinkA=0, shrinkB=0))

ax.text(b*np.cos(phi)-a*eps+0.35 ,b*np.sin(phi)/2, r"$b\sin\varphi$", ha="center",color="tab:green")

ax.scatter(b*np.cos(phi)-a*eps, b*np.sin(phi), s=60, fc="tab:blue")
ax.plot([-a*eps, b*np.cos(phi)-a*eps], [0,b*np.sin(phi)], c="tab:blue")

ax.text(a*np.cos(phi)/2-a*eps-0.1, a*np.sin(phi)/2, r"$b$", ha="center",color="tab:blue")

ax.plot([-2.5,1],[b*np.sin(phi), b*np.sin(phi)], ls="dashed", color="tab:blue")



# phi's label
AngleAnnotation((-a*eps,0), (0,0), (a*np.cos(phi)-a*eps, a*np.sin(phi)), ax=ax,
                      size=75, text=r"$\varphi$", color="tab:orange",
                      text_kw={"color": "tab:orange", "size": 15, "xytext": (-4,-2),"textcoords":"offset points"})


# plot axis
ax.annotate("", xytext=(-2.8, 0), xy=(1, 0), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#cccccc", shrinkA=0, shrinkB=0))
ax.annotate("", xytext=(0, -2.1), xy=(0, 2.1), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="#cccccc", shrinkA=0, shrinkB=0))





ax.axis('off')
ax.set_xlim([-2.8,1])
ax.set_ylim([-2.5,2.5])
ax.set_aspect('equal')
plt.show()
plt.savefig("ea2.png",bbox_inches='tight', transparent=True)