import calculate as cal
import matplotlib.pyplot as plt
import numpy as np
import funkcije as fun

print(cal.derivacija_u_tocki(fun.sinus, 3.14/2))

x, y = cal.derivacija_u_intervalu(fun.kubna_formula, -10, 10)

dx=np.arange(0.01, 0.1, 0.03)

plt.subplot(2, 1, 1)
for e in dx:
    x, y = cal.derivacija_u_intervalu(fun.kubna_formula, -3, 3, e)
    plt.scatter(x, y, s=10)

x=np.arange(-3, 3, 0.1)

y = 3*x**2
plt.plot(x, y)
plt.title('Metoda tri koraka')
plt.xlabel('x')
plt.ylabel('df(x)/dx')

plt.subplot(2, 1, 2)
for e in dx:
    x, y = cal.derivacija_u_intervalu(fun.kubna_formula, -3, 3, e, False)
    plt.scatter(x, y, s=10)

x=np.arange(-3, 3, 0.1)

y = 3*x**2
plt.plot(x, y)
plt.title('Metoda dva koraka')
plt.xlabel('x')
plt.ylabel('df(x)/dx')
plt.tight_layout()
plt.show()