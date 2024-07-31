class User:
    def __init__(self, rental_system: CarRentalSystem, user_name: str):
        self.rental_system = rental_system
        self.user_name = user_name

    def view_all_cars(self):
        self.rental_system.view_all_cars()

    def book_car(self, num_people: int, start_date: datetime, end_date: datetime):
        available = self.rental_system.cars_available(num_people, start_date, end_date)
        if available:
            car = available[0]
            self.rental_system.book_car(car, start_date, end_date, self.user_name)
            print(f"Car booked: {car}")
        else:
            print("No cars available.")