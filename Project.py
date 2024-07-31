from enum import Enum
from datetime import datetime
from typing import List, Optional

class CarCategory(Enum):
    SEDAN = "Sedan"
    SUV = "SUV"
    HATCHBACK = "Hatchback"

class User:
    def __init__(self, user_name: str):
        self.user_name = user_name

class Admin(User):
    def __init__(self, user_name: str, admin_id: int, admin_pass: str):
        super().__init__(user_name)
        self.admin_id = admin_id
        self.admin_pass = admin_pass

class Car:
    def __init__(self, color: str, category: CarCategory, seats: int, license_plate: str, per_day_cost: float):
        self.color = color
        self.category = category
        self.seats = seats
        self.license_plate = license_plate
        self.per_day_cost = per_day_cost
        self.is_rented = False
        self.rent_start_date: Optional[datetime] = None
        self.rent_end_date: Optional[datetime] = None
        self.rented_by: Optional[User] = None

    def __str__(self):
        return (f"Car category = {self.category.value}, color = {self.color}, seats = {self.seats}, "
                f"License Plate = {self.license_plate}, "
                f"per_day_cost = {self.per_day_cost}, is_rented = {self.is_rented}, "
                f"rent_start_date = {self.rent_start_date}, rent_end_date = {self.rent_end_date}, "
                f"rented_by = {self.rented_by}")

class CarRentalSystem:
    def __init__(self):
        self.cars: List[Car] = []
        self.admins: List[Admin] = []
        self.list_cars()
        self.list_admins()

    def list_cars(self):
        self.cars = [
            Car(category=CarCategory.SEDAN, color="Urban Titanium", seats=4, license_plate="LEA 987", per_day_cost=50000.0),
            Car(category=CarCategory.SUV, color="Midnight Blue", seats=7, license_plate="LED 867", per_day_cost=80000.0),
            Car(category=CarCategory.HATCHBACK, color="Pearl White", seats=5, license_plate="ARQ 123", per_day_cost=35000.0),
            Car(category=CarCategory.SEDAN, color="Black Pearl", seats=4, license_plate="ATD 631", per_day_cost=30000.0),
            Car(category=CarCategory.HATCHBACK, color="Gun Metallic", seats=5, license_plate="LRQ 178", per_day_cost=35000.0),
            Car(category=CarCategory.SUV, color="Lunar Silver", seats=7, license_plate="ALF 123", per_day_cost=80000.0)
        ]

    def list_admins(self):
        self.admins = [
            Admin("Ahmad", 123, "adminpass"),
            Admin("Ali", 456, "passadmin"),
            Admin("Bilal", 789, "adminpass1")
        ]

    def add_car(self, car: Car):
        self.cars.append(car)

    def delete_car(self, license_plate: str):
        for car in self.cars:
            if car.license_plate == license_plate:
                self.cars.remove(car)
                break

    def view_all_cars(self):
        for car in self.cars:
            print(car)

    def cars_available(self, num_people: int, start_date: datetime, end_date: datetime):
        available = []
        for car in self.cars:
            if car.seats >= num_people and (not car.is_rented or car.rent_end_date < start_date):
                available.append(car)
        return available

    def book_car(self, car: Car, start_date: datetime, end_date: datetime, user: User):
        if car in self.cars and not car.is_rented:
            car.is_rented = True
            car.rent_start_date = start_date
            car.rent_end_date = end_date
            car.rented_by = user
            return True
        return False

    def authenticate_admin(self, user_name: str, admin_id: int, password: str) -> bool:
        for admin in self.admins:
            if admin.user_name == user_name and admin.admin_id == admin_id and admin.admin_pass == password:
                return True
        return False

# Output

if __name__ == "__main__":
    system = CarRentalSystem()
    
    user_type = int(input("Are you an Admin or a User? (1 for Admin / 2 For User): "))

    if user_type == 1:
        user_name = input("Please enter your name: ")
        admin_id = int(input("Enter Admin ID: "))
        password = input("Enter Admin Password: ")
        
        if system.authenticate_admin(user_name, admin_id, password):
            print(f"Admin authenticated successfully. Welcome Admin: {admin_id}")
            
            while True:
                action = input("Would you like to add or delete a car? (add/delete/view/exit): ")
                if action == "add":
                    category = CarCategory[input("Enter car category (SEDAN/SUV/HATCHBACK): ").upper()]
                    color = input("Enter car color: ")
                    license_plate = input("Please enter the license plate number (ABC 123): ")
                    seats = int(input("Enter number of seats: "))
                    per_day_cost = float(input("Enter per day cost: "))
                    car = Car(category=category, color=color, seats=seats, license_plate=license_plate, per_day_cost=per_day_cost)
                    system.add_car(car)
                    print("Car added successfully.")
                elif action == "delete":
                    license_plate = input("Enter license number of car to delete (ABC 123): ")
                    system.delete_car(license_plate)
                    print("Car deleted successfully.")
                elif action == "view":
                    system.view_all_cars()
                elif action == "exit":
                    break
                else:
                    print("Invalid action. Please try again.")
        else:
            print("Invalid Admin Name, Admin ID or Password.")
    
    elif user_type == 2:
        user_name = input("Enter your name: ")
        user = User(user_name)
        print(f"Welcome, {user_name}!")
        
        while True:
            action = input("Would you like to view all cars or book a car? (view/book/exit): ")
            if action == "view":
                print("All cars in the system:")
                system.view_all_cars()
            elif action == "book":
                num_people = int(input("Enter number of people: "))
                start_date = datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d")
                end_date = datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d")
                available_cars = system.cars_available(num_people, start_date, end_date)
                if available_cars:
                    print("Available cars:")
                    for car in available_cars:
                        print(car)
                    license_plate = input("Enter the license plate number of the car you want to book: ")
                    car_to_book = next((car for car in available_cars if car.license_plate == license_plate), None)
                    if car_to_book and system.book_car(car_to_book, start_date, end_date, user):
                        print("Car booked successfully.")
                    else:
                        print("Failed to book the car.")
                else:
                    print("No cars available for the specified criteria.")
            elif action == "exit":
                break
            else:
                print("Invalid action. Please try again.")
    else:
        print("Invalid user type. Please enter either '1' for Admin or '2' for User.")