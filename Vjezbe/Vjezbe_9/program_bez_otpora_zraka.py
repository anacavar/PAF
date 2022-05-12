import matplotlib.pyplot as plt
from BungeeJump import BungeeJump
import numpy as np

skok2 = BungeeJump(100, 1, 1, 40, 0)

skok2.jump()

plt.plot(skok2.t, skok2.y)
plt.title("Ovisnost visine o vremenu")
plt.xlabel("t/s")
plt.xlabel("y/m")
plt.show()

plt.plot(skok2.t, skok2.E_gpot, label='E_gpot')
plt.plot(skok2.t, skok2.E_kin, label='E_kin')
plt.plot(skok2.t, skok2.E_pot, label='E_pot')
plt.plot(skok2.t, skok2.E_ukupna, label='E_uk')
plt.title("Ovisnost energija o vremenu")
plt.xlabel("t/s")
plt.ylabel("E/J")
plt.legend()

plt.show()

