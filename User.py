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