import unittest
from datetime import datetime
from Project import Car, CarCategory, CarRentalSystem 

class TestCarRentalSystem(unittest.TestCase):

    def setUp(self):
        self.system = CarRentalSystem()

    def test_add_car(self):
        new_car = Car(category=CarCategory.SEDAN, color="Red", seats=4, license_plate="XYZ 123", per_day_cost=25000.0)
        self.system.add_car(new_car)
        self.assertIn(new_car, self.system.cars)

    def test_delete_car(self):
        car_to_delete = self.system.cars[0]
        self.system.delete_car(car_to_delete)
        self.assertNotIn(car_to_delete, self.system.cars)

    def test_view_all_cars(self):
        with self.assertLogs() as log:
            self.system.view_all_cars()
            self.assertEqual(len(log.output), len(self.system.cars))

    def test_cars_available(self):
        num_people = 4
        start_date = datetime(2024, 8, 1)
        end_date = datetime(2024, 8, 10)
        available_cars = self.system.cars_available(num_people, start_date, end_date)
        for car in available_cars:
            self.assertGreaterEqual(car.seats, num_people)
            self.assertFalse(car.is_rented or car.rent_end_date >= start_date)

    def test_book_car(self):
        car_to_book = self.system.cars[0]
        start_date = datetime(2024, 8, 1)
        end_date = datetime(2024, 8, 10)
        user_name = "TestUser"
        booking_success = self.system.book_car(car_to_book, start_date, end_date, user_name)
        self.assertTrue(booking_success)
        self.assertTrue(car_to_book.is_rented)
        self.assertEqual(car_to_book.rent_start_date, start_date)
        self.assertEqual(car_to_book.rent_end_date, end_date)
        self.assertEqual(car_to_book.rented_by, user_name)

    def test_authenticate_admin(self):
        valid_admin_id = 123
        valid_password = "adminpass"
        invalid_admin_id = 999
        invalid_password = "wrongpass"
        self.assertTrue(self.system.authenticate_admin(valid_admin_id, valid_password))
        self.assertFalse(self.system.authenticate_admin(valid_admin_id, invalid_password))
        self.assertFalse(self.system.authenticate_admin(invalid_admin_id, valid_password))