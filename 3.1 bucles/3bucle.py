# print("tabla de Multiplicacion")
#v = int (input("Igrese un valor para la tabla -> "))
num = 489
aux = 0
for i in range(1,num + 1):
    if (num % i == 0 ):
        print (num," % ", i , " = ",num % i)
        aux = aux + 1
    else:
        print (num," % ", i , " = ",num % i)
# print (aux)
if ( aux == 2):
    print ("Si es PRIMO ")
else:
    print ("No es primo")

