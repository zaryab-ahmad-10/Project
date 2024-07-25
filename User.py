class User:
    def __init__(self, rental_system: CarRentalSystem):
        self.rental_system = rental_system

    def view_all_cars(self):
        self.rental_system.view_all_cars()

    def book_car(self, num_people: int, start_date: datetime, end_date: datetime):
        available = self.rental_system.cars_available(num_people, start_date, end_date)
        if available:
            car = available[0]
            self.rental_system.book_car(car, start_date, end_date)
            print(f"Car booked: {car}")
        else:
            print("No cars available.")