import pyfirmata
import time

# Conectar ao Arduino (substitua 'COM3' pela porta correta)
board = pyfirmata.Arduino('COM3')

# Pino digital onde o LED está conectado (pino 13)
led_pin = board.get_pin('d:13:o')

while True:
    # Acender o LED
    led_pin.write(1)
    print("LED ligado")
    time.sleep(1)
    
    # Apagar o LED
    led_pin.write(0)
    print("LED apagado")
    time.sleep(1)
