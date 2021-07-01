import serial as se

se = se.Serial("COM3", baudrate=2400, timeout=None)

while True:
    d=data.decode()[:-1]
    data = se.readline()
    print(d)

se.close()