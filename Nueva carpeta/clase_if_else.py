mensaje='hola mundo'
texto=input('ingrese texto: ')
if texto=='hola':
    print(mensaje[:])
elif texto=='como estas':
    print(mensaje[4:])
elif texto=='saludo':
    print(mensaje[:5])
else :
    print('error')

