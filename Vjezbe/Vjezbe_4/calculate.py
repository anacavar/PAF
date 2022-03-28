from matplotlib import interactive
import numpy as np

def derivacija_u_tocki(f, x, dx=0.01):
    derivacija = (f(x+dx)-f(x))/dx
    return derivacija

def derivacija_u_intervalu(f, a, b, dx=0.01, threestepmethod=True):
    if threestepmethod==True:
        interval = np.arange(a, b, dx)
        derivacije = []
        for x in interval:
            derivacije.append((f(x+dx)-f(x-dx))/(2*dx))
        return interval, derivacije
    elif threestepmethod==False:
        interval=np.arange(a, b, dx)
        derivacije = []
        for x in interval:
            derivacije.append((f(x+dx)-f(x))/dx)
        return interval, derivacije

def integracija(f, a, b, N=1000):
    dx=abs((b-a)/N)
    gornja_medja = 0
    donja_medja = 0
    interval = np.arange(a, b, dx)
    for x in interval:
        # print(f(x))
        gornja_medja+=f(x)*dx
        donja_medja+=f(x+dx)*dx
    return gornja_medja, donja_medja

def trapezna_integracija(f, a, b, N=1000):
    dx=abs((b-a)/N)
    interval = np.arange(a, b, dx)
    integral = 0
    for x in interval:
        integral += (f(x)+(f(x+dx)-f(x))/2)*dx
    return integral

    
    
