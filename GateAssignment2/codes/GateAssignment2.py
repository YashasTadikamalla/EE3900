# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FeJbKtflPZ7PUL4EjIe4i0H-qPrTvBPC
"""

import numpy as np
import matplotlib.pyplot as plt

t = [-3,-2,-1,0,1,2,3,4,5,6]


plt.stem(t,[0,0,0,0,1,0,0,0,0,0])
plt.xlabel('n')
plt.ylabel('h_1[n]')
plt.grid()
plt.title('impulse response 1')
plt.show()


plt.stem(t,[0,0,0,0,0,1,0,0,0,0])
plt.xlabel('n')
plt.ylabel('h_2[n]')
plt.grid()
plt.title('impulse response 2')
plt.show()

plt.stem(t,[0,0,0,0,0,0,1,0,0,0])
plt.xlabel('n')
plt.ylabel('h[n]')
plt.grid()
plt.title('overall impulse response')
plt.show()