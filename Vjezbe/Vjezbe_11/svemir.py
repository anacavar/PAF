import numpy as np
from planet import Planet

class Sustav():
    def __init__(self):
        self.planeti = []
        self.time = [0]

    def addPlanet(self, planet, r0, r0_kut, v0, v0_kut):
        self.planeti.append(planet)
        # preračunavanje kutova iz stupnjeva u radijane
        r0_kut = r0_kut*np.pi/180
        v0_kut = v0_kut*np.pi/180
        # računanje početnih koordinata
        x0 = r0*np.cos(r0_kut)
        y0 = r0*np.sin(r0_kut)
        v_x0 = v0*np.cos(v0_kut)
        v_y0 = v0*np.sin(v0_kut)
        # appendanje početnih vektora
        planet.r.append(np.array((x0, y0)))
        planet.v.append(np.array((v_x0, v_y0)))
        planet.x.append(planet.r[-1][0])
        planet.y.append(planet.r[-1][1])

    def __apply_gravity(self):
        # uspostavljanje međudjelovanja planeta prije početka gibanja
        for planet in self.planeti:
            planet.a.append(self.__gravitacija_na_planet(planet))

    def __gravitacija_na_planet(self, planet):
        # računa i vraća ukupnu akcečeraciju na pojedini planet u međudjelovanju sa svim ostalim tijelima u sustavu
        planets = [i for i in self.planeti]
        planets.remove(planet)
        F_ukupna = np.array((0, 0))
        for planet_i in planets:
            F_ukupna = np.add(F_ukupna, self.__gravitacija(planet, planet_i))
        a = F_ukupna/planet.mass
        return a

    def __gravitacija(self, planet1, planet2):
        #gravitacijska sila usmjerena od prvog planeta prema drugom
        G = 6.67*10**(-11) #newton-metre2-kilogram−2
        # G = 1
        r12 = np.subtract(planet2.r[-1], planet1.r[-1])
        r = np.sqrt(np.dot(r12, r12))
        F = G*planet1.mass*planet2.mass/r**3 * r12 # vektor u smjeru planeta 2
        return F

    def evolve(self, dt=60*60*24, t = 2*60*60*24*365.25):
        # prije gibanja postavimo odnose gravitacijskih sila na tijela
        self.__apply_gravity()
        # u svakom trenutku pomaknemo svaki planet za jedan korak
        while self.time[-1]<t:
            for planet in self.planeti:
                planet.a.append(self.__gravitacija_na_planet(planet))
                planet.move(dt)
            self.time.append(self.time[-1]+dt)

   