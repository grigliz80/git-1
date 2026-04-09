import pytest
from luna_weekly_cooking.models import MenuDay, Dish

def test_menu_day_creation():
    day = MenuDay("Monday")

    assert day.day_name == "Monday"
    assert day.dishes == []

def test_add_dish():
    day = MenuDay("Monday")
    dish = Dish("Borsch", "first")

    day.add_dish(dish)

    assert len(day.dishes) == 1
    assert day.dishes[0] == dish

def test_remove_dish():
    day = MenuDay("Monday")
    dish = Dish("Borsch", "first")

    day.add_dish(dish)
    day.remove_dish(dish)

    assert day.dishes == []

def test_remove_non_existing_dish():
    day = MenuDay("Monday")
    dish = Dish("Borsch", "first")

    with pytest.raises(ValueError):
        day.remove_dish(dish)