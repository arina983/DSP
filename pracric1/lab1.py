import numpy as np
import matplotlib.pyplot as plt

A = 5
f = 1
phi = 0.3 *np.pi
T = 1/f
t = np.linspace(0, 3*T, 300)
y = A*np.cos(2*np.pi*f*t + phi)
y_zero = A * np.cos(2*np.pi*f * t)

tau = phi/(2*np.pi*f)
print(f'временной сдвиг маскимума', tau)
print(f'период соответсвущий фазовому сдвигу', T)

T_2 = 6
f_2 = 1/T_2
moment = np.array([1, 3, 7])
for t_2 in moment:
    phi_2 = 2*np.pi*f_2*t_2
    print('момент времени', t_2)
    print(f'фазы колебания', phi_2)

# 1. Полярная форма для z = a + jb
a, b = 3, 4
z = complex(a, b)
r = np.abs(z)
phi = np.arctan(b/a)
print(f"z = {a} + {b}j")
print(f"Модуль: r = {r}")
print(f"Аргумент: φ = {np.degrees(phi):.2f}°")
print(f"Полярная форма: z = {r}·(cos({np.degrees(phi):.2f}°) + j·sin({np.degrees(phi):.2f}°))\n")

# 2. Из полярной в обычную
r2, phi2 = 4, np.radians(30)
a2 = r2 * np.cos(phi2)
b2 = r2 * np.sin(phi2)
print(f"Полярная форма: z = {r2}·(cos(30°) + j·sin(30°))")
print(f"Обычная форма: z = {a2:.3f} + {b2:.3f}j")

plt.figure(num = 'График cos(x)', figsize=(10,6))
plt.plot(t,y, 'b')
plt.plot(t, y_zero, 'r')
plt.xlabel('t')
plt.ylabel('A')
plt.grid(True)
plt.xlim(0, max(t))
plt.show()
