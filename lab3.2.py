import numpy as np
import matplotlib.pyplot as plt

f = 1
T = 1/f
A = 1
tau = 0.4
t = np.linspace(0, T, 2000)
omega1 = 2 * np.pi * f
N = np.array([0, 1, 2, 3, 4, 5, 6])
omega = N * omega1

#прямоугольный сигнал
x = np.where(t < tau, A, 0)

a = []
b = []
#вычисление коэффициентов an, bn
for i in range(len(N)):
    n = N[i]
    if n == 0:
        an = (1 / T) * np.trapz(x, t)
        bn = 0.0
    else:
        an = (2 / T) * np.trapz(x * np.cos(n * omega1 * t), t)
        bn = (2 / T) * np.trapz(x * np.sin(n * omega1 * t), t)
    a.append(an)
    b.append(bn)

a = np.array(a)
b = np.array(b)

An = np.sqrt(a**2 + b**2)
phi = np.arctan(-b/a)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
# График прямоугольного сигнала
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
# Синтез сигнала
# Постоянная составляющая
s2 = a[0] * np.ones_like(t)
s4 = a[0] * np.ones_like(t)
s6 = a[0] * np.ones_like(t)

# Добавляем гармоники
for n in range(1, 3):      # 1 и 2 гармоника
    s2 += a[n]*np.cos(n*omega1*t) + b[n]*np.sin(n*omega1*t)

for n in range(1, 5):      # 1..4 гармоники
    s4 += a[n]*np.cos(n*omega1*t) + b[n]*np.sin(n*omega1*t)

for n in range(1, 7):      # 1..6 гармоник
    s6 += a[n]*np.cos(n*omega1*t) + b[n]*np.sin(n*omega1*t)

# График синтеза
plt.figure(figsize=(10, 5))
plt.plot(t, x,  'k', linewidth=2, label='Исходный сигнал')
plt.plot(t, s2, label='2 гармоники')
plt.plot(t, s4, label='4 гармоники')
plt.plot(t, s6, label='6 гармоник')
plt.title('Синтез сигнала')
plt.xlabel('t, с')
plt.ylabel('x(t)')
plt.grid(True)
plt.legend()

plt.show()