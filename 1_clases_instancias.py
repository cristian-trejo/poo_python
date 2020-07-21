def run():
    cuartos_hotel = [100, 101, 102, 103]
    cuarto_ocupado = [True, False, True, False]

    print(cuarto_ocupado)

if __name__ == "__main__":
    run()

    class Hotel:
        
        def __init__(self, numero_maximo_huespedes, lugares_estacionamiento):
            self.numero_maximo_huespedes = numero_maximo_huespedes
            self.lugares_estacionamiento = lugares_estacionamiento
            self.huespedes = 0

        def anadir_huespedes(self, cantidad_huespedes):
            self.huespedes += cantidad_huespedes
        
        def checkout(self, cantidad_huespedes):
            self.huespedes -= cantidad_huespedes

        def ocupacion_total(self):
            return self.huespedes


    hotel = Hotel(numero_maximo_huespedes = 50, lugares_estacionamiento = 20)
    print(f'Lugares de estacionamiento Hotel 1: {hotel.lugares_estacionamiento}')
    hotel_2 = Hotel(50, 20)
    hotel_2.anadir_huespedes(3)
    hotel_2.checkout(1)
    print(f'Ocupacion del Hotel 2: {hotel_2.ocupacion_total()}')