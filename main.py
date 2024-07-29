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