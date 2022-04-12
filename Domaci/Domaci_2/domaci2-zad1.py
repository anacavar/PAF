from modul import JednodimenzionalnoGibanje

def konstantnaSila(x, v, t):
    k=5
    sila_u_tocki = k
    return sila_u_tocki

def silaHarmonickogOscilatora(x, v, t):
    k = 1
    sila_u_tocki = -k*x
    return sila_u_tocki

JednolikoUbrzanoGibanje = JednodimenzionalnoGibanje(konstantnaSila)
HarmonickiOscilator = JednodimenzionalnoGibanje(silaHarmonickogOscilatora)

JednolikoUbrzanoGibanje.set_initial_conditions(0, 1)
JednolikoUbrzanoGibanje.gibanje()
JednolikoUbrzanoGibanje.plot()

HarmonickiOscilator.set_initial_conditions(0, 1)
HarmonickiOscilator.gibanje()
HarmonickiOscilator.plot()