import serial as se

se.Serial("COM3", timeout=None, baudrate=2400)

si  =True

while si:
    raw = se.readline()
    r = raw.decode()[:-1]
    print(r)
    if r == "adios":
         si = False
se.close()