import numpy as np

class BungeeJump:

    def __init__(self, height, mass, k, l0, C):
        self.h = height
        self.m = mass
        self.k = k
        self.l0 = l0
        self.C = C
        self.g = -9.81
        self.y = [self.h]
        self.vy = [0]
        self.ay = [self.g]
        self.t = [0]
        self.E_gpot = [self.m*abs(self.g)*self.h]
        self.E_kin = [0]
        self.E_pot = [0]
        self.E_ukupna = [self.E_gpot[-1]+self.E_kin[-1]+self.E_pot[-1]]

    def sila(self):
        if self.y[-1]>(self.h-self.l0):
            F = - self.C*self.vy[-1]**2*np.sign(self.vy[-1])
            F = 0
        else:
            F = self.k*abs((self.h-self.y[-1])-self.l0) - self.C*np.sign(self.vy[-1])*self.vy[-1]**2
        return F

    def __move(self, dt = 0.01):
        self.ay.append(self.g + self.sila()/self.m)
        self.vy.append(self.vy[-1]+self.ay[-1]*dt)
        self.y.append(self.y[-1]+self.vy[-1]*dt)
        self.t.append(self.t[-1]+dt)
        self.E_gpot.append(self.m*abs(self.g)*self.y[-1])
        self.E_kin.append((self.m*self.vy[-1]**2)/2)
        if self.y[-1]>=(self.h-self.l0):
            self.E_pot.append(0)
        else:
            self.E_pot.append((self.k*(self.h-self.y[-1]-self.l0)**2)/2)
        self.E_ukupna.append(self.E_gpot[-1]+self.E_kin[-1]+self.E_pot[-1])

    def jump(self, t = 100):
        while self.t[-1]<t:
            self.__move()
    



