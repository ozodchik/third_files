cook_book = {}
with open("dishes.txt") as new_cookbook:
  line = new_cookbook.readline()
  while line != '':
    recept_name = line.strip()
    ingr_count = int(new_cookbook.readline())
    ingr = {}
    new_ingr = []
    for result in range(ingr_count):
      tmp = new_cookbook.readline().strip().split('|')
      ingredient_name, quantity, measure = tmp
      ingredient_list = {'ingredient_name': ingredient_name.strip(), 'quantity': int(quantity.strip()), 'measure': measure.strip()}
      new_ingr.append(ingredient_list)
    ingr[recept_name] = new_ingr 
    cook_book.update(ingr)
    new_cookbook.readline()
    line = new_cookbook.readline()
  # print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
  ingr_list = {}
  for item in dishes:
    for recipe, ingrs in cook_book.items():
      if item == recipe:
        for ingr in ingrs:
          ingredient_name = ingr['ingredient_name']
          measure = ingr['measure']
          quantity = ingr['quantity']
          quantity = quantity * person_count
          item_saved = ingr_list.get(ingredient_name, {'measure': measure, 'quantity': 0})
          quantity = quantity + item_saved['quantity']
          tmp = {ingredient_name: {'measure': measure, 'quantity': quantity}}
          ingr_list.update(tmp)
         
  print(ingr_list)

get_shop_list_by_dishes(["Омлет", "Фахитос"], 4)