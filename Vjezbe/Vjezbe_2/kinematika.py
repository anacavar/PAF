import matplotlib.pyplot as plt
import numpy as np

def jednolikoGibanje(F, m):

    a=F/m
    x=[0]
    t=[0]
    v=[0]
    a_list=[a]

    for i in range(100):
        dt = 0.1
        t.append(t[i]+dt)
        v.append(v[i]+a*dt)
        x.append(x[i]+v[i]*dt)
        a_list.append(a)
 
    fig, axs = plt.subplots(3)

    axs[0].plot(t, x)
    axs[0].title.set_text('Ovisnost položaja o vremenu')
    axs[0].set_xlabel('t [s]')
    axs[0].set_ylabel('x [m]')

    axs[1].plot(t, v)
    axs[1].title.set_text('Ovisnost brzine o vremenu')
    axs[1].set_xlabel('t [s]')
    axs[1].set_ylabel('v [m/s]')

    axs[2].plot(t, a_list)
    axs[2].title.set_text('Ovisnost akceleracije o vremenu')
    axs[2].set_xlabel('t [s]')
    axs[2].set_ylabel('a [m/s^2]')

    plt.tight_layout()
    plt.show()


def kosiHitac(v0, kut0):

    x=[]
    y=[]
    v_y=[]
    t=[]
    x.append(0)
    y.append(0)
    t.append(0)
    v_x=np.cos(np.deg2rad(kut0))*v0
    v_y.append(np.sin(np.deg2rad(kut0))*v0)
    dt=0.1

    for i in range (100):
        g=9.81
        x.append(x[i]+v_x*dt)
        v_y.append(v_y[i]-g*dt)
        y.append(y[i]+v_y[i]*dt)
        t.append(t[i]+dt)

    plt.subplot(2, 2, 1)
    plt.plot(x, y)
    plt.title('x - y graf')
    plt.xlabel('x [s]')
    plt.ylabel('y [m]')
    plt.subplot(2, 2, 2)
    plt.plot(t, x)
    plt.title('x - t graf')
    plt.xlabel('t [s]')
    plt.ylabel('x [m]')
    plt.subplot(2, 2, 3)
    plt.plot(t, y)
    plt.title('y - t graf')
    plt.xlabel('t [s]')
    plt.ylabel('y [m]')
    plt.tight_layout()  
    plt.show()

