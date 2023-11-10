import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    dishes: set[Dish]

    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, "r") as sheet:
            read_csv = csv.DictReader(sheet)

            for row in read_csv:
                name = row["dish"]
                price = float(row["price"])
                dish = Dish(name, price)
                ingredient = Ingredient(row["ingredient"])
                amount = int(row["recipe_amount"])

                if dish not in self.dishes:
                    dish.add_ingredient_dependency(ingredient, amount)
                    self.dishes.add(dish)
                else:
                    for dish in self.dishes:
                        if dish.name == name:
                            dish.add_ingredient_dependency(ingredient, amount)
