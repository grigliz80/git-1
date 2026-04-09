import pytest
from luna_weekly_cooking.models import Ingredient

def test_ingredient_creation():
    ingredient = Ingredient("Egg", 6, "per_piece")

    assert ingredient.name == "Egg"
    assert ingredient.price_per_unit == 6
    assert ingredient.unit == "per_piece"

def test_invalid_ingredient_unit():
    with pytest.raises(ValueError):
        Ingredient("Milk", 10, "invalid_unit")
