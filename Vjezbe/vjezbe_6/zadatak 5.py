import numpy as np
import arithm as ar

# 5 mjerenja temperature vrenja vode [u stupnjevima Celzijusa ]
malo_n = [99.8 , 100.1 , 99.9 , 100.2 , 100.0]

# 10000 mjerenja istog eksperimenta ( simulacija )
np . random . seed (42)
veliko_n = np . random . normal ( loc =100.0 , scale =0.2 , size =10000) . tolist ()

def oblik_1(n):
    suma=0
    avg=ar.aritmeticka_sredina(n)
    for i in n:
            suma=suma+(i-avg)**2

    return np.sqrt(suma/(len(n)))


def oblik_2(n):
    suma=0
    avg=ar.aritmeticka_sredina(n)
    for i in n:
        suma=suma+(i-avg)**2

    return np.sqrt(suma/(len(n)-1))

def oblik_3(n):
    return oblik_2(n)/np.sqrt(len(n))

print(f"Sigma n: {oblik_1(malo_n)} ----- {oblik_1(veliko_n)}") 

print(f"S: {oblik_2(malo_n)} ----- {oblik_2(veliko_n)}")          

print(f"Sigma X: {oblik_3(malo_n)} ----- {oblik_3(veliko_n)}")          

#a) S se povećanjem mjerenja se za jako malu vrijednost poveca, dok Sigma x se znatno smanji


#b) relatvine razlike:
relativna_razlika_malo=(np.abs(oblik_2(malo_n)-oblik_1(malo_n))/oblik_1(malo_n))*100
relativna_razlika_veliko=np.abs(oblik_2(veliko_n)-oblik_1(veliko_n))/oblik_1(veliko_n)*100
print( f"Relativna razlika za malu listu:  {relativna_razlika_malo:.2f}%,\
      \nRelativna za veliku listu: {relativna_razlika_veliko:.4f}%")

#c)np.std() je ispravo koristit za racunanje devijacije skupa podataka u cjelosti umjeto uzorka iz tog skupa