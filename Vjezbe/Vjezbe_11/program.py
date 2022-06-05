import numpy
from planet import Planet
from svemir import Sustav
import matplotlib.pyplot as plt
import matplotlib.animation as ani

SuncevSustav = Sustav()

# PODACI O PLANETIMA
masaSunca = 1.989 * 10**30 #kg
radijusSunca = 6.96340 * 10**8 #m

masaZemlje = 5.972 * 10**24 #kg
radijusZemlje = 6.371 * 10**6 #m
perihelionZemlje = 1.47098291 * 10**11 #m
brzinaZemlje = 30.29 * 10**3 #m/s

Sunce = Planet(masaSunca, radijusSunca)
Zemlja = Planet(masaZemlje, radijusZemlje)
SuncevSustav.addPlanet(Sunce, 0, 0, 0, 90)
SuncevSustav.addPlanet(Zemlja, perihelionZemlje, 0, brzinaZemlje, 90)

SuncevSustav.evolve()

fig = plt.figure()
plt.title('Graf')

# ANIMACIJA
# def animation_frame(i):
#     plt.scatter(Sunce.x[:i], Sunce.y[:i], color = 'blue')
#     plt.plot(Zemlja.x[:i], Zemlja.y[:i], color = 'red')

# animator = ani.FuncAnimation(fig, animation_frame, 2000)

plt.plot(Zemlja.x, Zemlja.y, label = "Zemlja")
plt.plot(Sunce.x, Sunce.y, label = "Sunce")

plt.legend()
plt.show()


