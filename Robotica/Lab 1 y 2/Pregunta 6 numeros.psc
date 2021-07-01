Algoritmo numerosmayor
	Definir n1,n2,n3 Como Entero
	Escribir 'Ingresar numero 1: '
	Leer n1
	Escribir '========='
	Escribir 'Ingresar numero 2: '
	Leer n2
	Escribir '========='
	Escribir 'Ingresar numero 3: '
	Leer n3
	Si n1=n2 Entonces
		Escribir '========='
		Escribir 'Los numeros 1 y 2 son iguales.'
		Escribir 'Intentar otra vez'
		Escribir '========='
	FinSi
	Si n2=n3 Entonces
		Escribir '========='
		Escribir 'Los numeros 2 y 3 son iguales.'
		Escribir 'Intentar otra vez'
		Escribir '========='
	FinSi
	Si n1=n3 Entonces
		Escribir '========='
		Escribir 'Los numeros 1 y 3 son iguales.'
		Escribir 'Intentar otra vez'
		Escribir '========='
	FinSi
	Si n2>n1 Y n3<n1 Entonces
		Escribir '========='
		Escribir 'El numero menor es ',n3,' y el numero mayor es ',n2
		Escribir '========='
	FinSi
	Si n1>n2 Y n3>n1 Entonces
		Escribir '========='
		Escribir 'El numero menor es ',n2,' y el numero mayor es ',n3
		Escribir '========='
	FinSi
	Si n1>n2 Y n3<n2 Entonces
		Escribir '========='
		Escribir 'El numero menor es ',n3,' y el numero mayor es ',n1
		Escribir '========='
	FinSi
	Si n3>n2 Y n2>n1 Entonces
		Escribir '========='
		Escribir 'El numero menor es ',n1,' y el numero mayor es ',n3
		Escribir '========='
	FinSi
FinAlgoritmo
