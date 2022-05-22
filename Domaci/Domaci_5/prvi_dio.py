# Napišite program koji crta putanju nabijene čestice u vremenski promjenjivom električnom i magnetnom
# polju. Demonstrirajte valjanost putanje za slučaj nabijene čestice koja se giba u vremenski promjenjivom
# magnetnom polju B~ (t) = (0, 0, B(t)) i ima sve tri komponente početne brzine različite od 0. Neka se magnetno
# polje mijenja linearno i neka u početnom trenutku iznosi B(t = 0) = 0, a u konačnom B(t = 10) = 1.
# • Usporedite putanju elektrona u konstantnom i vremenski promjenjivom magnetnom polju.
# • Usporedite putanje elektrona i pozitrona u vremenski promjenjivom magnetnom polju.

from cestica import Cestica
import matplotlib.pyplot as plt
import numpy as np

# čestica u vremenski promjenjivom magnetnom polju (polje linearno raste u z smjeru)
B0 = 0 # u z smjeru
elektron = Cestica(0, 0, 0, 0, 0, B0, -1, 1)
koeficijent_vremenske_ovisnosti_B = np.array((0, 0, 1)) # razlika se bolje vidi pri 10x većem koeficijentu od zadanog
# koeficijent_vremenske_ovisnosti_B = np.array((0, 0, 0.1)) 
koeficijent_vremenske_ovisnosti_E = np.array((0, 0, 0))
elektron.gibanje(0, 0, 0, 5, 5, 1, koeficijent_vremenske_ovisnosti_B, koeficijent_vremenske_ovisnosti_E)
x_Bt, y_Bt, z_Bt = elektron.getCoordinates()

# čestica u vremenski nepromjenjivom polju
B = 5 # u z smjeru
elektron = Cestica(0, 0, 0, 0, 0, B, -1, 1)
koeficijent_vremenske_ovisnosti_B = np.array((0, 0, 0))
koeficijent_vremenske_ovisnosti_E = np.array((0, 0, 0))
elektron.gibanje(0, 0, 0, 5, 5, 1, koeficijent_vremenske_ovisnosti_B, koeficijent_vremenske_ovisnosti_E)
x_B0, y_B0, z_B0 = elektron.getCoordinates()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x_B0, y_B0, z_B0, label='nepromjenjivo polje')
ax.plot(x_Bt, y_Bt, z_Bt, label='promjenjivo polje')
ax.set_xlabel('x/m')
ax.set_ylabel('y/m')
ax.set_zlabel('z/m')
ax.legend()
plt.show()



