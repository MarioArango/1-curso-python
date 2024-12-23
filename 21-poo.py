from datetime import datetime
from dataclasses import dataclass, asdict

#consecionaria

@dataclass
class Vehicle:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

@dataclass
class Client:
    def __init__(self, dni, name):
        self.dni = dni
        self.name = name
        self.pucharsed_vehicles = []

@dataclass
class Concessionary:
    def __init__(self, social_reason):
        self.social_reason = social_reason
        self.vehicles = []
        self.clients = []

    def add_vehicle(self, new_vehicle, quantity):
        if isinstance(quantity, int) and quantity > 0:
            exist_vehicle = any(vehicle['model'] == new_vehicle['model'] and vehicle['brand'] == new_vehicle['brand'] for vehicle in self.vehicles)
            if exist_vehicle:
                self.vehicles = [
                    {
                        **vehicle,
                        'quantity': vehicle['quantity'] + quantity
                    }
                    if vehicle['model'] == new_vehicle['model'] and vehicle['brand'] == new_vehicle['brand'] else vehicle
                    for vehicle in self.vehicles
                ]
            else:
                self.vehicles.append({**new_vehicle, 'quantity': quantity})
        else: 
            print('Ingrese una cantidad valida')
    
    def sale_vehicles(self, vehicle_saled, client_to_sale, quantity):
        is_registered = self.register_client(client_to_sale)
        if is_registered:
            #any cuando encuentra el primer True, se detiene, por eso es recomendable retornar un bool
            exist_vehicle = any(
                vehicle['model'] == vehicle_saled['model'] and vehicle['brand'] == vehicle_saled['brand']
                for vehicle in self.vehicles
            )

            if exist_vehicle:
                if isinstance(quantity, int) and quantity > 0:
                    exist_stock = any(
                        vehicle['quantity'] >= quantity and vehicle['model'] == vehicle_saled['model'] and vehicle['brand'] == vehicle_saled['brand']
                        for vehicle in self.vehicles
                    )

                    if exist_stock:
                        #actualiza el stock de vehiculos
                        self.vehicles = [
                            {
                                **vehicle,
                                'quantity': vehicle['quantity'] - quantity
                            }
                            if vehicle['model'] == vehicle_saled['model'] and vehicle['brand'] == vehicle_saled['brand']
                            else vehicle
                            for vehicle in self.vehicles
                        ]
                        #registra los vehiculo vendidos a clientes
                        self.clients = [
                            {
                                **client,
                                'vehicles': [
                                    *client['vehicles'],
                                    {
                                        **vehicle_saled,
                                        'date_sale': datetime.now().strftime('%Y-%m-%d')
                                    }
                                ]
                            }
                            if client['dni'] == client_to_sale['dni'] else client
                            for client in self.clients
                        ]
                    else:
                        print('No hay stock disponible')
                else:
                    print('Debe ingresar una cantidad valida')
            else: 
                print('El vehiculo solicitado no existe')
        else:
            print('Error al registrar un cliente')
            
    def register_client(self, client_registered):
        try: 
            #validar inicializacion de vehiculos en clientes
            if 'vehicles' not in client_registered:
                client_registered = {
                    **client_registered,
                    'vehicles': []
                }

            exist_client = any(
                client['dni'] == client_registered['dni']
                for client in self.clients
            )
            if exist_client:
                self.clients = [
                    {
                        **client,
                        **client_registered
                    }
                    if client['dni'] == client_registered['dni'] else client
                    for client in self.clients
                ]
            else: 
                self.clients.append(client_registered)

            return True
        except:
            return False

    def summary(self):
        vehicles = ''
        for vehicle in self.vehicles:
            vehicles += '- ' + vehicle + '\n' 

        clients = ''
        for client in self.clients:
            clients += '- ' + client + '\n' 

        print(f'''
    Vehiculos registrados: {vehicles}
    Clientes registrados: {clients}
''')        


corolla = Vehicle('Corolla', 'Toyota')
mazda3 = Vehicle('Mazda 3', 'Mazda')

mario = Client('72935585', 'Mario')
diego = Client('72753669', 'Diego')

concesionaria = Concessionary('Maquinarias')

concesionaria.add_vehicle(asdict(corolla), 2)
concesionaria.add_vehicle(asdict(mazda3), 3)
concesionaria.summary()

concesionaria.register_client(asdict(mario))
concesionaria.register_client(asdict(diego))
concesionaria.summary()

concesionaria.sale_vehicles(asdict(mazda3), asdict(mario), 1)
concesionaria.sale_vehicles(asdict(corolla), asdict(diego), 1)
concesionaria.summary()
