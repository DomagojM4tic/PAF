while True:
    try:
        x1=float(input("Unesi prvu x koordinatu: "))
        y1=float(input("Unesi prvu y koordinatu: "))
        x2=float(input("Unesi drugu x koordinatu: "))
        y2=float(input("Unesi drugu y koordinatu: "))
        break
    except ValueError:
        print("Pogrešan unos! Pokušaj ponovno!")

if x1==x2:
    print(f"jednadzba pravca je: x={x1}")
else:
    k=(y2-y1)/(x2-x1)
    l=y1-k*x1
    print(f"Jednadžba pravca je: y={k}x + {l}")
