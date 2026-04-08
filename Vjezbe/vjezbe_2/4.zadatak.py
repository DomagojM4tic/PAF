import calculus as calc
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**2

def anintf(x):
    return (1/3)*x**3


korak=np.arange(100,3000,10)
a=0
b=1

pravokutnik_gornja=[]
pravokutnik_donja=[]
trapez=[]
an=[]


for n in korak:
    gornja, donja = calc.integral_pravokutnik(f,a,b,n)
    pravokutnik_gornja.append(gornja)
    pravokutnik_donja.append(donja)
    trapez.append(calc.integral_trapez(f,a,b,n))
    an.append(anintf(b)-anintf(a))


print(anintf(b)-anintf(a))

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(korak,pravokutnik_gornja, color="blue", linestyle="--",label="Gornja i donja pravokutna aproksimacija")
plt.plot(korak,pravokutnik_donja, label="Analiticka",color="blue", linestyle="--")
plt.plot(korak,an, color="green")
plt.xlabel("n")
plt.ylabel("integral")
plt.legend()
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(korak,trapez,label="Trapezna aproksimacija",color="cyan", linestyle="--")
plt.plot(korak,an,label="Analiticka",color="green")
plt.legend()
plt.xlabel("n")
plt.ylabel("integral")
plt.grid(True)
plt.tight_layout()
plt.show()

print(calc.integral_trapez(f,0,1,600))




