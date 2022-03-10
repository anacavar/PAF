def koordinate(x1,y1,x2,y2):
    a=(y2-y1)/(x2-x1)
    b=y1-a*x1
    if b>0:
        print("y=",a, "x+",b)
    else:
        print("y=",a, "x",b)

koordinate(1, 2, 3, 4)