import matplotlib.pyplot as plt
import numpy as np

F=float(input("Unesi iznos sile u N: "))
m=float(input("Unesi masu čestice u kg: "))

a=F/m
t_max=10
dt=0.05

#x-t graf za 10 sekundi
t=np.arange(1,t_max,dt)
x=(1/2)*a*t**2
plt.figure(figsize=(8,4))
plt.subplot(1,3,1)
plt.title("x-t")
plt.grid()
plt.xlabel("t[s]")
plt.ylabel("x[m]")
plt.plot(t,x)


#v-t graf
v=a*t
plt.subplot(1,3,2)
plt.grid()
plt.title("v-t")
plt.xlabel("t[s]")
plt.ylabel("v[m/s]")
plt.plot(t,v)

#a-t graf
plt.subplot(1,3,3)
akc=v/t
plt.xlabel("t[s]")
plt.grid()
plt.title("a-t")
plt.ylabel("a[m/$s^2$]")
plt.plot(t,akc)
plt.tight_layout()


plt.show() 