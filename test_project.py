import unittest
from datetime import datetime
from Project import Car, CarCategory, CarRentalSystem, Admin, User

class TestCarRentalSystem(unittest.TestCase):
    def setUp(self):
        global rental_system
        rental_system = CarRentalSystem()
        self.admin = Admin()
        self.user = User()

        # Add some cars for testing
        self.car1 = Car(category=CarCategory.SEDAN, color="Urban Titanium", seats=4, per_day_cost=50000.0)
        self.car2 = Car(category=CarCategory.SUV, color="Midnight Blue", seats=7, per_day_cost=80000.0)
        self.car3 = Car(category=CarCategory.HATCHBACK, color="Pearl White", seats=5, per_day_cost=35000.0)
        self.admin.add_car(self.car1)
        self.admin.add_car(self.car2)
        self.admin.add_car(self.car3)

    def test_add_car(self):
        self.assertIn(self.car1, rental_system.cars)
        self.assertIn(self.car2, rental_system.cars)
        self.assertIn(self.car3, rental_system.cars)

    def test_delete_car(self):
        self.admin.delete_car(self.car1)
        self.assertNotIn(self.car1, rental_system.cars)

    def test_view_all_cars(self):
        rental_system.view_all_cars()  # We should see all cars printed out

    def test_cars_available(self):
        start_date = datetime(2024, 8, 1)
        end_date = datetime(2024, 8, 5)
        available_cars = rental_system.cars_available(num_people=5, start_date=start_date, end_date=end_date)
        self.assertIn(self.car2, available_cars)
        self.assertIn(self.car3, available_cars)
        self.assertNotIn(self.car1, available_cars)

    def test_book_car(self):
        start_date = datetime(2024, 8, 1)
        end_date = datetime(2024, 8, 5)
        self.user.book_car(num_people=5, start_date=start_date, end_date=end_date)
        self.assertTrue(self.car3.is_rented)
        self.assertEqual(self.car3.rent_start_date, start_date)
        self.assertEqual(self.car3.rent_end_date, end_date)