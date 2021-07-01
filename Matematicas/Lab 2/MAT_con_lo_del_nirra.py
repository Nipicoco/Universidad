inicio = int(input("####################################################\n# Bienvenido a la calculadora y conversor de bases #\n# A continuacion se mostraran todas las opciones   #\n#                                                  #\n# 1.Calculadora de Bases                           #\n# 2. Conversor de Bases                            #\n####################################################\nIngrese su opcion: "))
if inicio ==1:
    opciones = int(input("\n\n\nQue base desea utilizar para las operaciones\n1.Base Decimal\n2.Base Binario\n3.Base Octal\n4.Base Hexadecimal\n5.Salir\nIngrese numero: "))
    if opciones == 1:
        calcular = int(input("\n\n\nQue operacion desea realizar:\n1.Sumar\n2.Restar\n3.Dividir\n4.Multiplicar\nIngrese numero: "))
        if calcular == 1:
            num1=(int(input("\nIngrese Primer numero a sumar: ")))
            num2=(int(input("\nIngrese Segundo numero a sumar: ")))
            suma = num1 + num2
            print("\nEl resultado es:", suma)
        if calcular == 2:
            num1=(int(input("\nIngrese Primer numero a restar: ")))
            num2=(int(input("\nIngrese Segundo numero a restar: ")))
            resta = num1 - num2
            print("\nEl resultado es:", resta)
        if calcular == 3:
            num1=(int(input("\nIngrese Primer numero a dividir: ")))
            num2=(int(input("\nIngrese Segundo numero a dividir: ")))
            division = num1 / num2
            print("\nEl resultado es:",division)
        if calcular == 4:
            num1=(int(input("\nIngrese Primer numero a multiplicar: ")))
            num2=(int(input("\nIngrese Segundo numero a multiplicar: ")))
            multiplicacion = num1 * num2
            print("\nEl resultado es:",multiplicacion)
        elif calcular > 4 or calcular < 1:
            print("\nIngrese numero correcto")
    if opciones == 2:
        calcular = int(input("\n\n\nQue operacion desea realizar:\n1.Sumar\n2.Restar\n3.Dividir\n4.Multiplicar\nIngrese numero: "))
        if calcular==1:
            num1=(input("\nIngrese Primer numero a sumar: "))
            num2=(input("\nIngrese Segundo numero a sumar: "))
            integer_sum = int(num1, 2) + int(num2, 2)
            binary_sum = bin(integer_sum)
            print("\nEl resultado es:",binary_sum)
        if calcular == 2:
            num1=(input("\nIngrese Primer numero a restar: "))
            num2=(input("\nIngrese Segundo numero a restar: "))
            resta = int(num1, 2) - int(num2, 2)
            binario_resta = bin(resta)
            print("\nEl resultado es:",binario_resta)
        if calcular == 3:                                            #ERROR
            num1=(input("\nIngrese Primer numero a dividir: "))
            num2=(input("\nIngrese Segundo numero a dividir: "))
            division = int(num1, 2) / int(num2, 2) 
            binario_division = bin(division)
            print("\nEl resultado es:",binario_division)
        if calcular ==4:
            num1=(input("\nIngrese Primer numero a multiplicar: "))
            num2=(input("\nIngrese Segundo numero a multiplicar: "))
            multiplicacion = int(num1, 2) * int(num2, 2)
            binario_multiplicacion = bin(multiplicacion)
            print("\nEl resultado es:",binario_multiplicacion)
        elif calcular > 4 or calcular < 1:
            print("\nIngrese numero correcto")
    if opciones == 3:
        calcular = int(input("\n\n\nQue operacion desea realizar:\n1.Sumar\n2.Restar\n3.Dividir\n4.Multiplicar\nIngrese numero: "))
        if calcular == 1:
            num1=(input("\nIngrese Primer numero a sumar: "))
            num2=(input("\nIngrese Segundo numero a sumar: "))
            suma = int(num1, 8) + int(num2, 8)
            octal_suma = oct(suma)
            print("\nEl resultado es:",octal_suma)
        if calcular == 2:
            num1=(input("Ingrese Primer numero a restar: "))
            num2=(input("Ingrese Segundo numero a restar: "))
            resta = int(num1, 8) - int(num2, 8)
            octal_resta = oct(resta)
            print("\nEl resultado es:",octal_resta)
        if calcular == 3:                                                  #ERRROR
            num1=(input("\nIngrese Primer numero a dividir: "))
            num2=(input("\nIngrese Segundo numero a dividir: "))
            division = int(num1, 8) / int(num2, 8)
            octal_division = oct(division)
            print("\nEl resultado es:",octal_division)
        if calcular == 4:
            num1=(input("\nIngrese Primer numero a multiplicar: "))
            num2=(input("\nIngrese Segundo numero a multiplicar: "))
            multiplicacion = int(num1, 8) * int(num2, 8)
            octal_multiplicacion = oct(multiplicacion)
            print("\nEl resultado es:",octal_multiplicacion)
        elif calcular > 4 or calcular < 1:
            print("\nIngrese numero correcto")
    if opciones == 4:
        calcular = int(input("\n\n\nQue operacion desea realizar:\n1.Sumar\n2.Restar\n3.Dividir\n4.Multiplicar\nIngrese numero: "))
        if calcular == 1:
            num1=(input("\nIngrese Primer numero a sumar: "))
            num2=(input("\nIngrese Segundo numero a sumar: "))
            suma = int(num1, 16) + int(num2, 16)
            hexa_suma = hex(suma)
            print("\nEl resultado es:",hexa_suma)
        if calcular == 2:
            num1=(input("\nIngrese Primer numero a restar: "))
            num2=(input("\nIngrese Segundo numero a restar: "))
            resta = int(num1, 16) - int(num2, 16)
            hexa_resta = hex(resta)
            print("\nEl resultado es:",hexa_resta)
        if calcular == 3:                                                 #ERROR
            num1=(input("\nIngrese Primer numero a dividir: "))
            num2=(input("\nIngrese Segundo numero a dividir: "))
            division = int(num1, 16) / int(num2, 16)
            hexa_division = hex(division)
            print("\nEl resultado es:",hexa_division)
        if calcular ==4:
            num1=(input("\nIngrese Primer numero a multiplicar: "))
            num2=(input("\nIngrese Segundo numero a multiplicar: "))
            multiplicacion = int(num1, 16) * int(num2, 16)
            hexa_multiplicacion = hex(multiplicacion)
            print("\nEl resultado es:",hexa_multiplicacion)
        elif calcular > 4 or calcular < 1:
            print("\nIngrese numero correcto")
    if opciones == 5:
        print("\n\n\nAcaba de salir")
    elif opciones > 5 or opciones < 1:
        print("\nIngrese numero correcto")
