class DishIngredient:
    def __init__(self, ingredient, amount):
        self.ingredient = ingredient
        self.amount = amount
    
    @property
    def cost(self):
        if self.ingredient.unit == "per_100g":
            return (self.amount / 100) * self.ingredient.price_per_unit