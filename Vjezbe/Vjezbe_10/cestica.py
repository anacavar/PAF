import numpy as np

class Cestica:

    def __init__(self, Ex, Ey, Ez, Bx, By, Bz, q, m):
        self.q = q
        self.m = m 
        self.E = np.array((Ex, Ey, Ez))
        self.B = np.array((Bx, By, Bz))

    def __move_Euler(self, dt):
        F = self.q*self.E + self.q*np.cross(self.v[-1], self.B)
        a = F/self.m
        self.a.append(a)
        self.v.append(self.v[-1]+self.a[-1]*dt)
        self.r.append(self.r[-1]+self.v[-1]*dt)
        self.t.append(self.t[-1]+dt)

    def gibanje(self, x0, y0, z0, vx0, vy0, vz0, t=10, dt=0.0001):
        r0 = np.array((x0, y0, z0))
        v0 = np.array((vx0, vy0, vz0))
        a0 = self.q*np.cross(v0, self.B)/self.m
        self.r = [r0]
        self.v = [v0]
        self.a = [a0]
        self.t = [0]
        while self.t[-1]<t:
            self.__move_Euler(dt)

    def getCoordinates(self):
        x = []
        y = []
        z = []
        for r in self.r:
            x.append(r[0])
            y.append(r[1])
            z.append(r[2])
        return x, y, z

    def __move_RungeKutta(self, dt):
        k1_v = self.__a(self.v[-1])*dt
        k1_r = self.v[-1]*dt
        k2_v = self.__a(self.v[-1]+k1_v/2)*dt
        k2_r = (self.v[-1]+k1_v/2)*dt
        k3_v = self.__a(self.v[-1]*k2_v/2)*dt
        k3_r = (self.v[-1]+k2_v/2)*dt
        k4_v = self.__a(self.v[-1]+k3_v)*dt
        k4_r = (self.v[-1]+k3_v)*dt
        self.t.append(self.t[-1]+dt)
        self.v.append(self.v[-1]+(k1_v+2*k2_v+2*k3_v+k4_v)/6)
        self.r.append(self.r[-1]+(k1_r+2*k2_r+2*k3_r+k4_r)/6)

    def __a(self, v):
        F = self.q*self.E + self.q*np.cross(v, self.B)
        a = F/self.m
        return a

    def gibanje_RungeKutta(self, x0, y0, z0, vx0, vy0, vz0, t=10, dt=0.0001):
        r0 = np.array((x0, y0, z0))
        v0 = np.array((vx0, vy0, vz0))
        a0 = self.q*np.cross(v0, self.B)/self.m
        self.r = [r0]
        self.v = [v0]
        self.a = [a0]
        self.t = [0]
        while self.t[-1]<t:
            self.__move_RungeKutta(dt)
