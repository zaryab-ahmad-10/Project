import unittest
from datetime import datetime
from Project import CarCategory, User, Admin, Car, CarRentalSystem

class TestCarRentalSystem(unittest.TestCase):

    def setUp(self):
        self.system = CarRentalSystem()
        self.test_user = User("Khan")
        self.test_admin = Admin("Ahmad", 123, "adminpass")
        self.system.admins.append(self.test_admin) 

    def test_add_car(self):
        car = Car(color="Red", category=CarCategory.SEDAN, seats=4, license_plate="RED 123", per_day_cost=40000.0)
        self.system.add_car(car)
        self.assertIn(car, self.system.cars)

    def test_delete_car(self):
        car = Car(color="Blue", category=CarCategory.SUV, seats=7, license_plate="LEA 849", per_day_cost=70000.0)
        self.system.add_car(car)
        self.system.delete_car("LEA 849")
        self.assertNotIn(car, self.system.cars)

    def test_book_car(self):
        car = Car(color="Green", category=CarCategory.HATCHBACK, seats=5, license_plate="LED 567", per_day_cost=35000.0)
        self.system.add_car(car)
        start_date = datetime(2024, 7, 1)
        end_date = datetime(2024, 7, 5)
        success = self.system.book_car(car, start_date, end_date, self.test_user)
        self.assertTrue(success)
        self.assertTrue(car.is_rented)
        self.assertEqual(car.rented_by, self.test_user)
        self.assertEqual(car.rent_start_date, start_date)
        self.assertEqual(car.rent_end_date, end_date)

    def test_authenticate_admin(self):
        self.assertTrue(self.system.authenticate_admin("Ahmad", 123, "adminpass"))
        self.assertFalse(self.system.authenticate_admin("Ahmad", 123, "abcdefgh"))
        self.assertFalse(self.system.authenticate_admin("Hamza", 123, "adminpass"))

    def test_cars_available(self):
        car1 = Car(color="Silver", category=CarCategory.SUV, seats=7, license_plate="AEX 443", per_day_cost=75000.0)
        car2 = Car(color="Black", category=CarCategory.SEDAN, seats=4, license_plate="LZZ 124", per_day_cost=40000.0)
        self.system.add_car(car1)
        self.system.add_car(car2)
        start_date = datetime(2024, 7, 1)
        end_date = datetime(2024, 7, 5)
        available_cars = self.system.cars_available(4, start_date, end_date)
        self.assertIn(car1, available_cars)
        self.assertIn(car2, available_cars)

    def test_view_all_cars(self):
        car = Car(color="White", category=CarCategory.HATCHBACK, seats=5, license_plate="LKQ 333", per_day_cost=35000.0)
        self.system.add_car(car)
        with self.assertLogs(level='INFO') as log:
            self.system.view_all_cars()
            self.assertIn(f"Car category = {car.category.value}, color = {car.color}, seats = {car.seats}, "
                          f"License Plate = {car.license_plate}, per_day_cost = {car.per_day_cost}, "
                          f"is_rented = {car.is_rented}, rent_start_date = {car.rent_start_date}, "
                          f"rent_end_date = {car.rent_end_date}, rented_by = {car.rented_by}", log.output[0])