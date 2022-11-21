##escribe una funcion en python que acepte una lista y te genere otra lista elimindo los dupicados numeros

def delDuplicate(array):
    newArray=[]
    for el in  array:
        if el not in newArray:
            newArray.append(el)
    return newArray
arrayD=[1,1,2,4,5,5,8,8,6,6]
print(delDuplicate(arrayD))

##escriba una funcion que caepte una lista y genere otra con los numeros pares

def numPar(array):
    newArray=[]
    for r in array:
        if r % 2 == 0:
            newArray.append(r)
    return newArray
arrayD=[1,2,3,3,4,6,20,5,8,4,8]
print(numPar(arrayD))

      
    
  


##escriuba una funcion que acepte una lista y genere otra eliminando los duplicados textos

def delDuplicate(array):
    newArray=[]
    for el in  array:
        if el not in newArray:
            newArray.append(el)
    return newArray
arrayD=['a','a','b','c','c']
print(delDuplicate(arrayD))