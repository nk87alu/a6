import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2+0.75*np.tanh(2*x)
    
def cenDiff(x, h):
    return (f(x+h)-f(x-h))/(2*h)
    
for h in [1,.5,.1]:
    x = np.arange(-2,2,h)
    deriv = cenDiff(x, h)
    plt.plot(x, deriv, 'o-', label=f'h= {h}')

x = np.arange(-2,2, .01)
exact = 1.5/(np.cosh(2*x)**2)
plt.plot(x, exact, 'm--', label='exact')

plt.legend()
plt.xlabel('x')
plt.ylabel('f `(x)')
plt.grid()
plt.show()
