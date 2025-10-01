import numpy as np
import matplotlib.pyplot as plt

#%%
# gaussian



def f(x):
    return np.exp(-(x-mu)**2/2./sigma**2)/np.sqrt(2*np.pi)/sigma


mu = 5
sigma = 1

x = np.linspace(mu-4*sigma,mu+4*sigma,num=200)

fig, ax = plt.subplots(1, 1, figsize=(12, 4)) 

ax.plot(x,f(x), lw=3)

ax.plot([mu,mu],[0,f(mu)], c="#cccccc", lw=2, ls="--", zorder=-1)
ax.plot([mu-sigma,mu-sigma],[0,f(mu-sigma)], c="#cccccc", lw=2, ls="--", zorder=-1)
ax.plot([mu+sigma,mu+sigma],[0,f(mu+sigma)], c="#cccccc", lw=2, ls="--", zorder=-1)
ax.plot([mu-2*sigma,mu-2*sigma],[0,f(mu-2*sigma)], c="#cccccc", lw=2, ls="--", zorder=-1)
ax.plot([mu+2*sigma,mu+2*sigma],[0,f(mu+2*sigma)], c="#cccccc", lw=2, ls="--", zorder=-1)
ax.plot([mu-3*sigma,mu-3*sigma],[0,f(mu-3*sigma)], c="#cccccc", lw=2, ls="--", zorder=-1)
ax.plot([mu+3*sigma,mu+3*sigma],[0,f(mu+3*sigma)], c="#cccccc", lw=2, ls="--", zorder=-1)

ax.text(mu, -f(mu)*0.1, r"$\mu$", ha="center", color="k")
ax.text(mu-sigma, -f(mu)*0.1, r"$\mu-\sigma$", ha="center", color="k")
ax.text(mu+sigma, -f(mu)*0.1, r"$\mu+\sigma$", ha="center", color="k")
ax.text(mu-2*sigma, -f(mu)*0.1, r"$\mu-2\sigma$", ha="center", color="k")
ax.text(mu+2*sigma, -f(mu)*0.1, r"$\mu+2\sigma$", ha="center", color="k")
ax.text(mu-3*sigma, -f(mu)*0.1, r"$\mu-3\sigma$", ha="center", color="k")
ax.text(mu+3*sigma, -f(mu)*0.1, r"$\mu+3\sigma$", ha="center", color="k")

ax.text(mu, f(mu)*1.05, r"50%", ha="center", color="k")
ax.text(mu-sigma*1.4, f(mu-sigma)*1.05, r"15.9%", ha="center", color="k")
ax.text(mu+sigma*1.4, f(mu+sigma)*1.05, r"84.1%", ha="center", color="k")
ax.text(mu-2.2*sigma, f(mu-2*sigma)*1.4, r"2.3%", ha="center", color="k")
ax.text(mu+2.2*sigma, f(mu+2*sigma)*1.4, r"97.7%", ha="center", color="k")
ax.text(mu-3.1*sigma, f(mu-3*sigma)*3, r"0.2%", ha="center", color="k")
ax.text(mu+3.1*sigma, f(mu+3*sigma)*3, r"99.8%", ha="center", color="k")

# plot axis
ax.annotate("", xytext=(mu-5.5*sigma, 0), xy=(mu+5.5*sigma, 0), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="k", shrinkA=0, shrinkB=0))
ax.annotate("", xytext=(0, -f(mu)*0.1), xy=(0, f(mu)*1.1), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="k", shrinkA=0, shrinkB=0))

ax.text(mu+5.7*sigma, 0, r"$x$", ha="center", color="k")
ax.text(0, f(mu)*1.15, r"$P(x)$", ha="center", color="k")


ax.axis('off')
ax.set_xlim([mu-6*sigma,mu+6*sigma])
ax.set_ylim([-f(mu)*0.1,f(mu)*1.2])
#ax.set_aspect('equal')
#plt.show()
plt.savefig("gauss1.png",bbox_inches='tight', transparent=True)

