#Busqueda Binaria en Python

import math

numero_buscado=int(input("Introduce el numero que queres buscar:"))

lista=[10,20,30,40,50,60,70,80,90,100]

divisor = 1/2

divisor2 = 1/2 

for i in lista:

	if i == lista[len(lista)-1]
		print("El numero buscado no se encuentra en la lista")

	if lista[math.floor(len(lista)*(divisor))] < numero_buscado:
		divisor2 = divisor2/2
		divisor = divisor + divisor2
		print(divisor)

	elif lista[math.floor(len(lista)*(divisor))] > numero_buscado:
		divisor2 = divisor2/2
		divisor = divisor - divisor2
		print(divisor)

	else:
		print("La poscicion del numero buscado en la lista es:" + str(math.floor(len(lista)*(divisor)) + 1))
		break