from modul import ProjectileDrop
import matplotlib.pyplot as plt

objekt = ProjectileDrop(2000, 200)

x, y, t, v_y = objekt.dropProjectile()

plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.title('Ovisnost visine projektila o položaju x')
plt.xlabel('x [m]')
plt.ylabel('y [m]')

plt.subplot(2, 1, 2)
plt.plot(v_y, t)
plt.title('Ovisnost apsolutnog iznosa vertikalne brzine projektila o vremenu')
plt.xlabel('t [s]')
plt.ylabel('v_y [m/s]')

plt.tight_layout()
plt.show()





