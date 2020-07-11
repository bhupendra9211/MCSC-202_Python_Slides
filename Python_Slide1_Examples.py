# Program is created for MCSC-202-Lab Class
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi,2*np.pi,100)
y = np.sin(x)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of $\sin x$ ')
plt.show()
