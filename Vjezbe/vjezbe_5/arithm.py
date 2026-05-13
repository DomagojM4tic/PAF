import numpy as np


def aritmeticka_sredina(n):
        return sum(n)/len(n)

def standardna_devijacija(n):
        suma=0
        for i in n:
                suma=suma+(i-aritmeticka_sredina(n))**2

        return np.sqrt(suma/(len(n)-1))


tocke=[12,3,5,40,30,21,44,67,22,19]

print(aritmeticka_sredina(tocke))
print(standardna_devijacija(tocke))