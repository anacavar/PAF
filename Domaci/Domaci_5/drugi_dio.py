# • Usporedite putanje elektrona i pozitrona u vremenski promjenjivom magnetnom polju.

from cestica import Cestica
import matplotlib.pyplot as plt
import numpy as np

B0 = 0 # u z smjeru
elektron = Cestica(0, 0, 0, 0, 0, B0, -1, 1)
pozitron = Cestica(0, 0, 0, 0, 0, B0, 1, 1)

# elektron u vremenski promjenjivom magnetnom polju (polje linearno raste u z smjeru)
koeficijent_vremenske_ovisnosti_B = np.array((0, 0, 1))  # razlika se bolje vidi pri 10x većem koeficijentu od zadanog
# koeficijent_vremenske_ovisnosti_B = np.array((0, 0, 0.1))
koeficijent_vremenske_ovisnosti_E = np.array((0, 0, 0))
elektron.gibanje(0, 0, 0, 5, 5, 1, koeficijent_vremenske_ovisnosti_B, koeficijent_vremenske_ovisnosti_E)
x_e, y_e, z_e = elektron.getCoordinates()

# pozitron u vremenski promjenjivom magnetnom polju (polje linearno raste u z smjeru)
koeficijent_vremenske_ovisnosti_B = np.array((0, 0, 1)) # razlika se bolje vidi pri 10x većem koeficijentu od zadanog
# koeficijent_vremenske_ovisnosti_B = np.array((0, 0, 0.1))
koeficijent_vremenske_ovisnosti_E = np.array((0, 0, 0))
pozitron.gibanje(0, 0, 0, 5, 5, 1, koeficijent_vremenske_ovisnosti_B, koeficijent_vremenske_ovisnosti_E)
x_p, y_p, z_p = pozitron.getCoordinates()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x_e, y_e, z_e, label='elektron')
ax.plot(x_p, y_p, z_p, label='pozitron')
ax.set_xlabel('x/m')
ax.set_ylabel('y/m')
ax.set_zlabel('z/m')
ax.legend()
plt.show()