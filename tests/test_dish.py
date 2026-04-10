import pytest
from luna_weekly_cooking.models import Dish, DishIngredient, Ingredient

def test_dish_creation():
    dish = Dish("Borsch", "first")

    assert dish.name == "Borsch"
    assert dish.category == "first"

def test_invalid_dish_category():
    with pytest.raises(ValueError):
        Dish("Borsch", "invalid_category")

def test_dish_has_ingredients():
    dish = Dish("Borsch", "first")

    assert dish.ingredients == []

def test_add_ingredient_to_dish():
    dish = Dish("Borsch", "first")
    ingredient = Ingredient("Meat", 10, "per_100g")
    dish_ingredient = DishIngredient(ingredient, 200)

    dish.add_ingredient(dish_ingredient)
    
    assert len(dish.ingredients) == 1
    assert dish.ingredients[0] == dish_ingredient
