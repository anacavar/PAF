# Koristeći modul "particle.py" nacrtajte grafove ovisnosti dometa i vremena trajanja gibanja o početnom
# kutu otklona za neku odabranu i fiksiranu vrijednost početne brzine v0.

import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('C:\\repos\\PAF\\Vjezbe\\Vjezbe_3')
import particle

p = particle.Particle()
pocetni_kut=np.arange(1, 91, 1)
domet=[]
trajanje_gibanja=[]

for kut0 in pocetni_kut:
    p.set_initial_conditions(10, 0, 0, kut0)
    domet.append(p.range())
    trajanje_gibanja.append(p.total_time())

plt.subplot(2, 1, 1)
plt.plot(pocetni_kut, domet)
plt.title('Ovisnost dometa o početnom kutu')
plt.xlabel('stupnjevi')
plt.ylabel('domet [m]')
plt.subplot(2, 1, 2)
plt.plot(pocetni_kut, trajanje_gibanja)
plt.title('Ovisnost trajanja gibanja o početnom kutu')
plt.xlabel('stupnjevi')
plt.ylabel('vrijeme trajanja gibanja [s]')
plt.tight_layout() 
plt.show()