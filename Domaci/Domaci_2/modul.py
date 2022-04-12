# Razvijte vlastiti modul koji će korisniku omogućiti numeričko računanje položaja, brzine i akceleracije za
# jednodimenzionalno gibanje. Neka modul radi za bilo koju silu koju korisnik može definirati kao proizvoljnu
# funkciju brzine, položaja i vremena (F = f(v, x, t)). Testirajte modul u slučajevima konstante sile (F =
# const) i harmoničkog oscilatora (F = −kx).

import matplotlib.pyplot as plt

class JednodimenzionalnoGibanje():
    def __init__(self, f, m=1):
        self.f = f #funkcija sile
        self.m = m
        self.x=[]
        self.v=[]
        self.a=[]
        self.t=[]

    def set_initial_conditions(self, x0, v0):
        self.x=[x0]
        self.v=[v0]
        self.t=[0]
        self.a=[self.f(self.x[0], self.v[0], self.t[0])/self.m]

    def __move(self, dt):
        self.v.append(self.v[-1]+self.a[-1]*dt) 
        self.x.append(self.x[-1]+self.v[-1]*dt)
        self.a.append(self.f(self.x[-1], self.v[-1], self.t[-1]))
        self.t.append(self.t[-1]+dt)

    def gibanje(self, dt=1):
        dt=0.1
        if len(self.x)==0:
            print('Molimo da prvo postavite početne uvjete gibanja pomoću funkcije set_initial_conditions()')
        else:
            if len(self.x)>1:
                self.x = [self.x[0]]
                self.v = [self.v[0]]
                self.t = [0]
                self.a = [self.f(self.x[0], self.v[0], self.t[0])/self.m]
            while max(self.t)<20:
                self.__move(dt)

    def plot(self):
        plt.plot(self.t, self.x)
        plt.title('x - t graf')
        plt.xlabel('t/s')
        plt.ylabel('x/m')
        plt.show()
