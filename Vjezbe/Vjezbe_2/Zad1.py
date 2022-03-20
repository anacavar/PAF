# Napišite program u kojem korisnik definira iznos sile u N i masu čestice u kg, a program crta x − t, v − t
# i a − t graf za prvih 10 sekundi jednolikog gibanja u jednoj dimenziji. Diferencijalne jednadžbe rješavajte
# numerički. Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.

import matplotlib.pyplot as plt
import numpy as np

def jednolikoGibanje(F, m):

    a=F/m
    x=[0]
    t=[0]
    v=[0]
    a_list=[a]

    for i in range(100):
        dt = 0.1
        t.append(t[i]+dt)
        v.append(v[i]+a*dt)
        x.append(x[i]+v[i]*dt)
        a_list.append(a)
 
    fig, axs = plt.subplots(3)

    axs[0].plot(t, x)
    axs[0].title.set_text('Ovisnost položaja o vremenu')
    axs[0].set_xlabel('t [s]')
    axs[0].set_ylabel('x [m]')

    axs[1].plot(t, v)
    axs[1].title.set_text('Ovisnost brzine o vremenu')
    axs[1].set_xlabel('t [s]')
    axs[1].set_ylabel('v [m/s]')

    axs[2].plot(t, a_list)
    axs[2].title.set_text('Ovisnost akceleracije o vremenu')
    axs[2].set_xlabel('t [s]')
    axs[2].set_ylabel('a [m/s^2]')

    plt.tight_layout()
    plt.show()


jednolikoGibanje(5, 10)
