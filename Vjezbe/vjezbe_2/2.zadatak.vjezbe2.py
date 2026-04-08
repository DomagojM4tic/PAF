#%%
import particle as p
import matplotlib.pyplot as plt
import numpy as np
dt=np.linspace(0.0001, 0.1, 100)
rel_pogreska=[]

for t in dt:
    p1=p.Particle(10,60,0,0,dt=t)
    domet=p1.range()
    an=p1.an_rjesenje()
    r_pog=p1.rp()
    rel_pogreska.append(r_pog)

plt.plot(dt, rel_pogreska)
plt.ylabel("relativna pogreska [%]")
""" plt.xscale('log') """
plt.xlabel("dt[s]")
plt.grid()
plt.show()


# %%
