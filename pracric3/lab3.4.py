import numpy as np

Um = 1.0
cases = [(0.1, 0.05), (0.1, 0.025), (0.2, 0.05)]

for T, tau in cases:
    q = T / tau
    U0 = Um / q
    k = np.arange(1, 8)
    Uk = (2 * Um / (k * np.pi)) * np.abs(np.sin(k * np.pi * tau / T))
    print(f"T={T}, tau={tau}, q={q:.0f}, U0={U0:.3f}")
    print("  Uk:", " ".join(f"{v:.3f}" for v in Uk))