from luna_weekly_cooking.models import Dish

def test_dish_creation():
    dish = Dish("Borch", "first")

    assert dish.name == "Borch"
    assert dish.category == "first"

