import matplotlib.pyplot as plt
import numpy as np

np . random . seed (42)
mase_ciste = np . random . normal ( loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] # pogreske pri redukciji podataka

def histogram(podaci, k):
    x_max=max(podaci)
    x_min=min(podaci)
    h=(x_max-x_min)/k
    rubovi=[x_min+i*h for i in range(k+1)]
    
    podaci_po_k=np.zeros(k)

    for x in podaci:
        for i in range(k):
            if i==k-1:
                if rubovi[i]<= x <=rubovi[i+1]:
                    podaci_po_k[i]+=1
                    break
            else:
                if rubovi[i]<= x <rubovi[i+1]:
                    podaci_po_k[i]+=1
                    break
    
    for i in range(k):
        zagrada="]" if i==k-1 else ")"
        print(f"[{rubovi[i]:.2f}, {rubovi[i+1]:.2f}{zagrada} : {podaci_po_k[i]} --------")
    print("....................")
    
    return rubovi, podaci_po_k, h

k_razreda=10
rubovi, frekvencija, h = histogram(mase_ciste, k_razreda)
sredina=[rubovi[i]+h/2 for i in range(k_razreda)]

plt.figure(figsize=(9,6))
plt.bar(sredina, frekvencija, width=h,edgecolor='black', color='skyblue', alpha=0.8)

plt.xlabel('Masa', fontsize=11)
plt.ylabel('Frekvencija (broj mjerenja)', fontsize=11)
plt.title('Histogram cistih mjerenja mase zvijezde Sirius A', fontsize=12, fontweight='bold')


plt.xticks(rubovi, rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.tight_layout()
plt.show()      
