##escribir un programa de tabla de multiplicar del 1 al 10
eval=True
while eval==True:
    num=int(input('ingresa el num : '))
    if num==0:
        print('error')
        break
    else:
        for n in range(1,12):
            print(n,'*',num,'=',n*num)
     
##if numero!=0:
## for numero in range(1,11):
##  print(numero,'*' )