##pedir texto
##contar cantidad de vocales

oracion=input('ingrese su oracion')
vocales=['a','e','i','o','u']
contadorvocales=0
for letras in oracion:
    if letras in vocales:
        contadorvocales+=1
print('la cantidad de vocales es: ', 
contadorvocales)