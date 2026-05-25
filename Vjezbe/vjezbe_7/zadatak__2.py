import matplotlib.pyplot as plt
import numpy as np
import zadatak__1 as histogram


np . random . seed (42)
mase_ciste = np . random . normal ( loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] # pogreske pri redukciji podataka

k=14
rubovi, frekvencija, h = histogram.histogram(mase_ciste, k)

medijan=np.median(mase_ciste)
avg=np.mean(mase_ciste)
sredina=[rubovi[i]+h/2 for i in range(k)]


#plotannje
plt.figure(figsize=(9,6))   
plt.bar(sredina, frekvencija, width=h,edgecolor='black', color='skyblue', alpha=0.8)

plt.axvline(avg, color='red', linestyle='--', linewidth=2, 
            label=f'Aritmetička sredina: {avg:.4f}')

plt.axvline(medijan, color='purple', linestyle=':', linewidth=2.5, 
            label=f'Medijan: {medijan:.4f}')

plt.xlabel('Masa', fontsize=11)
plt.ylabel('Frekvencija (broj mjerenja)', fontsize=11)
plt.title('2.Histogram cistih mjerenja mase zvijezde Sirius A', fontsize=12, fontweight='bold')

plt.xticks(rubovi, rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()      

