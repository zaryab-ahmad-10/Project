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