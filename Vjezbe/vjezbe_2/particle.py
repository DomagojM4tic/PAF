import math as m
import matplotlib.pyplot as plt
import numpy as np

class Particle:
    def __init__(self, pocetna_brzina, kut, x0,y0, a=9.81, dt=0.01):
        self.v0 = pocetna_brzina
        self.theta=kut
        self.a=a
        self.dt=dt
        self.x0=x0
        self.y0=y0
        self.reset()
       
    def reset(self):
        self.x=[float(self.x0)]
        self.y=[float(self.y0)]
        self.vx=[self.v0*m.cos(m.radians(self.theta))]
        self.vy=[self.v0*m.sin(m.radians(self.theta))]
        
    def __move(self):
        self.x.append(self.x[-1]+self.vx[-1]*self.dt)
        self.vx.append(self.vx[-1])
        self.y.append(self.y[-1]+self.vy[-1]*self.dt)
        self.vy.append(self.vy[-1]-self.a*self.dt)

    def range(self):#numercik domet
        while self.y[-1]>=0:
            self.__move()

        return self.x[-1]
    
    def an_rjesenje(self):#analiticko rjesenje dometa
        self.D=((self.v0**2)*m.sin(m.radians(2*self.theta)))/self.a
        return self.D

    def rp(self):#ovo mi je funkcija relatvine pogreske
        pogreska=np.abs(self.D-self.x[-1])/np.abs(self.D) 
        return pogreska*100

    def plot_trajectory(self):
        plt.figure()
        plt.plot(self.x, self.y)
        plt.xlabel("Domet")
        plt.ylabel("Visina")
        """ plt.xticks()
        plt.xlim(0,300)
        plt.ylim(0,100) """
        plt.show()


