import kinematika as kinematika
import matplotlib.pyplot as plt
import numpy as np

F=float(input("Unesi iznos sile u N: "))
m=float(input("Unesi masu čestice u kg: "))
t_max=10
dt=0.05

kinematika.jednoliko_gibanje(F,m,t_max,dt)