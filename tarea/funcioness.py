password='123456789'
condicion=True
intentos=1
while condicion==True:
    print('este es tu'intentos,'intentos') 
    newPaassword=input('ingresa la contraseña : ')
    if newPaassword==password:
        print('binevenidos al sistema')
        condicion=False
    else:
        print('incorrecto')
        intentos+=1