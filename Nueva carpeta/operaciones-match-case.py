mensajeopciones="""
selecciona una opcion 
1)suma
2)resta
3)devicion
4)multiplicacion
5)salir
"""
while True:
    print(mensajeopciones)
    opcion = input('ingrese una opcion: ')
    num1=int(input('ingrese el primer num'))
    num2=int(input('ingrese el segundo num'))
    match opcion:
        case '1':
            print(f'la suma de{num1}+{num2}={num1+num2}')
        case '2':
            print(f'la resta de{num1}-{num2}={num1-num2}')
        case '3':
            print(f'la divicion de{num1}/{num2}={num1/num2}')
        case '4':
            print(f'la multiplicacion de{num1}*{num2}={num1*num2}')
        case '5':
            break
        case __:
            print('esta opcion no existe')