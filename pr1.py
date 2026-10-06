import numpy as np
import matplotlib.pyplot as plt

f = 2
t = np.linspace(0, 3*np.pi, 300)
y = np.sin(f*t)

plt.figure(num = 'График sin(x)', figsize=(10,6))

plt.plot(t,y)
plt.xlabel('t')
plt.ylabel('A')
#plt.title('график sin(x)')
plt.legend(['s(t)=Asin(2pi*f*t)'], loc = 'upper right')
plt.grid(True)
plt.xlim(0, max(t))
plt.show()
