#menu de opciones
#sumar
#resta
#divicion
#multiplicacion
#salir
##digite el num de la opcion(1-5);
##digite el primer num:
##digite el segundo num:
#-----------------
#la suma es :
#digite el num de la opcion(1-5);
from ipaddress import summarize_address_range
from pdb import Restart


n1= float(input('tu primer num:'))
n2= float(input('tu primer num:'))
opcion = 0 
while True :
    print(""""
    que deceas hacer
    1) suma 
    2) Resta
    4) divicion
    3) multiplicar
    5) salir
    """)
    opcion =int (input ('elige una opcion'))
    if opcion == 1:
        print('')
        print('RESULTADO: la suma de',n1,"+",n2,"es igual a",n1+n2)
    elif opcion ==2:
        print('')
        print('RESULTADO: la resta de',n1,"-",n2,"es igual a",n1-n2)
    elif opcion ==3:
        print('')
        print('RESULTADO: la multiplicaion de',n1,"*",n2,"es igual a",n1*n2)
    elif opcion ==4:
        print('')
        print('RESULTADO: la divicion de',n1,"/",n2,"es igual a",n1/n2)
    elif opcion == 5:
        print ('opcion incorrecta')
    else:
        print ('error') 