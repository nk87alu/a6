import numpy as np 
import matplotlib.pyplot as plt 

e_o = 8.854e-12
q1 = 1 
q2 = -1

x1, y1 = -.05, 0
x2, y2 = .05, 0

x = np.arange(-.1, .1, .001)
y = np.arange(-.1,.1 .001)
X , Y = np.meshgrid(x,y)

r1 = np.sqrt((X-x1)**2+(Y-y1)**2)
r2 = np.sqrt((X-x2)**2+(Y-y2)**2)

r1 = np.where(r1<.001,.001,r1)
r2 = np.where(r2<.001,.001,r2)

V = (q1/(4*np.pi*e_o*r1))+(q2/(4*np.pi*e_o*r2))

plt.contour(X,Y,V,levels=100)
plt.colorbar()
#plt.savefig('potential.png')
plt.show()
