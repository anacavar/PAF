import numpy as np
import matplotlib.pyplot as plt
import math

class Particle():

    def __init__(self):
        #kreira prazne liste
        self.x=[]
        self.y=[]
        self.v_y=[]
        self.t=[]

    def set_initial_conditions(self, v_0, x_0, y_0, kut_0):
        # postavlja početne vrijednosti brzine, kuta otklona i koordinata početnog položaja
        #napuni liste
        self.v_0 = v_0
        self.x_0 = x_0
        self.y_0 = y_0
        self.kut_0 = kut_0
        self.v_x=np.cos(np.deg2rad(self.kut_0))*v_0
        self.x.append(x_0)
        self.y.append(y_0)
        self.t.append(0)
        self.v_y.append(np.sin(np.deg2rad(kut_0))*v_0)

    def reset(self):
        # briše sve informacije o čestici - resetira sve liste o putanji čestice
        self.x.clear()
        self.y.clear()
        self.v_y.clear()
        self.t.clear()

    def __move(self, dt=0.01):
        i = 0
        while self.y[i]>=0:
            g=9.81
            self.x.append(self.x[i]+self.v_x*dt)
            self.v_y.append(self.v_y[i]-g*dt)
            self.y.append(self.y[i]+self.v_y[i]*dt)
            self.t.append(self.t[i]+dt)
            i+=1

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

    #koja za zadani kut računa potrebnu početnu brzinu da se pogodi kuglica zadanog položaja i radijusa
    # def velocity_to_hit_target(self, kut0):
    #     v0 = 0
    #     return v0


