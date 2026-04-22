import numpy as np
import matplotlib.pyplot as plt

class Projectile():
    def __init__(self, v0, masa, kut, povrsina_presjeka, Cd=0.47, g=9.81, rho=1.225):
        self.m=masa
        self.theta=kut
        self.v0=v0
        self.Rho=rho
        self.A=povrsina_presjeka
        self.Cd=Cd
        self.g=g
        self.vx=self.v0*np.cos(np.radians(self.theta))
        self.vy=self.v0*np.sin(np.radians(self.theta))
        self.reset()
        


    def ax(self,vx):
        k=(1/2)*self.Cd*self.Rho 
        return -k*vx/self.m
    
    def ay(self,vy):
        k=(1/2)*self.Cd*self.Rho*self.A
        return -self.g-k*vy/self.m

    def reset(self):
        self.vx=self.v0*np.cos(np.radians(self.theta))
        self.vy=self.v0*np.sin(np.radians(self.theta))

    def RungeKuttara(self, dt=0.01):
        self.reset()
        x=[0]
        y=[0]
        
        while y[-1]>=0:
        
            k1x=self.ax(self.vx)
            k2x=self.ax(self.vx+k1x*dt/2)
            k3x=self.ax(self.vx+k2x*dt/2)
            k4x=self.ax(self.vx+k3x*dt)

            dx=1/6*dt*(6*self.vx+dt*(k1x+k2x+k3x))
            self.vx=self.vx+1/6*dt*(k1x+2*k2x+2*k3x+k4x)
            
            k1y=self.ay(self.vy)
            k2y=self.ay(self.vy+k1y*dt/2)
            k3y=self.ay(self.vy+k2y*dt/2)
            k4y=self.ay(self.vy+k3y*dt)

            dy=1/6*dt*(6*self.vy+dt*(k1y+k2y+k3y))
            self.vy=self.vy+1/6*dt*(k1y+2*k2y+2*k3y+k4y)

            x.append(x[-1]+dx)
            y.append(y[-1]+dy)
            
        return x, y


    def kosi_hitac(self, dt=0.01):
        x=[0]
        y=[0]
                
        while y[-1]>=0:
            v=np.sqrt(self.vx**2 + self.vy**2)

            #F_ot=(1/2)*self.Cd*self.Rho*v**2
            #F_uk=self.m*self.g+F_ot
            k=(1/2)*self.Cd*self.Rho*self.A   
            

            ax=-k*self.vx/self.m
            ay=-self.g-k*self.vy/self.m
            
            
            self.vx=self.vx + ax*dt
            self.vy=self.vy + ay*dt

            if y[-1]>=0:
                x.append(x[-1]+self.vx*dt)
                y.append(y[-1]+self.vy*dt)

        return x, y

    

p=Projectile(20,2,60,0.10)
x, y = p.kosi_hitac()
X, Y = p.RungeKuttara()
plt.plot(x,y, label="Euler")
plt.plot(X,Y, label="Runge-Kutta - dt=0.01")
plt.grid(True)
plt.legend()
plt.xlabel("Domet[m]")
plt.ylabel("Visina[m]")
plt.show()