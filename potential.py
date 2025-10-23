import numpy as np
import matplotlib.pyplot as plt

e_o = 8.854e-12
q1 = 1
q2 = -1
x1, y1 = -.05, 0
x2, y2 = .05, 0
noHardCodeHere = .01
dx = .001

x = np.arange(-.1, .1, dx)
y = np.arange(-.1,.1, dx)
X , Y = np.meshgrid(x,y)

r1 = np.sqrt((X-x1)**2+(Y-y1)**2)
r2 = np.sqrt((X-x2)**2+(Y-y2)**2)

r1 = np.where(r1<noHardCodeHere,noHardCodeHere,r1)
r2 = np.where(r2<noHardCodeHere,noHardCodeHere,r2)

V = (q1/(4*np.pi*e_o*r1))+(q2/(4*np.pi*e_o*r2))

Ex = -(V[2:,: ]-V[0:-2, :])/(2*dx)
Ey = -(V[:,2:]-V[:, 0:-2])/(2*dx)

plt.contourf(X,Y,V,levels=60, cmap="bwr")
plt.colorbar()

Xnew = X[1:-1, 1:-1]
Ynew = Y[1:-1, 1:-1]
ExNew = Ex[:, 1:-1 ]
EyNew = Ey[1:-1 , :]
plt.streamplot(Xnew[0,:], Ynew[:,0], ExNew, EyNew,color='black', density=.75, linewidth=.33)

plt.savefig('potentialANDefield.png')                                          plt.show()