#%%

mu = 5
sigma = 1

x = np.linspace(mu-4*sigma,mu+4*sigma,num=200)

fig, ax = plt.subplots(1, 1, figsize=(12, 4)) 

ax.plot(x,f(x), lw=3)

ax.plot([mu,mu],[0,f(mu)], c="#cccccc", lw=2, ls="--", zorder=-1)
ax.plot([mu-sigma,mu-sigma],[0,f(mu-sigma)], c="#cccccc", lw=2, ls="--", zorder=-1)
ax.plot([mu+sigma,mu+sigma],[0,f(mu+sigma)], c="#cccccc", lw=2, ls="--", zorder=-1)
ax.plot([mu-2*sigma,mu-2*sigma],[0,f(mu-2*sigma)], c="#cccccc", lw=2, ls="--", zorder=-1)
ax.plot([mu+2*sigma,mu+2*sigma],[0,f(mu+2*sigma)], c="#cccccc", lw=2, ls="--", zorder=-1)

ax.text(mu, -f(mu)*0.1, r"$U_0$", ha="center", color="k")
#ax.text(mu-sigma, -f(mu)*0.1, r"$\mu-\sigma$", ha="center", color="k")
#ax.text(mu+sigma, -f(mu)*0.1, r"$\mu+\sigma$", ha="center", color="k")
#ax.text(mu-2*sigma, -f(mu)*0.1, r"$\mu-2\sigma$", ha="center", color="k")
#ax.text(mu+2*sigma, -f(mu)*0.1, r"$\mu+2\sigma$", ha="center", color="k")

ax.annotate("", xytext=(mu-sigma, f(mu)*0.08), xy=(mu, f(mu)*0.08), zorder=-2,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec="r", shrinkA=0, shrinkB=0))
ax.annotate("", xytext=(mu, f(mu)*0.08), xy=(mu+sigma, f(mu)*0.08), zorder=-2,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec="r", shrinkA=0, shrinkB=0))
ax.annotate("", xytext=(mu-2*sigma, f(mu)*0.08), xy=(mu-sigma, f(mu)*0.08), zorder=-2,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec="r", shrinkA=0, shrinkB=0))
ax.annotate("", xytext=(mu+sigma, f(mu)*0.08), xy=(mu+2*sigma, f(mu)*0.08), zorder=-2,
            arrowprops=dict(arrowstyle="<->, head_length=0.6, head_width=0.3", ec="r", shrinkA=0, shrinkB=0))

ax.text(mu, f(mu)*1.05, r"50%", ha="center", color="k")
ax.text(mu-sigma*1.4, f(mu-sigma)*1.05, r"15.9%", ha="center", color="k")
ax.text(mu+sigma*1.4, f(mu+sigma)*1.05, r"84.1%", ha="center", color="k")
ax.text(mu-2.2*sigma, f(mu-2*sigma)*1.4, r"2.3%", ha="center", color="k")
ax.text(mu+2.2*sigma, f(mu+2*sigma)*1.4, r"97.7%", ha="center", color="k")
ax.text(mu-3.1*sigma, f(mu-3*sigma)*3, r"0.2%", ha="center", color="k")
ax.text(mu+3.1*sigma, f(mu+3*sigma)*3, r"99.8%", ha="center", color="k")



ax.text(mu+0.5*sigma, f(mu)*0.1, r"$T\sqrt{kC_V}$", ha="center", color="r")
ax.text(mu-0.5*sigma, f(mu)*0.1, r"$T\sqrt{kC_V}$", ha="center", color="r")
ax.text(mu+1.5*sigma, f(mu)*0.1, r"$T\sqrt{kC_V}$", ha="center", color="r")
ax.text(mu-1.5*sigma, f(mu)*0.1, r"$T\sqrt{kC_V}$", ha="center", color="r")

