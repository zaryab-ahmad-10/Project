class Admin(User):
    def __init__(self, rental_system: CarRentalSystem, user_name: str, admin_id: int, admin_pass: str):
        super().__init__(rental_system, user_name)
        self.admin_id = admin_id
        self.admin_pass = admin_pass