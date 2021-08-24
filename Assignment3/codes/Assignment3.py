import numpy as np
import matplotlib.pyplot as plt

x = np.linspace( -10 , 10 , 150 )
y = np.linspace( -10 , 10 , 150 )
  
a, b = np.meshgrid( x , y )
  
C1 = a ** 2 + b ** 2 - 4*a + 5*b -2
C2 = a ** 2 + b ** 2 - 5*a + 6*b 
L=a-b-2
  
figure, axes = plt.subplots()
  
axes.contour( a , b , C1 , [0],colors='green' )
axes.contour( a , b , C2 , [0], colors='blue')
axes.contour( a , b , L , [0],colors='red')
axes.set_aspect( 1 )
plt.grid()
plt.title('Pair of circles with the associated radical axis')
plt.show()