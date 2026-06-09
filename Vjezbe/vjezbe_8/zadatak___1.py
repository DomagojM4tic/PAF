import numpy as np
import matplotlib.pyplot as plt


h0 = 0.54 # m
m = 0.5257 # kg
r = 4.025e-3 # m

h = [0.14 , 0.17 , 0.19 , 0.22 , 0.25 , 0.28 , 0.31 , 0.34 , 0.37 , 0.40] # m
t_mean = [1.740 , 1.793 , 2.043 , 2.190 , 2.280 , 2.417 , 2.540 , 2.640 , 2.670 , 2.813] # s

n=len(h)

y=[np.log(x) for x in h]
x=[np.log(x) for x in t_mean]

X_x_Y=[]
for i in range(0,n):
    X_x_Y.append(y[i]*x[i])

x2=[x**2 for x in x]

a=(n*sum(X_x_Y) - (sum(x)*sum(y)))/(n*sum(x2)-(sum(x))**2)
print("a: ", a)
b=(sum(y) - a*sum(x))/n
print("b: ", b)

y_fit=[a*x+b for x in x]


t2=[i**2 for i in t_mean]
s_x_t2=[]
t2na2=[i**2 for i in t2]

for i in range(0,n):
    s_x_t2.append(h[i]*t2[i])

k=sum(s_x_t2)/sum(t2na2)
print("a: ",k)
print("b: 0")

y_fit2=[k*i for i in t2]


Iz=m*r**2*(9.81/(2*k)-1)

print(f"Moment inercije iznosi: {Iz:e}")


residue = [(y[i] - y_fit[i])**2 for i in range(n)]

s = np.sqrt(sum(residue) / (n - 2))

# Suma kvadrata odstupanja nakon raspisivanja
SS_xx = sum(x2) - (sum(x)**2) / n

sigma_a = s / np.sqrt(SS_xx)
sigma_b = s * np.sqrt(sum(x2) / (n * SS_xx))

print(f"Pogreška koeficijenta a (sigma_a): {sigma_a}")
print(f"Pogreška koeficijenta b (sigma_b): {sigma_b}")

#drugi pravac pogreska
residue2 = [(h[i] - y_fit2[i])**2 for i in range(n)]
s2 = np.sqrt(sum(residue2) / (n - 1))
sigma_k = s2 / np.sqrt(sum(t2na2))
print(f"Pogreška koeficijenta k (sigma_k): {sigma_k}")

g = 9.81
sigma_Iz = m * (r**2) * (g / (2 * (k**2))) * sigma_k
print(f"Pogreška momenta inercije (sigma_Iz): {sigma_Iz:e}")

plt.figure(figsize=(10,6))
# Prvi graf
plt.subplot(1,2,1)
plt.scatter(x,y, label='Mjerenja')
plt.plot(x,y_fit, color='orange', label='Pravac')
plt.title('a) log(s) - log(t)')
plt.xlabel('log(t)')
plt.ylabel('log(s)')
plt.legend()

# Drugi graf
plt.subplot(1,2,2)
plt.scatter(t2,h, label='Mjerenja')
plt.plot(t2, y_fit2, color='red', label='Pravac')
plt.title('b) s - t^2')
plt.xlabel('t^2')
plt.ylabel('s')
plt.legend()

plt.tight_layout()
plt.show()
