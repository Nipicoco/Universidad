Algoritmo hipotenusa_triangulos
	Definir lado1,lado2 Como Real
	Escribir 'ingresar lado 1:'
	Leer lado1
	Escribir '=========='
	Escribir 'ingresar lado 2:'
	Leer lado2
	hipot <- RC((lado1^2)+(lado2^2))
	lado3 <- redon(hipot)
	Escribir '=========='
	Escribir 'La Hipotenusa del triangulo corresponde a: ',hipot
	Escribir '=========='
	Si lado1=lado2 Y lado1=lado3 Entonces
		Escribir ' Los lados ingresados corresponden a un triangulo equilatero'
	SiNo
		Si lado1=lado2 O lado2=lado3 O lado1=lado3 Entonces
			Escribir 'Los lados ingresados corresponden a un triangulo isoceles'
		SiNo
			Escribir 'Los lados ingresados corresponden a un triangulo escaleno'
		FinSi
	FinSi
FinAlgoritmo
