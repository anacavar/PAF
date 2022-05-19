from turtle import color
from Projectile import Projectile
import matplotlib.pyplot as plt

kugla = Projectile(10, 0.5, 'kugla')

# META 1
kugla.postavi_metu(5, 2, 1)
circle = plt.Circle((kugla.x_mete, kugla.y_mete), radius = kugla.r_mete, fill=False)
plt.gca().add_patch(circle)
najprecizniji_kut = kugla.angle_to_hit_target(0, 100, 0.01, 10, 1)
print(kugla.mind_koordinate)
kugla.kosiHitac_Euler(0, 100, najprecizniji_kut, 0.01, 10, 1)
kugla_crtez = plt.Circle(kugla.mind_koordinate, radius = kugla.a, fill=True, color='red')
plt.gca().add_patch(kugla_crtez)
plt.plot(kugla.x, kugla.y, label='kugla1')

# META 2
kugla.postavi_metu(1, 2, 0.5)
circle = plt.Circle((kugla.x_mete, kugla.y_mete), radius = kugla.r_mete, fill=False)
plt.gca().add_patch(circle)
najprecizniji_kut = kugla.angle_to_hit_target(0, 100, 0.01, 10, 1)
print(kugla.mind_koordinate)
kugla.kosiHitac_Euler(0, 100, najprecizniji_kut, 0.01, 10, 1)
kugla_crtez = plt.Circle(kugla.mind_koordinate, radius = kugla.a, fill=True, color='red')
plt.gca().add_patch(kugla_crtez)
plt.plot(kugla.x, kugla.y, label='kugla2')

# META 3
kugla.postavi_metu(6, 5, 1)
circle = plt.Circle((kugla.x_mete, kugla.y_mete), radius = kugla.r_mete, fill=False)
plt.gca().add_patch(circle)
najprecizniji_kut = kugla.angle_to_hit_target(0, 100, 0.01, 10, 1)
print(kugla.mind_koordinate)
kugla.kosiHitac_Euler(0, 100, najprecizniji_kut, 0.01, 10, 1)
kugla_crtez = plt.Circle(kugla.mind_koordinate, radius = kugla.a, fill=True, color='red')
plt.gca().add_patch(kugla_crtez)
plt.plot(kugla.x, kugla.y, label='kugla3')

plt.gca().set_aspect('equal', adjustable='box')
plt.title("Gađanje meta")
plt.xlabel('x/m')
plt.ylabel('y/m')
plt.legend()
plt.show()