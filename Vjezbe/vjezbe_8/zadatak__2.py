import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


kut_deg = [0 , 5 , 10 , 15 , 20 , 25 , 30 , 35 , 40 , 45 , 50 , 55 , 60 , 65 , 70 , 75 , 80 , 85]

T_120 = [0.8020 , 0.8187 , 0.8327 , 0.8660 , 0.8980 , 0.9153 , 0.9293 , 0.9653 , 0.9747 , 1.0200 , 1.0373 , 1.1160 , 1.1780 , 1.2733 , 1.4180 , 1.6373 , 1.9100 , 2.5460]

T_240 = [1.0140 , 1.0320 , 1.0433 , 1.0673 , 1.0840 , 1.1320 , 1.1440 , 1.1720 , 1.1980 , 1.2293 , 1.2813 , 1.3573 , 1.4200 , 1.5600 , 1.7413 , 1.9840 , 2.4473 , 3.1573]

g=9.81

def teorijski_period(theta, l):
    theta_rad = np.radians(theta)
    return 2 * np.pi * np.sqrt(l / (g * np.cos(theta_rad)))

popt_120, _ = curve_fit(teorijski_period, kut_deg, T_120, p0=[0.120])
popt_240, _ = curve_fit(teorijski_period, kut_deg, T_240, p0=[0.240])
l_fit_120 = popt_120[0]
l_fit_240 = popt_240[0]
L_stvarno_120 = 0.120  
L_stvarno_240 = 0.240 

rel_greska_120 = abs(l_fit_120 - L_stvarno_120) / L_stvarno_120 * 100
rel_greska_240 = abs(l_fit_240 - L_stvarno_240) / L_stvarno_240 * 100
print(f"Fitana (L=120mm): {l_fit_120:.4f} m | Relativna pogreška: {rel_greska_120:.2f}%")
print(f"Fitana (L=240mm): {l_fit_240:.4f} m | Relativna pogreška: {rel_greska_240:.2f}%")


kut_plot = np.linspace(0, 85, 200)
T_teorija_120 = teorijski_period(kut_plot, l_fit_120)
T_teorija_240 = teorijski_period(kut_plot, l_fit_240)


plt.scatter(kut_deg, T_120, color='blue', label='Mjerenja (L=120 mm)')
plt.plot(kut_plot, T_teorija_120, color='blue', linestyle='--', label=f'Teorija fit (l={l_fit_120:.3f}m)')

# Crtanje mjerenja (scatter) i teorije (plot) za 240 mm
plt.scatter(kut_deg, T_240, color='red', label='Mjerenja (L=240 mm)')
plt.plot(kut_plot, T_teorija_240, color='red', linestyle='--', label=f'Teorija fit (l={l_fit_240:.3f}m)')

# Uređivanje grafa
plt.title('Ovisnost perioda titranja o kutu nagiba osi njihala', fontsize=14)
plt.xlabel('Kut nagiba $\\theta$ [°]', fontsize=12)
plt.ylabel('Period $T$ [s]', fontsize=12)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.xlim(0, 90)

plt.show()





