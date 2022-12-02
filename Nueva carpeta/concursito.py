##definir una funcion max() que tome como argumento un array de num y devuelva el mayor del array
# mayor=["hoal","como estas", "hola como estas"] 
# min=max=mayor[0]
# for clase in mayor:
#      if clase < min:
#          min = clase
#      elif clase > max:
#          max = clase
# print("El mínimo es " + str(min))  


##escribir una funcion que almacene en una lista los siguientes precios,
##50,75,46,22,80,65,8, y muestre por pantalla el menor y el mayor de los precios
# precios = [50,75,46,22,80,65,8]
# min = max = precios[0]
# for precios in precios :
#     if precios < min:
#         min = precios
#     elif precios > max:
#         max = precios
# print("el minimo es " + str(min))
# print("el maximo es " + str(max))


##escribir una funcion mas larga () que tome una array de palabras y devuelva la mas larga
def mas_larga(lista):
	palabra_mayor = len(lista[0])
	palabra_mostrar = lista[0]

	for palabra in lista:
		if palabra_mayor <= len(palabra):
			palabra_mostrar = palabra
			palabra_mayor = len(palabra)
		else:
			palabra_mostrar = palabra_mostrar

	print(palabra_mostrar)


lista = ["hola", "como estas", "hola como estas"]
mas_larga(lista)


##escribir un programa que reciba una cadena de caracter y duelvuelva un diccionario con cada palabra que contiene
# def creador_dict(cadena):
#   '''Recibe una cadena de caracteres y regresa un diccionario con las palabras (keys) y conteo (value)'''
#   lista1= cadena.split()
#   dict1={}
#   for i in lista1:
#     if i in dict1:
#       dict1[i] +=1
#     else:
#       dict1[i]= 1
#   return dict1

# def contador_dict(dictionario):
#   '''Recibe un diccionario y regresa una tupla: la palabra mas repetida y cuantas veces aparece'''
#   palabra_frecuente= ''
#   cantidad=0
#   for keys,values in dictionario.items():
#     if values > cantidad:
#       cantidad= values
#       palabra_frecuente= keys
#   return palabra_frecuente,cantidad
# entrada=input('Ingrese su cadena de caracteres: ')
# print(creador_dict(entrada))
# print(contador_dict(creador_dict(entrada)))