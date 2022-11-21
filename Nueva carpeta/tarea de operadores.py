##crear una funcion de operadores matematicos 
##operadorMtematico(num1,num2,operacion)
##operadorMtematico(4,5,'suma esto')
##por consola la suma de 44
##por consola es un error


from html.entities import name2codepoint

print('ingrese el primer numero: ')
n1=float(input())
print('ingrese el segundo numero: ')
n2= float(input())
suma= n1 + n2
resta= n1 - n2
multiplicacion= n1 * n2
divicion= n1 / n2
print('la suma es: ', suma)
print('la resta es: ', resta)
print('la multiplicaion es: ', multiplicacion)
print('la divicion es: ', divicion)







#sentences=input('enter sentences: ')
#vocales=['a','e','i','o','u']
#def countVocals(oracion,vocal):
#    contador=0
#    for word in oracion:
#        if word in vocal:
#            contador+=1
#    return contador
#print(countVocals(sentences,vocales))







def mensaje(nombre,apellido,accion):
    if accion == 'saludo':
        mensaje='hola',nombre,apellido,'como estas'
    elif accion=='despedida':
        mensaje='adios',apellido,nombre
    return mensaje
print(mensaje('mozar','castillo','saludo'))
