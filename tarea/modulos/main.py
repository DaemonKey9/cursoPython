##aqui en main ejecutar mis funciones
# from funciones import operaciones
import funciones as op
respuesta=op.operaciones(10,8,'suma')
respuesta2=op.operaciones(100,20,'resta')
respuesta3=op.operaciones(5,10,'por')
print(f'la suma es {respuesta}')
print(f'la resta es{respuesta2}')
print(f'la multiplicaion es {respuesta3}')
print(op.saludo())