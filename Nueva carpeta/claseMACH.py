operacion='resta'
match operacion:
    case 'suma':
        print('realizare la suma')
    case 'resta':
        print('realizare la resta')
    case 'multiplicacion':
        print('realizare la multiplicacion')
    case _:
        print('no hay operacion')