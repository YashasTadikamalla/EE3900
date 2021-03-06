import numpy as np
import matplotlib.pyplot as plt

def x(n):
  if (n == -1 or n == 0 or n == 1 or n == 2 or n == 3):
    return 1
  elif (n == 4):
    return 0.5
  else:
    return 0

def u(n):
  if (n >= 0):
    return 1
  else:
    return 0

A=np.linspace(-3,5,9)
A=A.astype(int)
y=np.zeros(9)
z=np.zeros(9)

for i in range(9):
  y[i]=x(2*A[i])

for i in range(9):
  z[i]=x(A[i])*u(2-A[i])

print(A)
print(y)
print(z)

plt.stem(A,y,use_line_collection = True)
plt.title("x[2n]")
plt.show()

plt.stem(A,z,use_line_collection = True)
plt.title("x[n]u[2-n]")
plt.show()
