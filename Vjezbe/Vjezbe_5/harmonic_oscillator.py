# Napišite modul "harmonic_oscillator.py" koji će sadržavati klasu HarmonicOscillator s raznim metodama
# potrebnim za opis gibanja jednostavnog harmoničkog oscilatora u jednoj dimenziji.

import numpy as np

class HarmonicOscillator:

    def __init__(self, k=1, m=1):
        self.k = k
        self.m = m
        self.x=[]
        self.v=[]
        self.a=[]
        self.t=[]

    def set_initial_conditions(self, x0, v0):
        self.x=[x0]
        self.v=[v0]
        self.a=[-self.k/self.m*x0]
        self.t=[0]

    def reset(self):
        self.x = [self.x[0]]
        self.v = [self.v[0]]
        self.a = [self.a[0]]
        self.t = [self.t[0]]

    def __move(self, dt):
        self.v.append(self.v[-1]+self.a[-1]*dt)
        self.x.append(self.x[-1]+self.v[-1]*dt)
        self.a.append(-self.k/self.m*self.x[-1])
        self.t.append(self.t[-1]+dt)

    def gibanje(self, dt=1):
        if len(self.x)==0:
            print('Molimo da prvo postavite početne uvjete gibanja pomoću funkcije set_initial_conditions(x0, v0)')
        else:
            if len(self.x)>1:
                self.x = [self.x[0]]
                self.v = [self.v[0]]
                self.a = [-self.k/self.m*self.x[0]]
                self.t = [0]
            
            while max(self.t)<20:
                self.__move(dt)

    def analiticko_rjesenje(self):
        omega = np.sqrt(self.k/self.m)
        A = np.sqrt(self.x[0]**2+(self.v[0]/omega)**2)
        if self.x[0]==0:
            fi = np.pi/2
        else:
            fi = np.arctan(-self.v[0]/omega/self.x[0])
        
        x_analytical = []
        t = np.linspace(0, 20)
        for dt in t:
            x_analytical.append(-A*np.cos(omega*dt+fi))

        return t, x_analytical

    def period_titranja(self, dt):
        vremena_nultocki = []
        while len(vremena_nultocki)<3:

            while max(self.t)<30:
                self.__move(dt)
                if (self.x[-2]>0 and self.x[-1]<0) or (self.x[-2]<0 and self.x[-1]>0):
                    vremena_nultocki.append(self.t[-1])
                    break
                    
        period = vremena_nultocki[-1]-vremena_nultocki[0]
        return period