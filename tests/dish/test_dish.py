import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction


# Req 2
# def test_dish():


# Test initialization
def test_dish():
    dish = Dish("Pão de Queijo", 3.0)
    dish2 = Dish("Pão de Queijo", 3.0)
    dish3 = Dish("Pão de Batata", 3.5)

    # Test initialization
    assert dish.name == "Pão de Queijo"
    assert dish.price == 3.0

    assert dish.price == 3.0
    assert dish3.price == 3.5

    with pytest.raises(TypeError):
        Dish("Pão de Queijo", "ten")

    with pytest.raises(ValueError):
        Dish("Pão de Queijo", -10)

    # Test magic methods
    assert repr(dish) == "Dish('Pão de Queijo', R$3.00)"
    assert repr(dish2) == "Dish('Pão de Queijo', R$3.00)"
    assert repr(dish3) == "Dish('Pão de Batata', R$3.50)"

    assert dish == dish2
    assert dish != dish3

    assert hash(dish) == hash("Dish('Pão de Queijo', R$3.00)")
    assert hash(dish3) == hash("Dish('Pão de Batata', R$3.50)")

    # Test methods
    ingredient = Ingredient("farinha")
    ingredient2 = Ingredient("bacon")
    ingredient3 = Ingredient("ovo")

    dish.add_ingredient_dependency(ingredient, 1)
    dish.add_ingredient_dependency(ingredient2, 3)
    dish.add_ingredient_dependency(ingredient3, 1)

    assert dish.recipe == {ingredient: 1, ingredient2: 3, ingredient3: 1}

    restrictions = dish.get_restrictions()

    assert restrictions == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.GLUTEN,
    }

    all_ingredients = dish.get_ingredients()

    assert all_ingredients == {ingredient, ingredient2, ingredient3}
