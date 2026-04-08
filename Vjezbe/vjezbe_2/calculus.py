#%%
import numpy as np
import math as m
import matplotlib.pyplot as plt


def der_tocke(f,x,epsilon, metoda="3"):
    if metoda=="2":   
        derivacija=((f(x+epsilon)-f(x))/(epsilon))
    else:
        derivacija=((f(x+epsilon)-f(x-epsilon))/(2*epsilon))
    return derivacija


def derivacije(f,a,b,epsilon=1e-5, metoda="3"):
    tocke=np.linspace(a,b,20)
    derivacije=[]
    for x in tocke:
        derivacije.append(der_tocke(f,x,epsilon,metoda))
    return tocke, derivacije

def integral_pravokutnik(f,a,b,n):
    sirina=(b-a)/n
    gornja=0
    donja=0
    for i in range(n):
        lijeva=a+i*sirina
        desna=a+(i+1)*sirina
        gornja += max(f(lijeva),f(desna))
        donja += min(f(lijeva), f(desna))
    return gornja*sirina, donja*sirina


def integral_trapez(f,a,b,n):
    sirina = (b-a)/n
    zbroj = (f(a) + f(b))
    for i in range(1,n):
        x = a + i*sirina
        zbroj += 2*f(x)
    trapez=(sirina/2)*zbroj
    return trapez







# %%
