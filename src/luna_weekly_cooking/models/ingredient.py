class Ingredient:
    def __init__(self, name: str, price_per_unit: int, unit: str):
        allowed_units = {"per_piece", "per_100g", "per_100ml"}
        if unit not in allowed_units:
            raise ValueError(f"Invalid unit! {unit}")
        self.name = name
        self.price_per_unit = price_per_unit
        self.unit = unit
