from dis import dis
import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, m, a, tijelo = 'kugla'):
        self.tijelo = tijelo
        self.a = a
        self.A = []            
        if (tijelo!='kugla' and tijelo!='kocka'):
            print("Tijelo može biti samo kugla ili kocka")
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
        self.F = [0]

    def calculate_A(self, a, kut_brzine):
        A = a*a*np.cos(kut_brzine)+a*a*np.cos(np.pi/2-abs(kut_brzine))
        return A

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
        const = self.ro*self.C*self.A[-1]/2
        F = -const*v**2
        self.F.append(F)
        return F

    def __move_Euler(self):
        if (self.tijelo=='kocka'):
            self.A.append(self.calculate_A(self.a, self.kutbrzine[-1]))
        if (self.tijelo=='kugla'):
            self.A.append(self.a*self.a*np.pi)
        self.kutbrzine.append(np.arctan(self.vy[-1]/self.vx[-1]))
        F = self.__otporZraka()
        Fx = F*np.cos(self.kutbrzine[-1])
        Fy = F*np.sin(self.kutbrzine[-1])
        self.t.append(self.t[-1]+self.dt)
        self.ax.append(Fx/self.m)
        self.ay.append(self.g + Fy/self.m)
        self.vx.append(self.vx[-1]+self.ax[-1]*self.dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*self.dt)
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)

    def kosiHitac_Euler(self, h0, v0, kut0, dt, ro, C):
        self.set_initial_conditions(h0, v0, kut0, dt, ro, C)
        while self.y[-1]>=0:
            self.__move_Euler()

    def kosiHitac_RungeKutta(self, h0, v0, kut0, dt, ro, C):
        self.set_initial_conditions(h0, v0, kut0, dt, ro, C)
        while self.y[-1]>=0:
            self.__move_RungeKutta()

    def __ax(self, vx, vy):
        abs_v = np.sqrt(vx**2 + vy**2)
        cos = vx/abs_v
        const = self.ro*self.C*self.A[-1]/2
        F = -const*abs_v**2
        Fx = F*cos
        ax = Fx/self.m
        return ax

    def __ay(self, vx, vy):
        abs_v = np.sqrt(vx**2 + vy**2)
        sin = vy/abs_v
        const = self.ro*self.C*self.A[-1]/2
        F = -const*abs_v**2
        Fy = F*sin
        ay = self.g + Fy/self.m
        return ay

    def __move_RungeKutta(self):
        if (self.tijelo=='kocka'):
            self.A.append(self.calculate_A(self.a, self.kutbrzine[-1]))
        if (self.tijelo=='kugla'):
            self.A.append(self.a*self.a*np.pi)
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
        self.kutbrzine.append(np.arctan(self.vy[-1]/self.vx[-1]))

    def set_initial_conditions(self, h0, v0, kut0, dt, ro, C):
        if (self.tijelo=='kocka'):
            self.A.append(self.calculate_A(self.a, kut0))
        if (self.tijelo=='kugla'):
            self.A.append(self.a*self.a*np.pi)
        self.dt = dt
        self.ro = ro
        self.C = C
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

    def postavi_metu(self, x0, y0, r):
        self.x_mete = x0
        self.y_mete = y0
        self.r_mete = r

    def angle_to_hit_target(self, h0, v0, dt, ro, C):
        # za zadanu početnu brzinu računa kut otklona da se pogodi kuglica zadanog položaja i radijusa
        all_angles = np.arange(1, 91, 1)

        dictionary_angle_mind = {}
        dictionary_angle_coordinates = {}

        for kut0 in all_angles:
            self.set_initial_conditions(h0, v0, kut0, dt, ro, C)
            while self.y[-1]>=0:
                self.__move_Euler()
            distance = []
            dict_dist_koordinate = {}
            for i in range(len(self.x)):
                distance.append(np.sqrt((self.x[i]-self.x_mete)**2+(self.y[i]-self.y_mete)**2)) 
                dict_dist_koordinate[distance[-1]] = ((self.x[i], self.y[i]))
            min_d=min(distance)
            dictionary_angle_mind[kut0] = (min_d)
            dictionary_angle_coordinates[kut0] = (dict_dist_koordinate.get(min_d))

        dict_pogotci = {}
        for kut in all_angles:
            mind = dictionary_angle_mind[kut]
            if mind<=(self.r_mete+self.a):
                dict_pogotci[kut] = (mind)

        if (len(dict_pogotci)>0):
            najbolji_kut = min(dict_pogotci, key=dict_pogotci.get)
            najmanja_udaljenost = dict_pogotci.get(najbolji_kut)
            self.mind_koordinate = dictionary_angle_coordinates[najbolji_kut]
            print("Meta je pogođena!")
            print (najbolji_kut, najmanja_udaljenost)
            return najbolji_kut
        
        else:
            print('Meta nije pogođena!')
            najbolji_kut = min(dictionary_angle_mind, key=dictionary_angle_mind.get)
            najmanja_udaljenost = dictionary_angle_mind.get(najbolji_kut)
            self.mind_koordinate = dictionary_angle_coordinates[najbolji_kut]
            print(najbolji_kut, najmanja_udaljenost)
            return najbolji_kut



