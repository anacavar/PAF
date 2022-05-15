import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, m):
        self.m = m
        self.g = -9.81
        self.t = []
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
        self.kutbrzine = []

    def __reset(self):
        self.t = []
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
        self.kutbrzine = []

    def __otporZraka(self):
        v = np.sqrt(self.vx[-1]**2+self.vy[-1]**2)
        const = self.ro*self.C*self.A/2
        F = -const*v**2
        return F

    def __move_Euler(self):
        self.kutbrzine.append(np.arctan(self.vy[-1]/self.vx[-1]))
        Fx = self.__otporZraka()*np.cos(self.kutbrzine[-1])
        Fy = self.__otporZraka()*np.sin(self.kutbrzine[-1])
        self.t.append(self.t[-1]+self.dt)
        self.ax.append(Fx/self.m)
        self.ay.append(self.g + Fy/self.m)
        self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*self.dt)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)

    def kosiHitac_Euler(self, h0, v0, kut0, dt, ro, C, A):
        self.dt = dt
        self.ro = ro
        self.C = C
        self.A = A
        self.h0 = h0
        self.v0 = v0
        self.kut0 = kut0/180*np.pi
        self.__reset()
        self.kutbrzine.append(self.kut0)
        self.t.append(0)
        self.x.append(0)
        self.y.append(self.h0)
        self.vx.append(self.v0*np.cos(self.kut0))
        self.vy.append(self.v0*np.sin(self.kut0))
        self.ax.append(0)
        self.ay.append(self.g)
        while self.y[-1]>=0:
            self.__move_Euler()

    def kosiHitac_RungeKutta(self, h0, v0, kut0, dt, ro, C, A):
        self.dt = dt
        self.ro = ro
        self.C = C
        self.A = A
        self.h0 = h0
        self.v0 = v0
        self.kut0 = kut0/180*np.pi
        self.__reset()
        self.kutbrzine.append(self.kut0)
        self.t.append(0)
        self.x.append(0)
        self.y.append(self.h0)
        self.vx.append(self.v0*np.cos(self.kut0))
        self.vy.append(self.v0*np.sin(self.kut0))
        self.ax.append(0)
        self.ay.append(self.g)
        while self.y[-1]>=0:
            self.__move_RungeKutta()


    def __ax(self, vx, vy):
        abs_v = np.sqrt(vx**2 + vy**2)
        cos = vx/abs_v
        const = self.ro*self.C*self.A/2
        F = -const*abs_v**2
        Fx = F*cos
        ax = Fx/self.m
        return ax

    def __ay(self, vx, vy):
        abs_v = np.sqrt(vx**2 + vy**2)
        sin = vy/abs_v
        const = self.ro*self.C*self.A/2
        F = -const*abs_v**2
        Fy = F*sin
        ay = self.g + Fy/self.m
        return ay

    def __v_squared (self, _vx, _vy):
        return ((_vx)**2 + (_vy)**2)

    def __move_RungeKutta(self):
        k1_vx = self.__ax(self.vx[-1], self.vy[-1])*self.dt
        k1_vy = self.__ay(self.vx[-1], self.vy[-1])*self.dt
        k1_x = self.vx[-1]*self.dt
        k1_y = self.vy[-1]*self.dt
        k2_vx = self.__ax(self.vx[-1]+(k1_vx/2), self.vy[-1]+(k1_vy/2))*self.dt
        k2_vy = self.__ay(self.vx[-1]+(k1_vx/2), self.vy[-1]+(k1_vy/2))*self.dt
        k2_x = (self.vx[-1] + (k1_vx/2))*self.dt
        k2_y = (self.vy[-1] + (k1_vy/2))*self.dt
        k3_vx = self.__ax(self.vx[-1]+(k2_vx/2), self.vy[-1]+(k2_vy/2))*self.dt
        k3_vy = self.__ay(self.vx[-1]+(k2_vx/2), self.vy[-1]+(k2_vy/2))*self.dt
        k3_x = (self.vx[-1] + (k2_vx/2))*self.dt
        k3_y = (self.vy[-1] + (k2_vy/2))*self.dt
        k4_vx = self.__ax(self.vx[-1]+k3_vx, self.vy[-1]+k3_vy)*self.dt
        k4_vy = self.__ay(self.vx[-1]+k3_vx, self.vy[-1]+k3_vy)*self.dt
        k4_x = (self.vx[-1] + k3_vx)*self.dt
        k4_y = (self.vy[-1] + k3_vy)*self.dt
        self.vx.append(self.vx[-1]+(k1_vx+2*k2_vx+2*k3_vx+k4_vx)/6)
        self.vy.append(self.vy[-1]+(k1_vy+2*k2_vy+2*k3_vy+k4_vy)/6)
        self.x.append(self.x[-1]+(k1_x+2*k2_x+2*k3_x+k4_x)/6)
        self.y.append(self.y[-1]+(k1_y+2*k2_y+2*k3_y+k4_y)/6)

