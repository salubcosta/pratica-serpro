import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100, 0.1)
y = 2.7 ** x
# print(x,y)
plt.plot(x,y)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Exponencial")
plt.show()