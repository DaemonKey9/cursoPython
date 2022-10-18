mensaje='hola'
        #123
        #['h','o','l','a']
print (mensaje[1])
for letra in mensaje:
    print(letra)


#########@#########@#@#@##@#@#@#@#@#@#@#@
mensaje=input('ingrese un mesaje : ')
##mostrar por consola cuantas vocales a
##tiene el mansaje+
##hola como estas como te llamas
##tiene 4 vocales a


for letra in  mensaje:
    if letra=='a':
        print('aqui ta la a')
    print(letra)

#######con contador
mensaje='hola como estas '
contador=0
for letra in  mensaje:
    if letra=='a':
        contador+=1
        print('en este mensaje tines:',contador)