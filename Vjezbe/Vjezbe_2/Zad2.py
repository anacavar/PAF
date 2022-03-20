# Napišite program u kojem korisnik definira iznos početne brzine v0 u m/s i kut otklona θ u stupnjevima. Neka
# program crta x − y, x − t i y − t graf za prvih 10 sekundi gibanja u dvije dimenzije. Diferencijalne jednadžbe
# rješavajte numerički. Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.

import numpy as np
import matplotlib.pyplot as plt

def kosi_hitac(v0, kut0):

    x=[]
    y=[]
    v_y=[]
    t=[]
    x.append(0)
    y.append(0)
    t.append(0)
    v_x=np.cos(np.deg2rad(kut0))*v0
    v_y.append(np.sin(np.deg2rad(kut0))*v0)
    dt=0.1

    for i in range (100):
        g=9.81
        x.append(x[i]+v_x*dt)
        v_y.append(v_y[i]-g*dt)
        y.append(y[i]+v_y[i]*dt)
        t.append(t[i]+dt)

    plt.subplot(2, 2, 1)
    plt.plot(x, y)
    plt.title('x - y graf')
    plt.xlabel('x [s]')
    plt.ylabel('y [m]')
    plt.subplot(2, 2, 2)
    plt.plot(t, x)
    plt.title('x - t graf')
    plt.xlabel('t [s]')
    plt.ylabel('x [m]')
    plt.subplot(2, 2, 3)
    plt.plot(t, y)
    plt.title('y - t graf')
    plt.xlabel('t [s]')
    plt.ylabel('y [m]')
    plt.tight_layout()  
    plt.show()

kosi_hitac(75, 45)

