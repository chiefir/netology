class CookBook:
    def __init__(self, name, recipes_list_path):
        self.name = name
        self.meals = self.populate_recipes_from_file(recipes_list_path)

    def populate_recipes_from_file(self, recipes_list_path):
        with open(recipes_list_path, 'r') as f:
            recipes = {}
            while True:
                name = f.readline().strip()
                if name:
                    lines = f.readline()
                    ingredients = []
                    for _ in range(int(lines)):
                        line = f.readline().split("|")
                        ingredients.append({'ingredient_name': line[0].strip(), 'quantity': line[1].strip(), 'measure': line[2].strip()})
                    f.readline()
                    recipes[name] = ingredients
                else:
                    break
        return recipes

class ShopList:
    def __init__(self, name, cook_book_name, meals_list, guests_qty):
        self.name = name
        self.shop_list = self.make_shop_list(cook_book_name.meals, meals_list, guests_qty)

    def make_shop_list(self, cook_book_name, meals_list, guests_qty):
        ingredients_list = {}
        # Iterating over cook_book searching for ingredients. If ingredient is not in the ingredients_list, add the position,
        # if ingredient already is in the ingredients_list, add extra qty
        for dish in meals_list:
            for ingredient in cook_book_name[dish]:
                if ingredient['ingredient_name'] not in ingredients_list:
                    ingredients_list.setdefault(ingredient['ingredient_name'], {'measure': ingredient['measure'], 'quantity': ingredient['quantity']})
                else:
                    ingredients_list[ingredient['ingredient_name']]['quantity'] = int(ingredients_list[ingredient['ingredient_name']]['quantity']) + int(ingredient['quantity'])
        for ingredient, qty in ingredients_list.items():
            #Multiplying ingredients on persons qty planned
            qty['quantity'] = int(qty['quantity']) * int(guests_qty)
        return ingredients_list

if __name__ == '__main__':

    dinner_cook_book = CookBook('dinner_cook_book', 'recipes.txt')
    dinner_shop_list = ShopList('dinner_shop_list', dinner_cook_book, ['Запеченный картофель', 'Омлет'], 2)


    print(dinner_shop_list.shop_list)