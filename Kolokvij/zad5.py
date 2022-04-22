from modul import ProjectileDrop
import matplotlib.pyplot as plt 

objekt = ProjectileDrop(100, 10)

# bez vjetra
print(objekt.gadjanjeMete(150, 5))

#sa vjetrom
print(objekt.gadjanjeMete(150, 5, 5))