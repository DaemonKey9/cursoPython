
from asyncio.windows_events import INFINITE


contador=INFINITE
for num in range(0,contador):
    texto=input('ingrese texto: ')
    if texto=='salir' :
        break
   