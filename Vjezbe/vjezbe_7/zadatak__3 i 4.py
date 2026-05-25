import numpy as np
import matplotlib.pyplot as plt

def median(podaci):
    n=len(podaci)
    podaci_s=sorted(podaci)
    if n%2==1:
        return(podaci_s[(n)//2])
    else:
        return (podaci_s[(n//2)-1]+podaci_s[n//2])/2
        

a = [3 , 1 , 4 , 1 , 5 , 9 , 2 , 6 ] # paran n
b = [3 , 1 , 4 , 1 , 5 , 9 , 2 , 6 , 5] #neparan n

print(median(a))
print(np.median(a))
print(median(b))
print(np.median(b))

np . random . seed (42)
mase_ciste = np . random . normal ( loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] # pogreske pri redukciji podataka
print("medijani masa:")
print(median(mase))
print(np.median(mase))


print("-----------------------")
print("Razlika koristeci mase s pogreskama:")
avg_mase=np.mean(mase)
print(avg_mase,"avg s pogreskama - ")
medijan1=np.median(mase)
print(medijan1,"medijan s pogreskama")
razlika1=np.abs(avg_mase-medijan1)
print("Promjena medijana")

print(razlika1)
print("-----------------------")
print("razlika koristeci mase bez pogresak:")
avg_mase_ciste=np.mean(mase_ciste)
print(avg_mase_ciste,"avg bez pogresaka -")
medijan2=np.median(mase_ciste)
print(medijan2, "medijan bez pogresaka")
razlika2=np.abs(avg_mase_ciste-medijan2)
print(razlika2)
print("-----------------------")

print(f"Aritmeticka sredina se promjenila za {np.abs(avg_mase-avg_mase_ciste)}")
print(f"medijan se promjenio za {np.abs(medijan1-medijan2)}")



plt.figure()
plt.hist(mase_ciste)

plt.axvline(medijan1, color='red', linestyle='--', linewidth=2, 
            label=f'Aritmetička sredina: {medijan1:.4f}')

plt.axvline(avg_mase, color='purple', linestyle=':', linewidth=2.5, 
            label=f'Medijan: {avg_mase:.4f}')

plt.axvline(medijan2, color='orange', linestyle='-.', linewidth=2, 
            label=f'Aritmetička sredina bez pogresaka: {medijan2:.4f}')

plt.axvline(avg_mase_ciste, color='yellow', linestyle='solid', linewidth=2.5, 
            label=f'Medijan bez pogresaka: {avg_mase_ciste:.4f}')

plt.legend(loc='upper right')
plt.show()





