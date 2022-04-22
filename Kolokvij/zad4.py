from modul import ProjectileDrop
import matplotlib.pyplot as plt
import numpy as np

objekt = ProjectileDrop(2000, 200)

delta_t = np.arange(0.001, 0.1, 0.001)
vrijemeTrajanja = []

for dt in delta_t:
    vrijemeTrajanja.append(objekt.vrijemePadanja(dt))

plt.plot(delta_t, vrijemeTrajanja)
plt.title('Ovisnost vremena trajanja pada o koraku delta t')
plt.xlabel('dt [s]')
plt.ylabel('vrijeme trajanja t [s]')
plt.show()