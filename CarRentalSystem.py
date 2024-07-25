class CarRentalSystem:
    def __init__(self):
        self.cars: List[Car] = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def delete_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)

    def view_all_cars(self):
        for car in self.cars:
            print(car)

    def cars_available(self, num_people: int, start_date: datetime, end_date: datetime):
        available = []
        for car in self.cars:
            if car.seats >= num_people and (not car.is_rented or car.rent_end_date < start_date):
                available.append(car)
        return available

    def book_car(self, car: Car, start_date: datetime, end_date: datetime):
        if car in self.cars and not car.is_rented:
            car.is_rented = True
            car.rent_start_date = start_date
            car.rent_end_date = end_date
            return True
        return False