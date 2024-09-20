import time

# Simulação do pyFirmata e da placa Arduino
class SimulatedPin:
    def __init__(self, pin):
        self.pin = pin
        self.state = 0

    def write(self, value):
        self.state = value
        if self.state == 1:
            print(f"Simulação: LED no pino {self.pin} está ACESO")
        else:
            print(f"Simulação: LED no pino {self.pin} está APAGADO")

class SimulatedBoard:
    def __init__(self):
        print("Simulação: Arduino conectado")

    def get_pin(self, pin):
        print(f"Simulação: Pino {pin} configurado")
        return SimulatedPin(pin)

    def exit(self):
        print("Simulação: Conexão com Arduino finalizada")

# Simulando o código que controlaria o Arduino
board = SimulatedBoard()
led_pin = board.get_pin('d:13:o')

while True:
    # Simular acender o LED
    led_pin.write(1)
    time.sleep(1)
    
    # Simular apagar o LED
    led_pin.write(0)
    time.sleep(1)
