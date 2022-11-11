
#2. asignamos un nombre a la 
#3. siempre tiene que recibir parametros
  #()--no resive parametros
  #(nombre)---que 1 funcion recibiendo un paramwetro
  #(edad,nombre)
#4.siempre la funcion tiene que retornar un tipo de dato
def saludo(nombre):
    respuesta=f'hola como estas {nombre}'
    return respuesta
#como uso
arrayAmigos=['ronald','claudio','diego','jose','kevin']
for amigo in range(0,len(arrayAmigos)):
    print(saludo(arrayAmigos[amigo]))

## crear una funcion que me retorne los n numeros de fibonacci
1 1 2 3 5 8 13 
x=0
y=1
z=0
while True:
    n=int(input('ingrese num mayor a 1: '))
    if n>1:
        break
print("1",end=" ")
for i in range(0,n):
    z=x+y
    print(f"{z}",end=" ")
    x=y
    y=z
    z=y
    x=z
print("")
##crear una funcion que me retorne el factoeial de un numero n
 5=5*4*3*2*1
 7=7*6*5*4*3*2*1
 numero=int(input('numero: '))
factorial=1
if numero !=0:
    for i in range(1,numero+1):
        factorial*=i
        
print("factorial:",factorial)
##crear una funcion que me diga si una palabra es palindromo
ada
ala
def palindromo(cadena):
    izquierda = 0
    derecha = len(cadena)-1
 
    while  derecha >= izquierda:
        if not cadena[izquierda] == cadena[derecha]:
            return False

        izquierda += 1
        derecha -= 1 

    return True

#print(palindromo('ana'))
#print(palindromo('oso'))