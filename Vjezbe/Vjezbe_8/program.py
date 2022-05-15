from Projectile import Projectile
import matplotlib.pyplot as plt

projectile1 = Projectile(5)

projectile1.kosiHitac_Euler(0, 5, 45, dt=0.01, ro=2, C=1, A=10)

x_Euler = projectile1.x
y_Euler = projectile1.y

projectile1.kosiHitac_RungeKutta(0, 5, 45, dt=0.01, ro=2, C=1, A=10)

x_RungeKutta = projectile1.x
y_RungeKutta = projectile1.y

plt.plot(x_Euler, y_Euler, label="Euler")
plt.plot(x_RungeKutta, y_RungeKutta, label="Runge Kutta")
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.legend()

plt.show()



