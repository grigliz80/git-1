import pytest
from luna_weekly_cooking.models import DishIngredient, Ingredient

def test_dish_ingredient_creation():
    ingredient = Ingredient("Meat", 10, "per_100g")
    dish_ingredient = DishIngredient(ingredient, 200)

    assert dish_ingredient.ingredient == ingredient
    assert dish_ingredient.amount == 200

def test_dish_ingredient_cost_for_per_100g():
    ingredient = Ingredient("Meat", 10, "per_100g")
    dish_ingredient = DishIngredient(ingredient, 200)

    assert dish_ingredient.cost == 20

def test_dish_ingredient_cost_for_per_piece():
    ingredient = Ingredient("Egg", 6, "per_piece")
    dish_ingredient = DishIngredient(ingredient, 3)

    assert dish_ingredient.cost == 18

def test_dish_ingredient_cost_for_per_100ml():
    ingredient = Ingredient("Milk", 8, "per_100ml")
    dish_ingredient = DishIngredient(ingredient, 300)

    assert dish_ingredient.cost == 24