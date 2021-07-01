Algoritmo udcum
definir nume, unid, dece, cent, unim Como Entero
Escribir "Ingresar valor de 4 digitos: "
Imprimir "========="
leer nume
Si nume>999 y nume<=9999
	unid<-nume%10
	nume<-trunc(nume/10)
	dece<-nume%10
	nume<-trunc(nume/10)
	cent<-nume%10
	nume<-trunc(nume/10)
	unim<-nume%10
	nume<-trunc(nume/10)
Imprimir "========="
Escribir "Las composicion de numeros naturales del numero es: ',unID,"U ",decE,"D ",cenT,"C ",unim,"UM"
SiNo
	Imprimir "========="
	Escribir "El numero no pertenece a  una  UM"
	FinSi
Imprimir "========="
FinAlgoritmo