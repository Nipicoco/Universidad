Algoritmo anios
Definir anio,dia,mes Como Entero
	Repetir
		Escribir 'Ingrese un dia: '
		Leer dia
		Si dia>31 Entonces
			Imprimir "========="
			Escribir 'El dia supera el limite permitido!'
			Imprimir "========="
		FinSi
	Hasta Que dia>=1 Y dia<=31
	Imprimir "========="
	Repetir
		Escribir 'Ingrese un mes: '
		Leer mes
		Si mes>12 Entonces
			Imprimir "========="
			Escribir 'El mes supera el limite permitido'
			Imprimir "========="
		FinSi
	Hasta Que mes>=1 Y mes<=12
	Imprimir "========="
	Repetir
	Escribir 'Ingrese un año: '
		Leer anio
		Si anio>=9999 Entonces
			Imprimir "========="
			Escribir 'El año supera el limite permitido'
			Imprimir "========="
		FinSi
	Hasta Que anio>=0 Y anio<=9999
	Imprimir "========="
	Imprimir "La fecha es: ", dia, "/",mes, "/", anio
FinAlgoritmo

