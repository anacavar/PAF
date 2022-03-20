import numpy as np
import matplotlib.pyplot as plt

# vraća liste vrijednosti položaja x i y, brzine u y smjeru i vremena
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
    dt=0.01
    g=9.81

    for i in range (200):
        if y[i]>=0:
            x.append(x[i]+v_x*dt)
            v_y.append(v_y[i]-g*dt)
            y.append(y[i]+v_y[i]*dt)
            t.append(t[i]+dt)
        else:
            break

    return x, y, t, v_x, v_y

def kosi_hitac_graf(v0, kut0):
    x, y, t, v_x, v_y = kosi_hitac(v0, kut0)
    plt.plot(x, y)
    plt.title('x - y graf')
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.show()

def kosi_hitac_max_y(v0, kut0):
    x, y, t, v_x, v_y= kosi_hitac(v0, kut0)
    max_y=max(y)
    print("Maksimalna visina koju čestica dosegne je", max_y)

def kosi_hitac_max_x(v0, kut0):
    x, y, t, v_x, v_y= kosi_hitac(v0, kut0)
    max_x=max(x)
    print("Domet čestice je", max_x)

def kosi_hitac_max_v(v0, kut0):
    x, y, t, v_x, v_y= kosi_hitac(v0, kut0)
    maxv_y=max(v_y, key=abs)
    maxv=np.sqrt(v_x**2+maxv_y**2)
    print("Maksimalna brzina čestice tijekom kosog hitca je", maxv)

def gadjanje_mete(x0, y0, r, v0, kut0):

    x, y, t, v_x, v_y= kosi_hitac(v0, kut0)
    circle = plt.Circle((x0, y0), radius = r, fill=False)

    n = len(x)
    d = []

    for i in range (n):
        d.append(np.sqrt((x[i]-x0)**2+(y[i]-y0)**2))

    mind = min(d)

    if mind <= r:
        print('Meta je pogođena')
    else:
        print('Meta je promašena za udaljenost', mind-r)

    plt.gca().add_patch(circle)
    plt.plot(x, y)
    plt.title('Gađanje mete')
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

    
