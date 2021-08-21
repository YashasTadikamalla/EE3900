import numpy as np
from scipy.stats import bernoulli
import matplotlib.pyplot as plt


t = np.arange(-2,6,1)
h = [0,0,0,1,2,3,4,5]
x = [0,0,0,1,1,1,1,1]
y = [0,0,0,0,1,3,6,10]

plt.stem(t, h, markerfmt='o',use_line_collection=True)
plt.xlabel('t')
plt.ylabel('h(t)')
plt.grid()
plt.title('impulse response')
plt.show()

plt.stem(t, x, markerfmt='o',use_line_collection=True)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.title('input')
plt.show()

plt.stem(t, y, markerfmt='o',use_line_collection=True)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.title('output')
plt.show()