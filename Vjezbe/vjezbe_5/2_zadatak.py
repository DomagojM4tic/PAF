N=[200, 2000, 20000]


def funkcija(N):
    broj = 5
    terca=1/3

    for i in range(N):
        broj=broj+terca
    
    for i in range(N):
        broj=broj-terca

    return broj


for n in N:
    print(funkcija(n))