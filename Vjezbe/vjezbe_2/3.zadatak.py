#%%
import calculus as cal
import matplotlib.pyplot as plt
import numpy as np

def an_der_kub(x):
    return 3*(x**2)
def an_der_trig(x):
    return np.cos(x)
def kubnaf(x):
    return x**3
def trigf(x):
    return np.sin(x)

epsiloni=[0.5, 0.00001]

plt.figure(figsize=(14, 6))
plt.subplot(1,2,1)
x=np.linspace(-3,3,100)
plt.plot(x, an_der_kub(x), color="red", linestyle=":", label="Analiticko rješenje",linewidth="4")

for E in epsiloni:
    #3step graf
    tocke3,deriv3=cal.derivacije(kubnaf,-3,3,epsilon=E)
    plt.plot(tocke3,deriv3, color="blue", linestyle="-", label=f"3-step (ε={E})")
    tocke2,deriv2=cal.derivacije(kubnaf,-3,3,epsilon=E,metoda="2")#2step graf
    plt.plot(tocke2,deriv2, color="orange", linestyle="--", label=f"2-step (ε={E})")

plt.title("Derivacija kubne funkcije: f(x) = x^3")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.grid(True)

plt.subplot(1,2,2)
x=np.linspace(0,2*np.pi,1000)
plt.plot(x, an_der_trig(x), color="red", linestyle=":",label="Analiticko rješenje", linewidth="4")

for E in epsiloni:
    #three step graf
    tocke3,deriv3=cal.derivacije(trigf,0,2*np.pi,epsilon=E)
    plt.plot(tocke3,deriv3, color="blue", linestyle="-", label=f"3-step (ε={E})")
    tocke2,deriv2=cal.derivacije(trigf,0,2*np.pi,epsilon=E,metoda="2") #2step graf
    plt.plot(tocke2,deriv2, color="orange", linestyle="--", label=f"2-step (ε={E})")

plt.title("Derivacija trig. funkcije: f(x)=sin(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
# %%
