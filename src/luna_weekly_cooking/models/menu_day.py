class MenuDay:
    def __init__(self, day_name: str):
        self.day_name = day_name
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def remove_dish(self, dish):
        self.dishes.remove(dish)