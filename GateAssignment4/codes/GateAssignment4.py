import matplotlib.pyplot as plt
import numpy as np
import math

fs=np.linspace(-2,2,70)

def X(f):
  if (f>2 or f<-2):
    return 0
  else:
    return (math.sin(math.pi*f))/(math.pi*f)

vals=[]

for i in fs:
  vals.append(X(i))

plt.plot(fs,vals)
plt.ylabel('X(f)')
plt.xlabel('f')
plt.grid()
plt.show()
