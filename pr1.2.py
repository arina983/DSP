import numpy as np
import matplotlib.pyplot as plt

f = 2
duration = 0.4

T = 1/f
t = np.linspace(0.0001, 3*T, 300)
y = np.where((t % T) < duration, 1, 0)

plt.figure(num = 'Прямоугольный сигнал', figsize=(10,6))
plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('A')
plt.grid(True)
plt.show()

#уметь рисовать графики sin и cos
#уметь рисовать прямоугольный сигнал и менять длительность при заданном периоде