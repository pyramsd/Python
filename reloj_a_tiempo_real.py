# hacer un reloj en tiempo real que vaya mostrando la hora cada segundo
#  conseguir la hora solo una sola vez y que se vaya actualizando
import time

class TIME:
    def __init__(self):
        while True:
            localtime = time.localtime()
            result = time.strftime("%H:%M:%S %p", localtime)
            print(result)
            time.sleep(1)

t = TIME()
