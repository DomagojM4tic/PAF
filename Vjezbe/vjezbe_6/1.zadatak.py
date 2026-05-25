import arithm as ar


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


print("Dijametri: ")

for value in dijametri_2R.keys():
        print(f"Srednja vrijednost za {value}:")
        print(ar.aritmeticka_sredina(dijametri_2R[value]))
        print(f"Standardna devijacija: {value}:")
        print(ar.standardna_devijacija(dijametri_2R[value]))
    
print("Duljine: ")
for value in duljine_L.keys():
        print(f"Srednja vrijednost za {value}:")
        print(ar.aritmeticka_sredina(duljine_L[value]))
        print(f"Standardna devijacija: {value}:")
        print(ar.standardna_devijacija(duljine_L[value]))

print("Mase: ")
for value in mase_m.keys():
        print(f"Srednja vrijednost za {value}:")
        print(ar.aritmeticka_sredina(mase_m[value]))
        print(f"Standardna devijacija: {value}:")
        print(ar.standardna_devijacija(mase_m[value]))


#print(ar.aritmeticka_sredina(dijametri_2R["Valjak 1"]))
#print(ar.standardna_devijacija(dijametri_2R["Valjak 1"]))
