import numpy as np

T = 3
f1 = 1/T
t = np.linspace(0, T, 2000)
f2 = 1/T*3

s1 = np.sin(2*np.pi*f1*t)
for n in range(1, 11):
    sn = np.sin(2 * np.pi * n * f1 * t)
    integral = np.trapz(s1 * sn, t)
    print(f"{n:2} | {integral:12.6e}")
print("-----------------\n")

# Изменение частоты
s2 = np.sin(2*np.pi*f2*t)
for n in range(1, 11):
    sn = np.sin(2 * np.pi * n * f1 * t)
    integral = np.trapz(s2 * sn, t)
    print(f"{n:2} | {integral:12.6e}")
print("-----------------\n")

# Изменение интервала
print("Интервал интегрирования изменён: [0, T + 0.05]")
t2 = np.linspace(0, T + 0.05, 2000)
s3 = np.sin(2 * np.pi * f1 * t2)

print("n |  интеграл")
print("-" * 25)
for n in range(1, 11):
    sn_2 = np.sin(2 * np.pi * n * f1 * t2)
    integral = np.trapz(s3 * sn_2, t2)
    print(f"{n:2} | {integral:12.6e}")
print("-----------------\n")

# Комплексные экспоненты
e = np.exp(1j * 2*np.pi*n*f1*t)
pairs = [(1, 2), (1, -1), (3, -3), (5, 7), (-2, 4), (0, 1), (2, 2)]

print("Экспонента")
print("\nk  |  n  |  |интеграл|")
print("-" * 30)
for k, n in pairs:
    sk = np.exp(1j * 2 * np.pi * k * f1 * t)   # массив для k
    sn = np.exp(1j * 2 * np.pi * n * f1 * t)   # массив для n
    integral = np.trapz(sk * np.conj(sn), t)
    print(f"{k:2} | {n:2} | {np.abs(integral):12.6e}")

# Изменение частоты
print("\n" + "-" * 50)
print("Частота одной экспоненты изменена")
sk = np.exp(1j * 2 * np.pi * 1 * f1 * t)
sn_bad = np.exp(1j * 2 * np.pi * 1.7 * f1 * t)
integral = np.trapz(sk * np.conj(sn_bad), t)
print(f"{np.abs(integral):.6e}")

# Изменение интервала
print("\n" + "-" * 50)
print("Интервал [0, T+0.03]")
t3 = np.linspace(0, T + 0.03, 2000, endpoint=False)
sk = np.exp(1j * 2 * np.pi * 1 * f1 * t3)
sn = np.exp(1j * 2 * np.pi * 2 * f1 * t3)
integral = np.trapz(sk * np.conj(sn), t3)
print(f"|∫ s1·s2*| = {np.abs(integral):.6e}")