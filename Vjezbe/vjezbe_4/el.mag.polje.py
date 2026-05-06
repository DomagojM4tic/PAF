import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


class Cestica():
    def __init__(self, masa, naboj, B, E, v):
        self.m=masa
        self.q=naboj
        self.B=B
        self.v=v
        self.E=E
    
        #F=m dv/dt = q(v x B)


    def ax(self, v):
        return (self.q*(self.B[1]*self.v[2] - self.B[2]*self.v[1]) + self.q*self.E[0])/self.m
    def ay(self, v):
        return -((self.q*(self.B[0]*self.v[2] - self.B[2]*self.v[0]) + self.q*self.E[1]))/self.m
    def az(self, v):
        return (self.q*(self.B[0]*self.v[1] - self.B[1]*self.v[0]) + self.q*self.E[2])/self.m

    def RungeKuttara(self, n=3, tocke=1000):
     
        x=[0]
        y=[0]
        z=[0]
        Buk=np.sqrt(self.B[0]**2+self.B[1]**2+self.B[2]**2)
    
       

        T=2*np.pi*self.m/(abs(self.q)*Buk)
        dt=T/tocke

        t=0

        while t<n*T:
        
            k1x=self.ax(self.v[0])
            k2x=self.ax(self.v[0]+k1x*dt/2)
            k3x=self.ax(self.v[0]+k2x*dt/2)
            k4x=self.ax(self.v[0]+k3x*dt)

            dx=1/6*dt*(6*self.v[0]+dt*(k1x+k2x+k3x))
            self.v[0]=self.v[0]+1/6*dt*(k1x+2*k2x+2*k3x+k4x)
            
            k1y=self.ay(self.v[1])
            k2y=self.ay(self.v[1]+k1y*dt/2)
            k3y=self.ay(self.v[1]+k2y*dt/2)
            k4y=self.ay(self.v[1]+k3y*dt)

            dy=1/6*dt*(6*self.v[1]+dt*(k1y+k2y+k3y))
            self.v[1]=self.v[1]+1/6*dt*(k1y+2*k2y+2*k3y+k4y)
            
            k1z=self.az(self.v[2])
            k2z=self.az(self.v[2]+k1z*dt/2)
            k3z=self.az(self.v[2]+k2z*dt/2)
            k4z=self.az(self.v[2]+k3z*dt)

            dz=1/6*dt*(6*self.v[2]+dt*(k1z+k2z+k3z))
            self.v[2]=self.v[2]+1/6*dt*(k1z+2*k2z+2*k3z+k4z)

            t=t+dt

            x.append(x[-1]+dx)
            y.append(y[-1]+dy)
            z.append(z[-1]+dz)

            
        return x, y, z

    


elektron = Cestica(9.109e-31, -1.6e-19, [0,0,10], [3,5,5], [10e2,10e2,10e2])
x_e, y_e, z_e = elektron.RungeKuttara(n=4)


pozitron = Cestica(9.109e-31, 1.6e-19, [0,0,10], [3,5,5], [10e2,10e2,10e2])
x_p, y_p, z_p = pozitron.RungeKuttara(n=4)


# --- UREDAN PLOT ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Crtanje putanja
ax.plot3D(x_e, y_e, z_e, color='blue', linewidth=2, label='Elektron')
ax.plot3D(x_p, y_p, z_p, color='red', linewidth=2, label='Pozitron')

# Oznake osi i naslov
ax.set_title("Usporedba putanja: Elektron vs. Pozitron", fontsize=14, pad=15)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Dodavanje legende
ax.legend()

# Prikaz
plt.show()