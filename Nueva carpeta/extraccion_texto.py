##tendremos una variable con el mensaje hola mundo
##pedir al usuario un texto
##si el texto ingrsesado es hola
##mostar el mensaje completo
#si el texto ingresadoes como es estas
##extraeras del messaje la palabra hola
##si el texto ingresado es saludo
##extraeras del mensaje la palabra mundo
##si es ingresado otro texto
##mostar le mensaje error
from operator import truediv

mensaje='hola mundo'
texto=input('ingrese texto: ')
match texto:
    case 'hola':
        print(mensaje[:])
    case 'como estas':
        print(mensaje[:4])
    case 'saludos':
        print(mensaje[5:])
    case _:
        print('error')