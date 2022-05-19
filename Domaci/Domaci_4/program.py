from Projectile import Projectile
import matplotlib.pyplot as plt

#uzet je a tako da je promjer kugle jednak bridu kocke radi usporedbe gibanja
kugla = Projectile(10, 0.5, 'kugla')
kocka = Projectile(10, 1, 'kocka')

kugla.kosiHitac_Euler(0, 10, 45, 0.01, 10, 1)
kocka.kosiHitac_Euler(0, 10, 45, 0.01, 10, 1)

plt.plot(kugla.x, kugla.y, label='kugla')
plt.plot(kocka.x, kocka.y, label='kocka')
plt.xlabel('x/m')
plt.ylabel('y/m')

plt.legend()
plt.show()


