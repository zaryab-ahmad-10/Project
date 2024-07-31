class CarRentalSystem:
    def __init__(self):
        self.cars: List[Car] = [
             Car(category=CarCategory.SEDAN, color="Urban Titanium", seats=4, license_plate="LEA 987", per_day_cost=50000.0),
             Car(category=CarCategory.SUV, color="Midnight Blue", seats=7, license_plate="LED 867", per_day_cost=80000.0),
             Car(category=CarCategory.HATCHBACK, color="Pearl White", seats=5, license_plate="ARQ 123", per_day_cost=35000.0),
             Car(category=CarCategory.SEDAN, color="Black Pearl", seats=4, license_plate="ATD 631", per_day_cost=30000.0),
             Car(category=CarCategory.HATCHBACK, color="Gun Metallic", seats=5, license_plate="LRQ 178", per_day_cost=35000.0),
             Car(category=CarCategory.SUV, color="Lunar Silver", seats=7, license_plate="ALF 123", per_day_cost=80000.0)
        ]
        self.admins = [
            {"admin_id": 123, "password": "adminpass"},
            {"admin_id": 456, "password": "password123"},
            {"admin_id": 789, "password": "securepassword"}
        ]

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

    def book_car(self, car: Car, start_date: datetime, end_date: datetime, user_name: str):
        if car in self.cars and not car.is_rented:
            car.is_rented = True
            car.rent_start_date = start_date
            car.rent_end_date = end_date
            car.rented_by = user_name
            return True
        return False

    def authenticate_admin(self, admin_id: int, password: str) -> bool:
        for admin in self.admins:
            if admin["admin_id"] == admin_id and admin["password"] == password:
                return True
        return False