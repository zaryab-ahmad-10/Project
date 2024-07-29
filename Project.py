from enum import Enum
from datetime import datetime
from typing import List, Optional

class CarCategory(Enum):
    SEDAN = "Sedan"
    SUV = "SUV"
    HATCHBACK = "Hatchback"

class Car:
    def __init__(self, color: str, category: CarCategory, seats: int, per_day_cost: float):
        self.color = color
        self.category = category
        self.seats = seats
        self.per_day_cost = per_day_cost
        self.is_rented = False
        self.rent_start_date: Optional[datetime] = None
        self.rent_end_date: Optional[datetime] = None

    def __str__(self):
        return (f"Car(category= {self.category}, color= {self.color}, seats= {self.seats}, "
                f"per_day_cost= {self.per_day_cost}, is_rented= {self.is_rented}, "
                f"rent_start_date= {self.rent_start_date}, rent_end_date= {self.rent_end_date})")

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

class Admin:
    def add_car(self, car: Car):
        rental_system.add_car(car)

    def delete_car(self, car: Car):
        rental_system.delete_car(car)

class User:
    def view_all_cars(self):
        rental_system.view_all_cars()

    def book_car(self, num_people: int, start_date: datetime, end_date: datetime):
        available = rental_system.cars_available(num_people, start_date, end_date)
        if available:
            car = available[0]
            rental_system.book_car(car, start_date, end_date)
            print(f"Car booked: {car}")
        else:
            print("No cars available.")

# Initializing the CarREntalSystem class to rental rental_system as an instance.
rental_system = CarRentalSystem()


if __name__ == "__main__":
    admin = Admin()
    user = User()

    # Admin adds cars
    car1 = Car(category=CarCategory.SEDAN, color="Urban Titanium", seats=4, per_day_cost=50000.0)
    car2 = Car(category=CarCategory.SUV, color="Midnight Blue", seats=7, per_day_cost=80000.0)
    car3 = Car(category=CarCategory.HATCHBACK, color="Pearl White", seats=5, per_day_cost=35000.0)
    car4 = Car(category=CarCategory.SEDAN, color="Black Pearl", seats=4, per_day_cost=30000.0)
    car5 = Car(category=CarCategory.HATCHBACK, color="Gun Metallic", seats=5, per_day_cost=35000.0)
    car6 = Car(category=CarCategory.SUV, color="Lunar Silver", seats=7, per_day_cost=80000.0)
    admin.add_car(car1)
    admin.add_car(car2)
    admin.add_car(car3)
    admin.add_car(car4)
    admin.add_car(car5)
    admin.add_car(car6)

    # User views all cars
    print("All cars in the system:")
    user.view_all_cars()

    # User books a car
    print("\nBooking a car:")
    user.book_car(num_people=7, start_date=datetime(2024, 8, 1), end_date=datetime(2024, 8, 5))