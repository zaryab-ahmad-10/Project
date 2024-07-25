class Admin:
    def __init__(self, rental_system: CarRentalSystem):
        self.rental_system = rental_system

    def add_car(self, car: Car):
        self.rental_system.add_car(car)

    def delete_car(self, car: Car):
        self.rental_system.delete_car(car)
