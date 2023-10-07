# kör kerülete 2*r*3.14

r = float(input("Mi a kör sugara? (cm) "))
print("A kör kerülete:", 2*r*3.14, "cm")

# egy sóros

print("A kör kerülete:", 2*float(input("Mi a kör sugara? (cm) "))*3.14, "cm")

# háromszög területe T=a*m/2

a = int(input("Mi a oldalhosszúsága? "))
ma = int(input("Mi a magasága? "))
print("A háromszöged területe", a*ma/2, "cm\u00b2")

# bármelyik kettő oldal össze addva nagyobbnak kell lennie mint a harmadiknak

a = int(input("Az a szög legyen?: "))
b = int(input("Az b szög legyen?: "))
c = int(input("Az c szög legyen?: "))

if(a+b>c, ):
    if(a+c>b):
        if(b+c>a):
            print("ez egy háromszög")
        else:
            print("nem háromszög")
    else:
        print("nem háromszög")
else:
    print("nem háromszög")