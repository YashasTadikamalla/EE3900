from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

A = np.array([1,1,-2]).reshape((3,1))
U = (np.array([1,1,-2])/np.sqrt(6)).reshape((3,1))
O = np.array([0,0,0]).reshape((3,1))

OA = A-O
OU = U-O

L_OA = np.empty((2,3),float)
L_OA[0,:] = A[:,0]
L_OA[1,:] = O[:,0]

L_OU = np.empty((2,3),float)
L_OU[0,:] = U[:,0]
L_OU[1,:] = O[:,0]


plt.plot(L_OA[:,0],L_OA[:,1],L_OA[:,2],'r',label="OA")
plt.plot(L_OU[:,0],L_OU[:,1],L_OU[:,2],'y',label="OU")
ax.scatter(A[0],A[1],A[2],'o')
ax.text(1,1,-2, "A", color='blue')
ax.scatter(U[0],U[1],U[2],'o')
ax.text(1/np.sqrt(6),1/np.sqrt(6),-2/np.sqrt(6), "U", color='blue')
ax.scatter(0,0,0,'o')
ax.text(0,0,0, "O", color='blue')


plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.title('Unit vector OU along vector OA')
plt.show()

print('Vector OA is :\n',OA)
print('Unit Vector OU along OA is :\n',OU)