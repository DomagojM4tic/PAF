#%%
import particle as p

print("hello")
p1=p.Particle(10,60,0,0)
domet=p1.range()
an=p1.an_rjesenje()

print(f"Domet cestice je: {domet:.2f} m")
print(f"Analiticki domet: {an:.2f} m")
print(f"Odstupanje: {domet-an:.2f} m")

p1.plot_trajectory()
p1.reset()

print("Podatci su resetirani!")

# %%
