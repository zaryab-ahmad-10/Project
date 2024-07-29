class Car:
    def __init__(self, color: str, category: CarCategory, seats: int, per_day_cost: float):
        self.color = color
        self.category = category
        self.seats = seats
        self.per_day_cost = per_day_cost
        self.is_rented = False
        self.rent_start_date: Optional[datetime] = None
        self.rent_end_date: Optional[datetime] = None

    def __str__(self):
        return (f"Car(category= {self.category}, color= {self.color}, seats= {self.seats}, "
                f"per_day_cost= {self.per_day_cost}, is_rented= {self.is_rented}, "
                f"rent_start_date= {self.rent_start_date}, rent_end_date= {self.rent_end_date})")
