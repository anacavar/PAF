
from re import X
import numpy as np
import matplotlib.pyplot as plt

class ProjectileDrop():
    def __init__(self, h, v_x):
        self.h0 = h
        self.v_x = v_x
        print('Objekt uspješno stvoren. Visina objekta je:', self.h0, 'm, brzina objekta je:', self.v_x, 'm/s.')

    def promijeniVisinu(self, h_new):
        self.h0 = h_new
        return self.h0
    
    def promijeniBrzinu(self, v_new):
        self.v_x = self.v_x + v_new 
        return self.v_x

    def dropProjectile(self, dt=0.01, vjetar = 0):
        self.x = [0]
        self.a_x = vjetar
        self.vx_projektila = [self.v_x]
        self.h = [self.h0]
        self.vy = [0]
        self.t = [0]
        g = 9.81 #m/s^2

        while self.h[-1]>0:
            self.x.append(self.x[-1]+self.vx_projektila[-1]*dt)
            self.t.append(self.t[-1]+dt)
            self.vy.append(self.vy[-1]+dt*g)
            self.h.append(self.h[-1]-self.vy[-1]*dt)
            self.vx_projektila.append(self.vx_projektila[-1]+self.a_x*dt)

        return self.x, self.h, self.t, self.vy

    def vrijemePadanja(self, dt=0.01):
        self.dropProjectile(dt)
        return self.t[-1]

    def gadjanjeMete(self, x_mete, sirina, v_vjetra = 0):
        self.x_projektila = [0]
        self.t_gibanja = [0]
        self.h_projektila = [self.h0]

        time = np.arange(0, 100, 0.1)

        for t in time:

            while self.t_gibanja[-1]<t:
                dt = 0.1
                self.x_projektila.append(self.x_projektila[-1]+self.v_x*dt)
                self.t_gibanja.append(self.t_gibanja[-1]+dt)
                self.h_projektila.append(self.h0)

            
            x_padanja, h, tt, vy = self.dropProjectile(vjetar = v_vjetra)
            xx = x_padanja[-1] + self.x_projektila[-1]

            if (xx >= x_mete-sirina and xx <= x_mete+sirina):
                trenutakIspustanja = t
                break


        for i in range (len(x_padanja)):
            x_padanja[i] = x_padanja[i]+self.x_projektila[-1]

        
        xxx = self.x_projektila + x_padanja
        yyy = self.h_projektila + h

        plt.plot(xxx, yyy)
        plt.title('Putanja projektila')
        plt.xlabel('x/m')
        plt.ylabel('y/m')
        plt.show()
        

        return trenutakIspustanja


