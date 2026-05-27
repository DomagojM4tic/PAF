import arithm as ar
import matplotlib.pyplot as plt
import numpy as np


M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]

alfa = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]

Mxalfa=[]
Xna2=[x**2 for x in alfa]

for i in range(0,len(M)):
    Mxalfa.append(alfa[i]*M[i])
print(Mxalfa)

xy=ar.aritmeticka_sredina(Mxalfa)
print(xy)
print(Xna2)

x2=ar.aritmeticka_sredina(Xna2)
print(x2)

a=xy/x2

print(a)
Yna2=[x**2 for x in M]
y2=ar.aritmeticka_sredina(Yna2)

y=[]
yplus=[]
yminus=[]
    
sigma=np.sqrt(1/len(M)*((y2/x2)-a**2))

for i in alfa:
    y.append(a*i)
    yplus.append((a+sigma)*i)
    yminus.append((a-sigma)*i)



plt.figure(figsize=(8, 6)) # Povećava graf da bude pregledniji

# Crtanje točaka i pravaca s bojama i oznakama
plt.scatter(alfa, M, color='blue', s=60, label='Izmjereni podaci', zorder=5)
plt.plot(alfa, y, 'r-', linewidth=2, label=f'Najbolji fit ($a = {a:.4f}$)')
plt.plot(alfa, yplus, 'g--', alpha=0.7, label=r'Gornja granica ($a + \sigma$)')
plt.plot(alfa, yminus, 'g--', alpha=0.7, label=r'Donja granica ($a - \sigma$)')

# Naslov i osi
plt.title('Određivanje modula torzije $D_t$ aluminijske šipke', fontsize=14, pad=15)
plt.xlabel('Kut zakretanja $\\phi$ [rad]', fontsize=12)
plt.ylabel('Moment torzije $M$ [Nm]', fontsize=12)

# Mreža (grid), granice i legenda
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=11)
plt.xlim(0, max(alfa)*1.1)
plt.ylim(0, max(M)*1.1)

# Uklanjanje desne i gornje crte okvira za uredniji izgled
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()