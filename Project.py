from enum import Enum
from datetime import datetime
from typing import List, Optional

class CarCategory(Enum):
    SEDAN = "Sedan"
    SUV = "SUV"
    HATCHBACK = "Hatchback"

class Car:
    def __init__(self, color: str, category: CarCategory, seats: int, license_plate: str ,per_day_cost: float):
        self.color = color
        self.category = category
        self.seats = seats
        self.license_plate = license_plate
        self.per_day_cost = per_day_cost
        self.is_rented = False
        self.rent_start_date: Optional[datetime] = None
        self.rent_end_date: Optional[datetime] = None
        self.rented_by: Optional[str] = None
        self.renter_id: Optional[str] = None

    def __str__(self):
        return (f"Car category= {self.category.value}, color= {self.color}, seats= {self.seats}, "
                f"License Plate = {self.license_plate},"
                f"per_day_cost= {self.per_day_cost}, is_rented= {self.is_rented}, "
                f"rent_start_date= {self.rent_start_date}, rent_end_date= {self.rent_end_date}, "
                f"rented_by= {self.rented_by}, renter_id= {self.renter_id}")

class CarRentalSystem:
    def __init__(self):
        self.cars: List[Car] = [
             Car(category=CarCategory.SEDAN, color="Urban Titanium", seats=4,license_plate="LEA 987", per_day_cost=50000.0),
                Car(category=CarCategory.SUV, color="Midnight Blue", seats=7,license_plate="LED 867", per_day_cost=80000.0),
                Car(category=CarCategory.HATCHBACK, color="Pearl White", seats=5,license_plate="ARQ 123", per_day_cost=35000.0),
                Car(category=CarCategory.SEDAN, color="Black Pearl", seats=4,license_plate="ATD 631" ,per_day_cost=30000.0),
                Car(category=CarCategory.HATCHBACK, color="Gun Metallic", seats=5,license_plate="LRQ 178", per_day_cost=35000.0),
                Car(category=CarCategory.SUV, color="Lunar Silver", seats=7,license_plate="ALF 123", per_day_cost=80000.0)
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

    def book_car(self, car: Car, start_date: datetime, end_date: datetime, user_name: str, user_id: str):
        if car in self.cars and not car.is_rented:
            car.is_rented = True
            car.rent_start_date = start_date
            car.rent_end_date = end_date
            car.rented_by = user_name
            car.renter_id = user_id
            return True
        return False

class Admin:
    def __init__(self, rental_system: CarRentalSystem):
        self.rental_system = rental_system

    def add_car(self, car: Car):
        self.rental_system.add_car(car)

    def delete_car(self, car: Car):
        self.rental_system.delete_car(car)

class User:
    def __init__(self, rental_system: CarRentalSystem, user_name: str, user_id: str):
        self.rental_system = rental_system
        self.user_name = user_name
        self.user_id = user_id

    def view_all_cars(self):
        self.rental_system.view_all_cars()

    def book_car(self, num_people: int, start_date: datetime, end_date: datetime):
        available = self.rental_system.cars_available(num_people, start_date, end_date)
        if available:
            car = available[0]
            self.rental_system.book_car(car, start_date, end_date, self.user_name, self.user_id)
            print(f"Car booked: {car}")
        else:
            print("No cars available.")

def authenticate_admin(admin_id: str, password: str) -> bool:
    # Example credentials
    stored_admin_id = "admin123"
    stored_password = "adminpass"
    return admin_id == stored_admin_id and password == stored_password

# Output

if __name__ == "__main__":
    system = CarRentalSystem()
    
    user_type = input("Are you an Admin or a User? (Admin/User): ")

    if user_type == "Admin":
        admin_id = input("Enter Admin ID: ")
        password = input("Enter Admin Password: ")
        
        if authenticate_admin(admin_id, password):
            admin = Admin(system)
            print("Admin authenticated successfully.")
            
            while True:
                action = input("Would you like to add or delete a car? (add/delete/exit): ")
                if action == "add":
                    category = CarCategory[input("Enter car category (SEDAN/SUV/HATCHBACK): ").upper()]
                    color = input("Enter car color: ")
                    license_plate = input("Please enter the license plate number (ABC 123): ")
                    seats = int(input("Enter number of seats: "))
                    per_day_cost = float(input("Enter per day cost: "))
                    car = Car(category=category, color=color, seats=seats, per_day_cost=per_day_cost)
                    admin.add_car(car)
                    print("Car added successfully.")
                elif action == "delete":
                    license_plate = input("Enter license number of car to delete (ABC 123): ")
                    for car in system.cars:
                        if car.license_plate == license_plate:
                            admin.delete_car(car)
                            print("Car deleted successfully.")
                            break
                    else:
                        print("Car not found.")
                elif action == "exit":
                    break
                else:
                    print("Invalid action. Please try again.")
        else:
            print("Invalid Admin ID or Password.")
    
    elif user_type == "User":
        user_name = input("Enter your name: ")
        user_id = input("Enter your User ID: ")
        user = User(system, user_name, user_id)
        print(f"Welcome, {user_name}!")
        
        while True:
            action = input("Would you like to view all cars or book a car? (view/book/exit): ")
            if action == "view":
                print("All cars in the system:")
                user.view_all_cars()
            elif action == "book":
                num_people = int(input("Enter number of people: "))
                start_date = datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d")
                end_date = datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d")
                user.book_car(num_people, start_date, end_date)
            elif action == "exit":
                break
            else:
                print("Invalid action. Please try again.")
    else:
        print("Invalid user type. Please enter either 'Admin' or 'User'.")