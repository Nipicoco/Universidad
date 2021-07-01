import serial as rs

sMsg = '''
                 ----[ << CARTA >> ]----
                          
         

         Si quieres ser exitoso profesionalmente,
         debes estudiar y practicar mucho el arte
         de la programacion.


                     By Alberto Caro
         
       ''' 

nFH = open('carta.txt','w')
nFH.write(sMsg)
nFH.close()





