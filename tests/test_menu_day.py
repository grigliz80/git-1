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

def test_get_dishes_by_category():
    day = MenuDay("Monday")

    dish1 = Dish("Borsch", "first")
    dish2 = Dish("Steak", "second")

    day.add_dish(dish1)
    day.add_dish(dish2)

    first_dishes = day.get_dishes_by_category("first")

    assert len(first_dishes) == 1
    assert first_dishes[0] == dish1