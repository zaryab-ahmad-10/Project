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