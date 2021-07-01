import serial as s

PORT = "COM2"


se = s.Serial("COM3", baudrate=2400, timeout=None)

carta = open("carta.txt","r")
contenido = carta.read()

while True:
    contenido = (contenido)
    se.write(bytes(contenido, 'ascii'))
    break

se.close()