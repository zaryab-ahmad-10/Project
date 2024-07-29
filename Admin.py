class Admin:
    def add_car(self, car: Car):
        rental_system.add_car(car)

    def delete_car(self, car: Car):
        rental_system.delete_car(car)
