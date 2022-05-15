import matplotlib.pyplot as plt

HOx_file = open("HO_x.txt", "r")
HOa_file = open("HO_a.txt", "r")
HOv_file = open("HO_v.txt", "r")
HOt_file = open("HO_t.txt", "r")

x_content = HOx_file.read()
a_content = HOa_file.read()
v_content = HOv_file.read()
t_content = HOt_file.read()

HOx_file.close()
HOa_file.close()
HOv_file.close()
HOt_file.close()

x = x_content.split()
a = a_content.split()
v = v_content.split()
t = t_content.split()

x = [float(i) for i in x]
a = [float(i) for i in a]
v = [float(i) for i in v]
t = [float(i) for i in t]

plt.subplot(2, 2, 1)
plt.plot(t, x)
plt.title('x - t graf')
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.subplot(2, 2, 2)
plt.plot(t, v)
plt.title('v - t graf')
plt.xlabel('t [s]')
plt.ylabel('v [m/s]')
plt.subplot(2, 2, 3)
plt.plot(t, a)
plt.title('a - t graf')
plt.xlabel('t [s]')
plt.ylabel('a [m/s2]')
plt.tight_layout()  
plt.show()