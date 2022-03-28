import calculate as cal
import funkcije as fun
import matplotlib.pyplot as plt
import numpy as np

print(cal.integracija(fun.sinus, 0, 3.14, 500))
print(cal.trapezna_integracija(fun.sinus, 0, 3.14, 500))

#integral funkcije sinus na intervalu od -pi/4 do 2*pi
a=-np.pi/4
b=2*np.pi
N=np.arange(40, 1000, 30)

donja_medja=[]
gornja_medja=[]
trapez=[]
analiticki_integral=[]

for n in N:
    analiticki_integral.append(-(np.cos(b)-np.cos(a)))
    gornja_medja.append(cal.integracija(fun.sinus, a, b, n)[0])
    donja_medja.append(cal.integracija(fun.sinus, a, b, n)[1])
    trapez.append(cal.trapezna_integracija(fun.sinus, a, b, n))

plt.plot(N, analiticki_integral)
plt.scatter(N, gornja_medja, s=10)
plt.scatter(N, donja_medja, s=10)
print(len(N), len(trapez))
plt.scatter(N, trapez, s=10)

plt.title('Numerička integracija')
plt.xlabel('N broj koraka')
plt.ylabel('Vrijednost integrala')
plt.show()