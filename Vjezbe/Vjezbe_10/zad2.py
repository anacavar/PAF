from cestica import Cestica
import matplotlib.pyplot as plt

B = 5 # u z smjeru

elektron = Cestica(0, 0, 0, 0, 0, B, -1, 1)

elektron.gibanje(0, 0, 0, 5, 5, 1, dt=0.001)
x_e, y_e, z_e = elektron.getCoordinates()

elektron.gibanje_RungeKutta(0, 0, 0, 5, 5, 1, dt=0.001)
x_r, y_r, z_r = elektron.getCoordinates()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x_e, y_e, z_e, label='Euler')
ax.plot(x_r, y_r, z_r, label='Runge Kutta')
ax.legend()
ax.set_xlabel('x/m')
ax.set_ylabel('y/m')
ax.set_zlabel('z/m')
plt.show()
