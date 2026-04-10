class Dish:
    def __init__(self, name: str, category: str):
        allowed_categories = {"first", "second"}
        if category not in allowed_categories:
            raise ValueError("Not Existing Category!")
        
        self.name = name
        self.category = category
        self.ingredients = []

    def add_ingredient(self, dish_ingredient):
        self.ingredients.append(dish_ingredient)