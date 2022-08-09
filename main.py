#task1
def my_cook_book():
    with open('dishes.txt', encoding='utf-8') as file:
        cook_book = {}
        for txt in file.read().split('\n\n'):
            name, _, *args = txt.split('\n')
            tmp = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                tmp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = tmp
    return cook_book

print(my_cook_book())

#task2
def get_shop_list_by_dishes(dishes, persons):
    menu = my_cook_book()
    shopping_list = {}
    for dish in dishes:
        for item in (menu[dish]):
            items_list = dict([(item['ingredient_name'],
                                {'measure': item['measure'], 'quantity': int(item['quantity']) * persons})])
            if shopping_list.get(item['ingredient_name']):
                extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                              int(items_list[item['ingredient_name']]['quantity']))
                shopping_list[item['ingredient_name']]['quantity'] = extra_item

print(get_shop_list_by_dishes(['Фахитос'], 10))