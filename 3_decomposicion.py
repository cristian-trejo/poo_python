class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        # Variables privadas comienzan con _(underscore)
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros = 4)

    def acelerar(self, tipo = 'despacio'):
        
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en_movimiento'


class Motor:
    # tipo = 'gasolina' -> Default Keywork, por defecto sera de tipo gasolina
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        self.cantidad = cantidad
            

class Frenos:
    def __init__(self, pistones = 4):
        self.pistones = pistones
        self._motor = Motor(cilindros = 4)
        self._temperatura = '90'
        

    def frenar(self, tipo):
        self.tipo = tipo

        if tipo == 'despacio':
            self._motor.inyecta_gasolina(8)
            self._temperatura += 5
        else:
            self._motor.inyecta_gasolina(2)
            self._temperatura += 10