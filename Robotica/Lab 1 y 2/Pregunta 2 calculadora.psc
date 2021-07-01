Algoritmo Indice
	Escribir "Ingresa tu peso en kilogramos"
	leer peso
	Escribir "Ingresa tu estatura en metros"
	leer estatura
	imc<-Peso/(estatura*estatura)
	Escribir "=============="
	Escribir "Tu IMC es:", imc
	Escribir "=============="
	Si imc<18.5 
		Escribir "Tu IMC indica que estas en un peso inferior al normal."
	FinSi
	Si imc>=18.5 y imc<=24.9
		Escribir "Tu IMC indica que tu peso es normal"
	FinSi
	Si imc>=25.0 y imc<=29.9
		Escribir "Tu IMC indica que tu peso es superior al normal"
	FinSi
	Si imc>30
		Escribir "Tu IMC indica que esta en sobrepeso"
	FinSi
FinAlgoritmo
