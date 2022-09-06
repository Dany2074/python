'''
1.	Calcular las notas de presentación de N alumnos (validar que N sea entero
 y mayor a cero). La nota de presentación de cada alumno se calcula según
  el siguiente criterio: 
-	Parte práctica: 10%
-	Parte de problemas: 50%
-	Parte teórica el 40%
El programa debe ser capaz de solicitar el apellido paterno 
(debe tener como mínimo tres caracteres), género (en forma aleatoria)
 y las notas de cada alumno (validar que las notas estén en el rango 1.0 a 7.0)
  y luego mostrar:
-	Género y Nota de presentación de cada alumno y Nota mínima 
que debe sacarse en el examen para aprobar 
(nota de presentación equivale a 60% y nota de examen 40%)
-	Promedio de las notas de presentación de las mujeres
-	Apellido del alumn@ con peor y mejor nota de presentación

'''
import random
while(True):#cantidad ingresada
	try:
		n=int(input("Ingrese la cantidad de alumnos:\n cantidad:"))
		if n>0:
			break
	except ValueError:
		print("\n\tDebe ser un numero entero!!\n")
print("\nLa cantidad ingresada es",n)
i0=0
i1=0
mayor=0
menor=8
apeMayor=0
apeMenor=0
sumaM=0
while(i0<n):#while con n 
	i0=i0+1
	print("\n\tCantidad de alumnos ingresados",i0)
	while(True):#Apellido paterno
		apellido=input("Ingresa Apellido Paterno del alumno: ")
		if(len(apellido)>=3):
			if(apellido.isalpha()):
				break
			else:
				print("El apellido debe tener sólo letras")
		else:
			print("el apellido debe ser mayor o igual a 3 caracteres")

	gen=random.choice(["Masculino","Femenino"])
	#print("genero:",gen)
	while(True):#nota 1
		try:
			nota1=float(input("Ingrese nota 1.Parte práctica 10%:"))
			if(nota1>=1 and nota1<=7):
				break
			else:
				print("\n\tNo valido:nota debe estar entre 1 y 7:\n")
		except ValueError:
				print("\n\tNota no valida:nota debe ser un numero:\n")
	while(True):#nota 2
		try:
			nota2=float(input("Ingrese nota 2.Parte de problemas: 50%:"))
			if(nota2>=1 and nota2<=7):
				break
			else:
				print("\n\tNo valido:nota debe estar entre 1 y 7:\n")
		except ValueError:
				print("\n\tNota no valida:nota debe ser un numero:\n")
	while(True):#nota 3
		try:
			nota3=float(input("Ingrese nota 3.Parte teórica el 40%:"))
			if(nota3>=1 and nota3<=7):
				break
			else:
				print("\n\tNo valido:nota debe estar entre 1 y 7:\n")
		except ValueError:
				print("\n\tNota no valida:nota debe ser un numero:\n")
	np=round(nota1*0.1+nota2*0.5+nota3*0.4,1)
	ne=round((4-np*0.6)/0.4,1)
	print("Genero:",gen,"Nota de presentacion:",np)
	print("Nota de examen para aprobar:",ne)
	if gen=="Femenino":
		i1=i1+1
		sumaM=sumaM+np
	if mayor<np:
		mayor=np
		apeMayor=apellido
	if menor>np:
		menor=np
		apeMenor=apellido
print("-Alumno con la mejor nota de presentacion apellido:",apeMayor,"\n-Alumno con la peor nota de presentacion apellido:",apeMenor)
if i1!=0:
	Prom_nota_mujer=sumaM/i1
	print("El promedio de nota de presentacion de mujeres es:",Prom_nota_mujer)
else:
	print("No se ingresaron alumnos mujeres")