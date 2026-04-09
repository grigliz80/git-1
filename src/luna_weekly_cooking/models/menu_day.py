class MenuDay:
    def __init__(self, day_name: str):
        self.day_name = day_name
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def remove_dish(self, dish):
        self.dishes.remove(dish)

    def get_dishes_by_category(self, category):
        return [dish for dish in self.dishes if dish.category == category]