# plot axis
ax.annotate("", xytext=(mu-5.5*sigma, 0), xy=(mu+5.5*sigma, 0), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="k", shrinkA=0, shrinkB=0))
ax.annotate("", xytext=(0, -f(mu)*0.1), xy=(0, f(mu)*1.1), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="k", shrinkA=0, shrinkB=0))

ax.text(mu+5.7*sigma, 0, r"$x$", ha="center", color="k")
ax.text(0, f(mu)*1.15, r"$P(x)$", ha="center", color="k")


ax.axis('off')
ax.set_xlim([mu-6*sigma,mu+6*sigma])
ax.set_ylim([-f(mu)*0.1,f(mu)*1.2])
#ax.set_aspect('equal')
plt.show()
plt.savefig("gauss2.png",bbox_inches='tight', transparent=True)


#%%
# maxwell-boltzmann

m=1

def g(v,kT):
    return np.sqrt(2*m**3/np.pi/kT**3)*v**2*np.exp(-m*v**2/2/kT)

#avg_v = np.sqrt(8*kT/np.pi/m)

#rms_v = np.sqrt(3*kT/m)

#prob_v = np.sqrt(2*kT/m)


v = np.linspace(0,20,num=200)


fig, ax = plt.subplots(1, 1, figsize=(12, 4.5)) 

ax.plot(v,g(v,5), lw=3, c="tab:blue")
ax.plot(v,g(v,10), lw=3, c="tab:green")
ax.plot(v,g(v,20), lw=3, c="tab:red")

ax.text(4.6, g(2.9,5), r"Small T", ha="center", color="tab:blue")
ax.text(10, g(8.5,20), r"Large T", ha="center", color="tab:red")

# plot axis
ax.annotate("", xytext=(-1, 0), xy=(21, 0), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="k", shrinkA=0, shrinkB=0))
ax.annotate("", xytext=(0, -0.03), xy=(0, 0.3), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="k", shrinkA=0, shrinkB=0))

ax.text(21.5, 0, r"$v$", ha="center", color="k")
ax.text(0, 0.31, r"$f(v)$", ha="center", color="k")



ax.axis('off')
ax.set_xlim([-1,22])
ax.set_ylim([-0.03,0.3])
plt.show()
plt.savefig("MB1.png",bbox_inches='tight', transparent=True)


#%%

m=1
kT = 15

avg_v = np.sqrt(8*kT/np.pi/m)

rms_v = np.sqrt(3*kT/m)

prob_v = np.sqrt(2*kT/m)


v = np.linspace(0,20,num=200)


fig, ax = plt.subplots(1, 1, figsize=(12, 3)) 


ax.plot(v,g(v,kT), lw=3, c="tab:red")
ax.plot([avg_v, avg_v], [0,g(avg_v,kT)], c="#cccccc", lw=2, ls="--", zorder=-1)
ax.plot([rms_v, rms_v], [0,g(rms_v,kT)], c="#cccccc", lw=2, ls="--", zorder=-1)
ax.plot([prob_v, prob_v], [0,g(prob_v,kT)], c="#cccccc", lw=2, ls="--", zorder=-1)


ax.text(avg_v, -0.01, r"$v_\text{avg}$", ha="center", color="k")
ax.text(rms_v, -0.01, r"$v_\text{rms}$", ha="left", color="k")
ax.text(prob_v, -0.01, r"$v_\text{mp}$", ha="right", color="k")


# plot axis
ax.annotate("", xytext=(-1, 0), xy=(21, 0), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="k", shrinkA=0, shrinkB=0))
ax.annotate("", xytext=(0, -0.03), xy=(0, 0.18), zorder=-5,
            arrowprops=dict(arrowstyle="->, head_length=0.6, head_width=0.3", ec="k", shrinkA=0, shrinkB=0))

ax.text(21.5, 0, r"$v$", ha="center", color="k")
ax.text(0, 0.19, r"$f(v)$", ha="center", color="k")



ax.axis('off')
ax.set_xlim([-1,22])
ax.set_ylim([-0.03,0.18])
plt.show()
plt.savefig("MB2.png",bbox_inches='tight', transparent=True)



