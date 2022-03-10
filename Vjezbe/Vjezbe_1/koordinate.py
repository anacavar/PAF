try:
    koord1 = tuple(map(int, input("Unesite koordinate kao x,y: ").split(',')))
    koord2 = tuple(map(int, input("Unesite koordinate kao x,y: ").split(',')))
    x1=koord1[0]
    y1=koord1[1]
    x2=koord2[0]
    y2=koord2[1]
    a=(y2-y1)/(x2-x1)
    b=y1-a*x1
    if b>0:
        print("y=",a, "x+",b)
    else:
        print("y=",a, "x",b)
except:
    print("Molim unesite pravilne koordinate")