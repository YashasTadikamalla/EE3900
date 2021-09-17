import numpy as np
import matplotlib.pyplot as plt
from math import *

# initialising variables and matrices
F=np.array([0,12]).T
n=np.array([0,1]).T
F_norm=12
n_norm=1
F=F.reshape(2,1)
n=n.reshape(2,1)
c=3
e=2
I=np.array([[1,0],[0,1]])
I=I.reshape(2,2)

# calculating V,u,f
V=(pow(n_norm,2)*I)-(pow(e,2)*(n@n.T))
u=(c*pow(n_norm,2)*n)-(pow(n_norm,2)*F)
f=(pow(n_norm,2)*pow(F_norm,2))-(pow(c,2)*pow(e,2))

print(V)
print(u)
print(f)

fig=plt.figure()
ax = fig.add_subplot(111)
len = 10000
y = np.linspace(-10,10,len)

def hyperbola_gen(y):
    x = np.sqrt(3*((y**2)-36))
    return x

#Generating the Standard Hyperbola
x = hyperbola_gen(y)
xStandardLeft = np.vstack((-x,y))
xStandardRight = np.vstack((x,y))

#Plotting points
A = np.array([0,12])
B = np.array([0,-12])
C = np.array([0,6])
D = np.array([0,-6])

#Plotting the standard hyperbola
plt.plot(xStandardLeft[0,:],xStandardLeft[1,:],label='Hyperbola',color='b')
plt.plot(xStandardRight[0,:],xStandardRight[1,:],color='b')

# Plotting the foci and vertices
plt.plot(A[0],A[1],'o',color='g',label='Focus1')
plt.text(0.5 ,11.5,'F1(0,12)')
plt.plot(B[0],B[1],'o',color='g',label='Focus2')
plt.text(0.5 ,-12.5,'F2(0,-12)')
plt.plot(C[0],C[1],'o',color='r',label='Vertex1')
plt.text(0.5 ,5.5,'B1(0,6)')
plt.plot(D[0],D[1],'o',color='r',label='Vertex2')
plt.text(0.5 ,-6.5,'B2(0,-6)')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()


# In[ ]:




