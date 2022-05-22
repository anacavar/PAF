# Napišite program koji crta putanju nabijene čestice u konstantnom električnom i magnetnom polju. 
# Demonstrirajte valjanost putanje za slučaj nabijene čestice koja se giba u konstatnom magnetnom polju B~ = (0, 0, B)
# i ima sve tri komponente početne brzine različite od 0. Kako se u tom slučaju giba elektron, a kako pozitron?

from cestica import Cestica
import matplotlib.pyplot as plt

B = 5 # u z smjeru

elektron = Cestica(0, 0, 0, 0, 0, B, -1, 1)
elektron.gibanje(0, 0, 0, 5, 5, 1)

pozitron = Cestica(0, 0, 0, 0, 0, B, 1, 1)
pozitron.gibanje(0, 0, 0, 5, 5, 1)

x_e, y_e, z_e = elektron.getCoordinates()
x_p, y_p, z_p = pozitron.getCoordinates()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x_e, y_e, z_e, label='elektron')
ax.plot(x_p, y_p, z_p, label='pozitron')
ax.legend()
ax.set_xlabel('x/m')
ax.set_ylabel('y/m')
ax.set_zlabel('z/m')
plt.show()
