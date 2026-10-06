import numpy as np
import matplotlib.pyplot as plt

f = 5
T = 1/f
A = 1
phi = np.pi/4
t = np.linspace(0, T, 2000)
x = A * np.cos(2*np.pi*f*t + phi)
N = np.array([0,1,2,3,4])
omega1 = 2 * np.pi * f
omega = N * omega1

a = []
b = []
# Вычисление коэффициентов an, bn
for i in range(len(N)):
    n = N[i]
    an = 2/T * np.trapz(x * np.cos(n*2*np.pi*f*t), t)
    bn = 2/T * np.trapz(x * np.sin(n*2*np.pi*f*t), t)
    a.append(an)
    b.append(bn)

a = np.array(a)
b = np.array(b)

An = np.sqrt(a**2 + b**2)
phi = np.arctan(-b/a)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# График гармонического колебания
axes[0, 0].plot(t, x)
axes[0, 0].set_title("Сигнал x(t)")
axes[0, 0].set_xlabel("t, с")
axes[0, 0].set_ylabel("x(t)")
axes[0, 0].grid(True)

# Коэффициенты an, bn
axes[0, 1].stem(omega, a, label="an")
axes[0, 1].stem(omega, b, markerfmt="s", label="bn")
axes[0, 1].set_title("Коэффициенты an, bn")
axes[0, 1].set_xlabel("ω")
axes[0, 1].set_ylabel("Значение коэффициента")
axes[0, 1].legend()
axes[0, 1].grid(True)

# Амплитудный спектр
axes[1, 0].stem(omega, An)
axes[1, 0].set_title("Амплитудный спектр An")
axes[1, 0].set_xlabel("ω")
axes[1, 0].set_ylabel("An")
axes[1, 0].grid(True)

# Фазовый спектр
axes[1, 1].stem(omega, phi)
axes[1, 1].set_title("Фазовый спектр φ(n)")
axes[1, 1].set_xlabel("ω")
axes[1, 1].set_ylabel("φ(n), рад")
axes[1, 1].grid(True)

plt.tight_layout()
plt.show()