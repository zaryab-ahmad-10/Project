if __name__ == "__main__":
    system = CarRentalSystem()
    
    user_type = int(input("Are you an Admin or a User? (1 for Admin / 2 For User): "))

    if user_type == 1:
        admin_id = int(input("Enter Admin ID: "))
        password = input("Enter Admin Password: ")
        
        if system.authenticate_admin(admin_id, password):
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
                    for car in system.cars:
                        if car.license_plate == license_plate:
                            system.delete_car(car)
                            print("Car deleted successfully.")
                            break
                    else:
                        print("Car not found.")

                elif action == "view":
                    system.view_all_cars()
                elif action == "exit":
                    break
                else:
                    print("Invalid action. Please try again.")
        else:
            print("Invalid Admin ID or Password.")
    
    elif user_type == 2:
        user_name = input("Enter your name: ")
        user = User(system, user_name)
        print(f"Welcome, {user_name}!")
        
        while True:
            action = input("Would you like to view all cars or book a car? (view/book/exit): ")
            if action == "view":
                print("All cars in the system:")
                user.view_all_cars()
            elif action == "book":
                num_people = int(input("Enter number of people: "))
                start_date = datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d")
                end_date = datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d")
                user.book_car(num_people, start_date, end_date)
            elif action == "exit":
                break
            else:
                print("Invalid action. Please try again.")
    else:
        print("Invalid user type. Please enter either 'Admin' or 'User'.")
