from src.models.ingredient import Ingredient, Restriction


# Req 1
def test_ingredient():
    ingredient = Ingredient("ovo")
    ingredient2 = Ingredient("ovo")
    ingredient3 = Ingredient("salmão")

    assert ingredient.name == "ovo"
    assert ingredient.restrictions == {Restriction.ANIMAL_DERIVED}

    assert ingredient == ingredient2
    assert ingredient != ingredient3

    assert hash(ingredient) == hash(ingredient2)
    assert hash(ingredient) != hash(ingredient3)

    assert repr(ingredient) and repr(ingredient2) == "Ingredient('ovo')"
    assert repr(ingredient3) == "Ingredient('salmão')"
