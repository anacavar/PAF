import numpy
from planet import Planet
from svemir import Sustav
import matplotlib.pyplot as plt
import matplotlib.animation as ani

SuncevSustav = Sustav()

# PODACI O PLANETIMA
masaSunca = 1.989 * 10**30 #kg
radijusSunca = 6.96340 * 10**8 #m

masaMerkura = 3.285 * 10**23 #kg
radijusMerkura = 2.4397 * 10**6 #m
udaljenostMerkura = 5.79*10**10  #m
brzinaMerkura = 4.79*10**4 #m/s

masaVenere = 4.867 * 10**24 #kg
radijusVenere = 6.0518 * 10**6 #m
udaljenostVenere =  1.082*10**11 #m
brzinaVenere = 3.50*10**4 #m/s

masaZemlje = 5.972 * 10**24 #kg
radijusZemlje = 6.371 * 10**6 #m
udaljenostZemlje = 1.496*10**11 #m
brzinaZemlje = 2.98 * 10**4 #m/s

masaMarsa = 6.39 * 10**23 #kg
radijusMarsa = 3.3895 * 10**6 #m
udaljenostMarsa = 2.279*10**11 #m
brzinaMarsa = 2.41*10**4 #m/s

masaJupitra =  1.898 * 10**27 #kg
radijusJupitra = 6.9911 * 10**7 #m
udaljenostJupitra = 7.786*10**11 #m
brzinaJupitra =1.31*10**4 #m/s

masaSaturna = 5.683 * 10**26 #kg
radijusSaturna = 5.8232 * 10**7 #m
udaljenostSaturna = 1.4335*10**12 #m
brzinaSaturna = 9.7 *10**3 #m/s

masaUrana = 8.681 * 10**25 #kg
radijusUrana = 2.5362 * 10**7 #m
udaljenostUrana = 2.8725*10**12 #m
brzinaUrana =  6.8*10**3 #m/s

masaNeptuna = 1.024 * 10**26 #kg
radijusNeptuna = 2.4622 * 10**7 #m
udaljenostNeptuna = 4.4951*10**12 #m
brzinaNeptuna = 5.4*10**3 #m/s

Sunce = Planet(masaSunca, radijusSunca)
Merkur = Planet(masaMerkura, radijusMerkura)
Venera = Planet(masaVenere, radijusVenere)
Zemlja = Planet(masaZemlje, radijusZemlje)
Mars = Planet(masaMarsa, radijusMarsa)
Jupiter = Planet(masaJupitra, radijusJupitra)
Saturn = Planet(masaSaturna, radijusSaturna)
Uran = Planet(masaUrana, radijusUrana)
Neptun = Planet(masaNeptuna, radijusNeptuna)

SuncevSustav.addPlanet(Sunce, 0, 0, 0, 90)
SuncevSustav.addPlanet(Merkur, udaljenostMerkura, 0, brzinaMerkura, 90)
SuncevSustav.addPlanet(Venera, udaljenostVenere, 0, brzinaVenere, 90)
SuncevSustav.addPlanet(Zemlja, udaljenostZemlje, 0, brzinaZemlje, 90)
SuncevSustav.addPlanet(Mars, udaljenostMarsa, 0, brzinaMarsa, 90)
SuncevSustav.addPlanet(Jupiter, udaljenostJupitra, 0, brzinaJupitra, 90)
SuncevSustav.addPlanet(Saturn, udaljenostSaturna, 0, brzinaSaturna, 90)
SuncevSustav.addPlanet(Uran, udaljenostUrana, 0, brzinaUrana, 90)
SuncevSustav.addPlanet(Neptun, udaljenostNeptuna, 0, brzinaNeptuna, 90)

SuncevSustav.evolve()

fig = plt.figure()
plt.title('Graf')
plt.axis('equal')

# ANIMACIJA
def animation_frame(i):
    plt.plot(Sunce.x[:i], Sunce.y[:i], label = "Sunce", color = "yellow")
    plt.plot(Merkur.x[:i], Merkur.y[:i], label = "Merkur", color = "brown")
    plt.plot(Venera.x[:i], Venera.y[:i], label = "Venera", color = "orange")
    plt.plot(Zemlja.x[:i], Zemlja.y[:i], label = "Zemlja", color = "green")
    plt.plot(Mars.x[:i], Mars.y[:i], label = "Mars", color = "red")
    plt.plot(Jupiter.x[:i], Jupiter.y[:i], label = "Jupiter", color = "cyan")
    plt.plot(Saturn.x[:i], Saturn.y[:i], label = "Saturn", color = "grey")
    plt.plot(Uran.x[:i], Uran.y[:i], label = "Uran", color = "pink")
    plt.plot(Neptun.x[:i], Neptun.y[:i], label = "Neptun", color = "blue")

animator = ani.FuncAnimation(fig, animation_frame, 2000)

# plt.plot(Sunce.x, Sunce.y, label = "Sunce")
# plt.plot(Merkur.x, Merkur.y, label = "Merkur")
# plt.plot(Venera.x, Venera.y, label = "Venera")
# plt.plot(Zemlja.x, Zemlja.y, label = "Zemlja")
# plt.plot(Mars.x, Mars.y, label = "Mars")
# plt.plot(Jupiter.x, Jupiter.y, label = "Jupiter")
# plt.plot(Saturn.x, Saturn.y, label = "Saturn")
# plt.plot(Uran.x, Uran.y, label = "Uran")
# plt.plot(Neptun.x, Neptun.y, label = "Neptun")

plt.legend()
plt.show()



