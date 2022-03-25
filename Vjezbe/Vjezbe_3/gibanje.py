import particle
import math

p1=particle.Particle()

p1.set_initial_conditions(1, 0, 0, 45)
p1.plot_trajectory()
p1.range()
print('Ukupno vrijeme gibanja je', p1.total_time(), 's')
print('Maksimalna brzina za vrijeme gibanja je', p1.max_speed(), 'm/s')

# Koristeći klasu Particle u programu "gibanje.py" kreirajte jedan objekt i postavite ga na neke od vrijednosti
# za koje ste analitički izračunali domet. Slaže li se numeričko rješenje s analitičkim? Koliko je odstupanje?

def analiticki_domet(v, kut0):
    domet=v**2*math.sin(2*math.radians(kut0))/9.81
    return domet

p = particle.Particle()
p.set_initial_conditions(1, 0, 0, 45)
domet_numericki=p.range()
domet_analiticki=analiticki_domet(1, 45)

print("Analitički domet je", domet_analiticki, 'm', "\nNumerički domet je", domet_numericki, 'm')
print("Odstupanje je", abs(domet_analiticki-domet_numericki), 'm' )

