from luna_weekly_cooking.models import MenuDay

def test_menu_day_creation():
    day = MenuDay("Monday")

    assert day.day_name == "Monday"
    assert day.dishes == []