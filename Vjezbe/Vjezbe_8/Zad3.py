from Projectile import Projectile
import matplotlib.pyplot as plt
import numpy as np

projectile1 = Projectile(5)

C = np.arange(0.01, 10, 0.01)
ranges1 = []

for cd in C:
    projectile1.kosiHitac_RungeKutta(0, 5, 45, dt=0.01, ro=2, C=cd, A=10)
    ranges1.append(projectile1.x[-1])

mass = np.arange(1, 100, 1)
ranges2 = []

for m in mass:
    projectile = Projectile(m)
    projectile.kosiHitac_RungeKutta(0, 5, 45, dt=0.01, ro=2, C=1, A=10)
    ranges2.append(projectile.x[-1])

plt.subplot(2, 1, 1)
plt.plot(C, ranges1)
plt.title('Ovisnost dometa projektila o koeficijentu trenja Cd')
plt.xlabel('Cd')
plt.ylabel('x [m]')
plt.subplot(2, 1, 2)
plt.plot(mass, ranges2)
plt.title('Ovisnost dometa projektila o masi projektila')
plt.xlabel('mass [kg]')
plt.ylabel('v [m/s]')

plt.tight_layout()  
plt.show()

