import math
valor = 963
print("Sistema para calcular Billetes y Monedas")
print("El valor es: " + str(valor))
# para billetes de 200
v200 = math.trunc(valor/200)
valor = valor % 200

# para billetes de 100
v100 = math.trunc(valor/100)
valor = valor % 100

# para billetes de 50
v50 = math.trunc(valor/50)
valor = valor % 50

# para billetes de 20
v20 = math.trunc(valor/20)
valor = valor % 20

# para billetes de 10
v10 = math.trunc(valor/10)
valor = valor % 10

# para monedas de 5.00
v5 = math.trunc(valor/5)
valor = valor % 5

# para monedas de 2.00
v2 = math.trunc(valor/2)
valor = valor % 2

# para monedas de 1.00
v1 = math.trunc(valor/1)
valor = valor % 1

# para monedas de 0.50
v05 = math.trunc(valor/0.5)
valor = valor % 0.5

# para monedas de 0.20
v02 = math.trunc(valor/0.2)
valor = valor % 0.2

# para monedas de 0.10
v01 = math.trunc(valor/0.1)
valor = valor % 0.1

print("EXISTE "+ str(v200) + " BILLETES DE S/. 200.00")
print("EXISTE "+ str(v100) + " BILLETES DE S/. 100.00")
print("EXISTE "+ str(v50) + " BILLETES S/. 50.00")
print("EXISTE "+ str(v20) + " BILLETES S/. 20.00")
print("EXISTE "+ str(v10) + " BILLETES S/. 10.00")
print("EXISTE "+ str(v5) + " MONEDAS S/. 5.00")
print("EXISTE "+ str(v2) + " MONEDAS S/. 2.00")
print("EXISTE "+ str(v1) + " MONEDAS S/. 1.00")
print("EXISTE "+ str(v05) + " MONEDAS S/. 0.50")
print("EXISTE "+ str(v02) + " MONEDAS S/. 0.20")
print("EXISTE "+ str(v01) + " MONEDAS S/. 0.10")