import csv
import math
import time

archivo = "coordenadas totales.csv"

with open(archivo) as csvfile: #TO-DO 2
	L = [(float(x), float(y))  for x, y in csv.reader(csvfile, delimiter=',')]

def distancia(p1, p2):      #TO-DO 1
	distancia = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(1/2)
	return [distancia,p1,p2]

def mergeSort(arr):       	#TO-DO 3
	if len(arr) > 1: 
		mid = len(arr)//2 
		L = arr[:mid] 
		R = arr[mid:] 

		mergeSort(L) 
		mergeSort(R)
  
		i = j = k = 0 # contadorees
		  
		while i < len(L) and j < len(R): 
			if L[i][0] < R[j][0]: 
				arr[k] = L[i] 
				i+= 1
			else: 
				arr[k] = R[j]
				j+= 1
			k+= 1
		  
		while i < len(L): 
			arr[k] = L[i] 
			i += 1
			k += 1
		  
		while j < len(R): 
			arr[k] = R[j] 
			j+= 1
			k+= 1

def ordenamiento(arr):		#TO-DO 4 divide
	if len(arr) > 2: # se cumple si lo que retorna es mas de un valor 
		med = len(arr)//2
		L1 = arr[:med] 
		L2 = arr[med:]

		res_1 = ordenamiento(L1)
		res_2 = ordenamiento(L2)

		if res_1[0] < res_2[0]: # comparo distancias
			res_12 = res_1	
		else:
			res_12 = res_2

		res_12 = puntox(L1,L2,res_12)

		return res_12

	else: # CASOS BASE
		if len(arr) == 2:
			return distancia(arr[0], arr[1])
		if len(arr) == 1:
			return [math.inf,(arr[0][0],arr[0][1])]

def puntox(La, Lb, resu):		#TO-DO 5 la de los puntos en x
	xLa = La[-1][0]
	xLb = Lb[0][0]
	new_list = []

	for punto in range(len(La)-1, -1, -1):
		if abs(La[punto][0] - xLb) < resu[0]:
			new_list.append(La[punto])
		else:
			break

	for punto in Lb:
		if abs(punto[0] - xLa) < resu[0]:
			new_list.append(punto)
		else:
			break

	for i in range(len(new_list)): # calculo por fuerza bruta de todos los puntos de new_list
		for j in range(len(new_list)):
			if j <= i:
				continue
			k = distancia(new_list[i],new_list[j]) 
			if k[0] < resu[0]:
				resu = k
	return resu

def mostrar():
	x = time.time() 
	mergeSort(L) #ORDENA EN FUNCION DE COORDENADA X
	resultado = ordenamiento(L)
	x = time.time() - x
	print("Archivo usado =", archivo)
	print("Pa =", resultado[1])
	print("Pb =", resultado[2])
	print("d(Pa,Pb) =", resultado[0])
	print("Tiempo de ejecucion: ",x,"s")

print("Este proceso puede tardar un momento...")
mostrar()
input()