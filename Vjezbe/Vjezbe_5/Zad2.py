# Razvijenom modulu dodajte metodu koja za zadane početne uvjete numerički računa period titranja. 
# Ispitajte preciznost metode u ovisnosti o veličini koraka ∆t

from harmonic_oscillator import HarmonicOscillator
import matplotlib.pyplot as plt
import numpy as np

HO = HarmonicOscillator()
HO.set_initial_conditions(0, 1)
delta_t = np.arange(0.01, 0.1, 0.01)
numericki_periodi = []

period_analiticki = 2*np.pi/np.sqrt(HO.k/HO.m)
analiticki_lista = []

for dt in delta_t:
    period= HO.period_titranja(dt)
    numericki_periodi.append(period)
    analiticki_lista.append(period_analiticki)

plt.plot(delta_t, analiticki_lista)
plt.scatter(delta_t, numericki_periodi)
plt.ylabel("Delta t [s]", fontsize=14)
plt.xlabel("Period T [s]", fontsize=14)
plt.show()
