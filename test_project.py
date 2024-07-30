import unittest
from datetime import datetime
from Project import Car, CarCategory, CarRentalSystem, Admin, User

class TestCarRentalSystem(unittest.TestCase):

    def setUp(self):
        self.system = CarRentalSystem()

    def test_add_car(self):
        car = Car(category=CarCategory.SEDAN, color="Blue", seats=4, license_plate="XYZ 123", per_day_cost=100.0)
        self.system.add_car(car)
        self.assertIn(car, self.system.cars)

    def test_delete_car(self):
        car = Car(category=CarCategory.SEDAN, color="Blue", seats=4, license_plate="XYZ 123", per_day_cost=100.0)
        self.system.add_car(car)
        self.system.delete_car(car)
        self.assertNotIn(car, self.system.cars)

    def test_view_all_cars(self):
        car1 = Car(category=CarCategory.SEDAN, color="Blue", seats=4, license_plate="XYZ 123", per_day_cost=100.0)
        car2 = Car(category=CarCategory.SUV, color="Red", seats=7, license_plate="ABC 456", per_day_cost=150.0)
        self.system.add_car(car1)
        self.system.add_car(car2)
        all_cars = self.system.view_all_cars()
        self.assertIn(car1, all_cars)
        self.assertIn(car2, all_cars)

    def test_cars_available(self):
        start_date = datetime.strptime("2023-08-01", "%Y-%m-%d")
        end_date = datetime.strptime("2023-08-10", "%Y-%m-%d")
        car = Car(category=CarCategory.SEDAN, color="Blue", seats=4, license_plate="XYZ 123", per_day_cost=100.0)
        self.system.add_car(car)
        available_cars = self.system.cars_available(4, start_date, end_date)
        self.assertIn(car, available_cars)

    def test_book_car(self):
        start_date = datetime.strptime("2023-08-01", "%Y-%m-%d")
        end_date = datetime.strptime("2023-08-10", "%Y-%m-%d")
        car = Car(category=CarCategory.SEDAN, color="Blue", seats=4, license_plate="XYZ 123", per_day_cost=100.0)
        self.system.add_car(car)
        user_name = "Test User"
        user_id = "user123"
        success = self.system.book_car(car, start_date, end_date, user_name, user_id)
        self.assertTrue(success)
        self.assertTrue(car.is_rented)
        self.assertEqual(car.rent_start_date, start_date)
        self.assertEqual(car.rent_end_date, end_date)
        self.assertEqual(car.rented_by, user_name)
        self.assertEqual(car.renter_id, user_id)

class TestAuthentication(unittest.TestCase):

    def test_authenticate_admin_success(self):
        self.assertTrue(authenticate_admin("admin123", "adminpass"))

    def test_authenticate_admin_failure(self):
        self.assertFalse(authenticate_admin("wrongid", "wrongpass"))