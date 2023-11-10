import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    dishes: set[Dish]

    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        with open(source_path, "r") as sheet:
            reader = csv.DictReader(sheet)
            for row in reader:
                # print(row["recipe_amount"])
                name = row["dish"]
                price = float(row["price"])
                dish = Dish(name, price)
                ingredient = Ingredient(row["ingredient"])
                if dish not in self.dishes:
                    dish.add_ingredient_dependency(
                        ingredient, row["recipe_amount"]
                    )
                    self.dishes.add(dish)
                else:
                    for dish in self.dishes:
                        if dish.name == name:
                            dish.add_ingredient_dependency(
                                ingredient, row["recipe_amount"]
                            )
                # dish.add_ingredient_dependency(
                #     ingredient, row["recipe_amount"]
                # )
                # print(dish.get_ingredients())
                # self.dishes.add(dish)


test = MenuData("data/menu_base_data.csv")
print(test.dishes)