if inicio ==  2:
    tipo = int(input("\n\n\nQue conversor desea utilizar\n1.Decimal a Binario\n2.Decimal a Octadecimal\n3.Decimal a Hexadecimal\n4.Binario a Decimal\n5.Binario a Octadecimal\n6.Binario a Hexadecimal\n7.Octadecimal a Decimal\n8.Octadecimal a Binario\n9.Octadecimal a Hexadecimal\n10.Hexadecimal a Decimal\n11.Hexadecimal a Binario\n12.Hexadecimal a Octadecimal\nSeleccione una opcion: "))
    if tipo == 2:
        numero = int(input("Ingrese el valor en decimal (entero): "))
        lista = [] #creo una lista vacia

        while numero >= 1:
            lista.append(str(numero % 8)) #lleno la lista con el .append
            numero //= 8
        print("La conversión de decimal a octal es: ")
        print("".join(lista[::-1]))

    elif tipo == 1:
        def decimal_a_binario(decimal):
            if decimal <= 0:
                return "0"
            # Aquí almacenamos el resultado
            binario = ""
            # Mientras se pueda dividir...
            while decimal > 0:
            # Saber si es 1 o 0
                residuo = int(decimal % 2)
            # E ir dividiendo el decimal
                decimal = int(decimal / 2)
            # Ir agregando el número (1 o 0) a la izquierda del resultado
                binario = str(residuo) + binario
            return binario


        decimal = int(input("Ingresa un número decimal: "))
        binario = decimal_a_binario(decimal)
        print(f"El número {decimal} es {binario} en binario")

    elif tipo == 3:
        # Función que regresa el verdadero valor hexadecimal.
        # Por ejemplo, si recibe un 15 devuelve f, y si recibe un número menor a 10, devuelve el número sin modificarlo
        def obtener_caracter_hexadecimal(valor):
            # Lo necesitamos como cadena
            valor = str(valor)
            equivalencias = {
                "10": "a",
                "11": "b",
                "12": "c",
                "13": "d",
                "14": "e",
                "15": "f",
            }
            if valor in equivalencias:
                return equivalencias[valor]
            else:
                return valor


        def decimal_a_hexadecimal(decimal):
            hexadecimal = ""
            while decimal > 0:
                residuo = decimal % 16
                verdadero_caracter = obtener_caracter_hexadecimal(residuo)
                hexadecimal = verdadero_caracter + hexadecimal
                decimal = int(decimal / 16)
            return hexadecimal


        decimal = int(
            input("Escribe un número decimal, yo lo convertiré a hexadecimal: "))
        hexadecimal = decimal_a_hexadecimal(decimal)
        print(f"El decimal {decimal} es {hexadecimal} en hexadecimal")

    elif tipo == 4:
        def octal_a_decimal(octal):
            decimal = 0
            posicion = 0
            # Invertir octal, porque debemos recorrerlo de derecha a izquierda
            # pero for in empieza de izquierda a derecha
            octal = octal[::-1]
            for digito in octal:
                valor_entero = int(digito)
                numero_elevado = int(8 ** posicion)
                equivalencia = int(numero_elevado * valor_entero)
                decimal += equivalencia
                posicion += 1
            return decimal


        octal = input("Ingresa un número octal: ")
        decimal = octal_a_decimal(octal)
        print(f"El octal {octal} es {decimal} en decimal")

    elif tipo == 5:
        def binario_a_decimal(binario):
            posicion = 0
            decimal = 0
            # Invertir la cadena porque debemos recorrerla de derecha a izquierda
            binario = binario[::-1]
            for digito in binario:
                    #Elevar 2 a la posición actual
                    multiplicador = 2 ** posicion
                    decimal += int(digito) * multiplicador
                    posicion += 1
                    return decimal
            binario = input("Ingresa un número binario: ")
            decimal = binario_a_decimal(binario)
            print(decimal)

    elif tipo == 6:
        def obtener_valor_real(caracter_hexadecimal):
            equivalencias = {
                "f": 15,
                "e": 14,
                "d": 13,
                "c": 12,
                "b": 11,
                "a": 10,
            }
            if caracter_hexadecimal in equivalencias:
                return equivalencias[caracter_hexadecimal]
            else:
                return int(caracter_hexadecimal)


        def hexadecimal_a_decimal(hexadecimal):
            # Convertir a minúsculas para hacer las cosas más simples
            hexadecimal = hexadecimal.lower()
            # La debemos recorrer del final al principio, así que la invertimos
            hexadecimal = hexadecimal[::-1]
            decimal = 0
            posicion = 0
            for digito in hexadecimal:

                # Necesitamos que nos dé un 10 para la A, un 9 para el 9, un 11 para la B, etcétera
                valor = obtener_valor_real(digito)

                elevado = 16 ** posicion

                equivalencia = elevado * valor
                decimal += equivalencia

                posicion += 1
            return decimal


        hexadecimal = input("Ingresa un número hexadecimal: ")
        decimal = hexadecimal_a_decimal(hexadecimal)
        print(f"El hexadecimal {hexadecimal} equivale a {decimal} en decimal")
    else:
        print("Las opciones disponibles son solo A, B, C, D, E y F")
        exit()