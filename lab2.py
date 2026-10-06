import numpy as np
import matplotlib.pyplot as plt

# t = np.linspace(0,1,100)
# A = 5
# f = 5
# ph = 0
# x = A*np.sin(2*np.pi*f*t+ph)
#
# A_2 = 6
# f_2 = 4
# ph_2 = 0.25
# x_2 = A_2*np.sin(2*np.pi*f_2*t+ph_2)
#
# A_3 = 2
# f_3 = 7
# ph_3 = 0.5
# x_3 = A_3*np.sin(2*np.pi*f_3*t+ph_3)
#
# x_sum = x+x_2+x_3
#
# plt.figure(figsize = (12, 6))
# plt.plot(t, x, 'b')
# plt.plot(t, x_2, 'orange')
# plt.plot(t, x_3, 'g')
# plt.plot(t, x_sum, 'red')
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# plt.xlim(0, 1)
# plt.grid(True)
# plt.show()

#4
# f = 5
# T = 1 / f
# t = np.linspace(0, 5*T, 2000)
#
# x = (4/np.pi) * np.cos(2*np.pi*f*t - np.pi/2) + (4/(3*np.pi)) * np.cos(2*np.pi*3*f*t - np.pi/2)
#
# plt.figure(figsize=(12, 5))
# plt.plot(t, x)
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# plt.title('Сумма двух гармоник (формула 4)')
# plt.grid(True)
# plt.show()
#5
f = 5
T = 1 / f
t = np.linspace(0, 5 * T, 3000)

def sum(t, f, N_t):
    x = np.zeros_like(t)
    for n in range(N_t):
        odd = 2 * n + 1
        A = 4 / (odd * np.pi)
        x += A * np.cos(2 * np.pi * odd * f * t - np.pi / 2)
    return x

plt.figure(figsize=(12, 10))
N_list = [1, 2, 3, 4]

for i, N in enumerate(N_list, 1):
    x = sum(t, f, N)
    plt.subplot(2, 2, i)
    plt.plot(t, x)
    plt.title(f'Число слагаемых = {N}')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(True)

plt.tight_layout()
plt.show()