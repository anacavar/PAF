# Za česticu početne brzine v0 = 10 m/s i kuta otklona θ = 60o nacrtajte graf ovisnoti relativne pogreške
# numeričkog riješenja o vrijednosti vremenskog koraka ∆t.

import particle
import numpy as np
import matplotlib.pyplot as plt

p = particle.Particle()
p.set_initial_conditions(10, 0, 0, 60)


def relativna_pogreska(delta_t):
    rel_pogreska = []
    domet_analiticki=p.analiticki_domet()
    for dt in delta_t:
        p.set_initial_conditions(10, 0, 0, 60)
        domet_numericki=p.range(dt)
        p.reset()
        rel = abs(domet_analiticki-domet_numericki)/domet_analiticki*100
        rel_pogreska.append(rel)
    return rel_pogreska #vraća listu

delta_t = np.arange(0.00001, 0.12, 0.001)
rel_pog = relativna_pogreska(delta_t)

plt.plot(delta_t, rel_pog)
plt.title('Ovisnost relativne pogreške o vremenskom koraku')
plt.xlabel("∆t [s]")
plt.ylabel("Relativna pogreška [%]")
plt.show()


