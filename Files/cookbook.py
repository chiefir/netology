def get_recipe(file_name):
    """Reads through the file and returns a dictionary with meal name keys and ingredients values"""
    with open(file_name, 'r') as f:
        meals = {}
        while True:
            name = f.readline().strip()
            if name:
                lines = f.readline()
                ingredients = []
                for _ in range(int(lines)):
                    line = f.readline().split("|")
                    ingredients.append({'ingredient_name': line[0].strip(), 'quantity': line[1].strip(), 'measure': line[2].strip()})
                f.readline()
                meals[name] = ingredients
            else:
                break
    return meals

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    """Iterating over cook_book searching for ingredients. If ingredient is not in the shop_list, add the position,
    if ingredient already is in the shop_list, add extra qty"""
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list.setdefault(ingredient['ingredient_name'], {'measure': ingredient['measure'], 'quantity': ingredient['quantity']})
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] = int(shop_list[ingredient['ingredient_name']]['quantity']) + int(ingredient['quantity'])
    for ingredient, qty in shop_list.items():
        """Multiplying ingredients on persons qty planned"""
        qty['quantity'] = int(qty['quantity']) * int(person_count)
    return shop_list

"""Reading recipes"""
cook_book = get_recipe('recipes.txt')

"""Passing meals list and persons qty"""
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
