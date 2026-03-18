
def jednoliko_gibanje(F,m,t_max,dt):
    import matplotlib.pyplot as plt
    import numpy as np

    a=F/m
    #x-t graf za 10 sekundi
    t=np.arange(0,t_max,dt)
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
    a=v/t
    plt.xlabel("t[s]")
    plt.grid()
    plt.title("a-t")
    plt.ylabel("a[m/$s^2$]")
    plt.plot(t,a)
    plt.tight_layout()

    return plt.show() 

F=float(input("Unesi iznos sile u N: "))
m=float(input("Unesi masu čestice u kg: "))

t_max=10
dt=0.05

jednoliko_gibanje(F,m,t_max,dt)