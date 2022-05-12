import matplotlib.pyplot as plt
from BungeeJump import BungeeJump
import numpy as np

skok1 = BungeeJump(100, 1, 1, 40, 0.001)

skok1.jump()

plt.plot(skok1.t, skok1.y)
plt.title("Ovisnost visine o vremenu")
plt.xlabel("t/s")
plt.xlabel("y/m")
plt.show()

plt.plot(skok1.t, skok1.E_gpot, label='E_gpot')
plt.plot(skok1.t, skok1.E_kin, label='E_kin')
plt.plot(skok1.t, skok1.E_pot, label='E_pot')
plt.plot(skok1.t, skok1.E_ukupna, label='E_uk')
plt.title("Ovisnost energija o vremenu")
plt.xlabel("t/s")
plt.ylabel("E/J")
plt.legend()

plt.show()

