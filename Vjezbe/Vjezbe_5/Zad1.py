# Koristeći razvijeni modul
# nacrtajte x − t, v − t i a − t graf za neke proizvoljno odabrane početne parametre. Ispitajte preciznost
# numeričkog rješenja za različite korake ∆t.

from harmonic_oscillator import HarmonicOscillator
import matplotlib.pyplot as plt
import numpy as np

HO = HarmonicOscillator()
HO.set_initial_conditions(0, 1)
HO.gibanje(0.01)

plt.subplot(3, 1, 1)
plt.plot(HO.t, HO.x)
plt.title("x-t graf")
plt.xlabel("t[s]")
plt.ylabel("x[m]")

plt.subplot(3, 1, 2)
plt.plot(HO.t, HO.v)
plt.title("v-t graf")
plt.xlabel("t[s]")
plt.ylabel("v[m/s]")

plt.subplot(3, 1, 3)
plt.plot(HO.t, HO.a)
plt.title("a-t graf")
plt.xlabel("t[s]")
plt.ylabel("a[m/s^2]")

plt.tight_layout()
plt.show()

deltat = [0.01, 0.1, 1]

for dt in deltat:
    HO.gibanje(dt)
    plt.scatter(HO.t, HO.x, s=5)

t_analiticko, x_analiticko = HO.analiticko_rjesenje()
plt.plot(t_analiticko, x_analiticko, 'r-')
plt.title('Usporedba numerickih rjesenja H.O. s analitickim')
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.show()
