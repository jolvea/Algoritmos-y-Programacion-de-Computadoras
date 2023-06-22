x=15
y=5
print("SELECCIONE UNA OPCION")
print("=====================")
print(" 1: SUMA \n 2: RESTA\n 3: MULTIPLICACION\n 4: DIVISION")
var = input("Ingrese una opcion a realizar-> ")
if var == "1":
    res=x+y
    print("La suma es: ",res)
elif var == "2":
    res=x-y
    print("La resta es: ",res)
elif var == "3":
    res=x*y
    print("La multiplicacion es: ",res)
elif var == "4":
    res=x/y
    print("La division es: ",res)
else:
    print("No selecciono una opcion VALIDA")
