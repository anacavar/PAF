import matplotlib.pyplot as plt
import numpy as np

def koordinate(x1,y1,x2,y2, opcija='ekran'):
    a=(y2-y1)/(x2-x1)
    b=y1-a*x1
    x = np.arange(0.0, 4.0, 0.01)
    y = a*x + b
    plt.plot(x, y, linestyle='--')
    plt.scatter(x1, y1, color='red')
    plt.scatter(x2, y2, color='red')
    if opcija=='ekran':
        plt.show()
    if opcija=='pdf':
        plt.savefig('plooot.pdf')

#Opcija može biti 'ekran' ili 'pdf'
koordinate(1, 2, 3, 4, opcija='pdf')
