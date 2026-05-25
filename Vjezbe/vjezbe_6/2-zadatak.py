import arithm as ar
import numpy as np
#mjereni u mm
dijametri_2R = {
    "Valjak 1": [19.98, 20.18, 20.10, 20.08, 19.74],
    "Valjak 2": [19.92, 19.82, 19.96, 19.98, 19.88],
    "Valjak 3": [24.96, 24.98, 24.98, 24.92, 24.94]
}

# Table 2: Duljine L [mm] mjerene pomičnom mjerkom
duljine_L = {
    "Valjak 1": [49.80, 49.00, 50.48, 49.80, 49.96],
    "Valjak 2": [52.56, 52.50, 52.62, 52.58, 52.54],
    "Valjak 3": [55.34, 55.40, 55.30, 55.44, 55.48]
}

# Table 3: Mase m [g] mjerene vagom
mase_m = {
    "Valjak 1": [138.92, 138.98, 139.20, 138.90, 138.92],
    "Valjak 2": [128.65, 128.60, 128.65, 128.35, 128.50],
    "Valjak 3": [71.89, 71.90, 71.79, 71.85, 71.70]
}

RhoLit = {
    "Valjak 1": 8.9, #bakar
    "Valjak 2": 7.87,#zeljezo
    "Valjak 3": 2.70#aluminij
}


def volumen_valjka(R, L):
    r=R/10
    l=L/10
    return ((r)**2)*np.pi*l


def sigma_volumena(R, R_sigma, L, L_sigma):
    return np.sqrt(((2*R*np.pi*L*R_sigma)**2) + ((R**2)*np.pi*L_sigma)**2)/1000

 #R_sigma=(2*R*np.pi*L*ar.standardna_devijacija(R))**2
    #L_sigma=(np.pi*(R**2)*ar.standardna_devijacija(L))**2


def gustoca(m,V):
    return m/V

def sigma_gustoca(m, m_sigma, V, V_sigma):
    return np.sqrt(((1/V*m_sigma)**2)+(m/(V**2)*V_sigma)**2)



for key in dijametri_2R.keys() and duljine_L.keys():

    #R_sigma=(2*ar.aritmeticka_sredina(dijametri_2R[key])*np.pi*ar.aritmeticka_sredina(duljine_L[key])*ar.standardna_devijacija(dijametri_2R[key]))**2
    #L_sigma=(np.pi*(ar.aritmeticka_sredina(dijametri_2R[key])**2)*ar.standardna_devijacija(duljine_L[key]))**2
    radijus=[x/2 for x in dijametri_2R[key]]
    duljine=np.array(duljine_L[key])

    R=ar.aritmeticka_sredina(radijus)
    L=ar.aritmeticka_sredina(duljine_L[key])
    r_sigma=ar.standardna_devijacija(radijus)
    l_sigma=ar.standardna_devijacija(duljine)
    m_sigma=ar.standardna_devijacija(mase_m[key])
    
    volumen=volumen_valjka(R,L)
    Vpogreska=sigma_volumena(R,r_sigma,L,l_sigma)
    #ispis
    print(f"Volumen {key}: ")
    print(f"{volumen:.2} cm^3 ------ pogreska: {Vpogreska}")
    

    m=ar.aritmeticka_sredina(mase_m[key])
    m_sigma=ar.standardna_devijacija(mase_m[key])
    Rho=gustoca(m,volumen)
    #ispis
    Gpogreska=sigma_gustoca(m,m_sigma,volumen,Vpogreska)

    relativna_pog=np.abs(Rho-RhoLit[key])/RhoLit[key]*100

    print(f"Gustoca {key}: ")
    print(f"{Rho:.2} g/cm^3 ------ pogreska: {Gpogreska}\n Relativna pogreska: {relativna_pog:.2}% \n")




    








