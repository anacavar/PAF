import numpy as np
import matplotlib.pyplot as plt
import math
# from Vjezbe.Vjezbe_2.kosihitac import kosi_hitac
class Particle():

    def __init__(self):
        #kreira prazne liste
        self.x=[]
        self.y=[]
        self.v_y=[]
        self.t=[]

    def set_initial_conditions(self, v_0, x_0, y_0, kut_0):
        # postavlja početne vrijednosti brzine, kuta otklona i koordinata početnog položaja
        # napuni liste
        self.v_0 = v_0
        self.x_0 = x_0
        self.y_0 = y_0
        self.kut_0 = kut_0
        self.v_x=np.cos(np.deg2rad(self.kut_0))*v_0
        self.x.clear()
        self.y.clear()
        self.t.clear()
        self.v_y.clear()
        self.x.append(x_0)
        self.y.append(y_0)
        self.t.append(0)
        self.v_y.append(np.sin(np.deg2rad(kut_0))*v_0)

    def reset(self):
        # briše sve informacije o čestici - resetira sve liste o putanji čestice
        x0=self.x[0]
        y0=self.y[0]
        vy0=self.v_y[0]
        t0=self.t[0]
        self.x.clear()
        self.y.clear()
        self.v_y.clear()
        self.t.clear()
        self.x.append(x0)
        self.y.append(y0)
        self.t.append(t0)
        self.v_y.append(vy0)

    def __move(self, dt=0.01):
        self.reset()
        i = 0
        while self.y[i]>=0:
            g=9.81
            self.x.append(self.x[i]+self.v_x*dt)
            self.v_y.append(self.v_y[i]-g*dt)
            self.y.append(self.y[i]+self.v_y[i]*dt)
            self.t.append(self.t[i]+dt)
            i+=1
        return self.x, self.y

    def range(self, dt=0.01):
        # numerički računa domet projektila
        self.__move(dt)
        max_x=max(self.x, key=abs)
        return max_x

    def plot_trajectory(self):
        self.__move()
        plt.plot(self.x, self.y)
        plt.title('x - y graf')
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.show()

    def analiticki_domet(self):
        domet=self.v_0**2*math.sin(2*math.radians(self.kut_0))/9.81
        return domet

    def total_time(self):
        t_ukupno = max(self.t)
        return t_ukupno

    def max_speed(self):
        max_vy = max(self.v_y, key=abs)
        max_v = np.sqrt(max_vy**2+self.v_x**2)
        return max_v

    def velocity_to_hit_target(self, kut0, x0, y0, r):
        all_velocities = np.arange(1, 10, 1)
        min_distances=[]
        hit_velocities=[]
        for v in all_velocities:
            self.set_initial_conditions(v, 0, 0, kut0)
            x, y = self.__move()
            n = len(x)
            distance = []
            for i in range (n):
                distance.append(np.sqrt((x[i]-x0)**2+(y[i]-y0)**2))
                
            min_d=min(distance)
            min_distances.append(min_d)

            if min_d<=r:
                hit_velocities.append(v)
        
            if len([*filter(lambda x: x<min_d, min_distances)]) == 0:
                v_min_d = v

        if len(hit_velocities)>0:
            print('Brzine za koje će projektil pogoditi metu su:', hit_velocities, 'm/s')
            print('Brzina koja najpreciznije gađa metu je', v_min_d, 'm/s, s udaljenošću od centra mete', round(min(min_distances), 2), 'm')
            return hit_velocities
        else:
            print('Meta neće biti pogođena ali minimalna udaljenost od', round(min_d, 2), 'm dosegnuta je pri brzini', v_min_d, 'm/s')
            return min_d
    

    def angle_to_hit_target(self, v, x0, y0, r):
        # za zadanu početnu brzinu računa kut otklona da se pogodi kuglica zadanog položaja i radijusa
        all_angles = np.arange(1, 91, 1)
        min_distances=[]
        hit_angles=[]
        for kut0 in all_angles:
            self.set_initial_conditions(v, 0, 0, kut0)
            x, y = self.__move()
            n = len(x)
            distance = []
            for i in range (n):
                distance.append(np.sqrt((x[i]-x0)**2+(y[i]-y0)**2))
                
            min_d=min(distance)
            min_distances.append(min_d)

            if min_d<=r:
                hit_angles.append(kut0)
        
            if len([*filter(lambda x: x<min_d, min_distances)]) == 0:
                kut0_min_d = kut0

        if len(hit_angles)>0:
            print('Kutovi za koje će projektil pogoditi metu su:', hit_angles, 'stupnjeva')
            print('Kut koji najpreciznije gađa metu je', kut0_min_d, 'stupnjeva, s udaljenošću od centra mete', round(min(min_distances), 2), 'm')
            return hit_angles
        else:
            print('Meta neće biti pogođena ali minimalna udaljenost od', round(min_d, 2), 'm dosegnuta je pri kutu od', kut0_min_d, 'stupnjeva')
            return min_d


        

