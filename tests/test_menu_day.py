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