from load_data import load_data
from order_checker import order_checker

def display_menu(meals, combos):
    print("The menu is here: ")

    meal_names = [meal['name'] for meal in meals]
    combo_names = [combo['name'] for combo in combos]
    
    menu_items = meal_names + combo_names

    for index, item in enumerate(menu_items):
        if index == len(menu_items) - 1:
            print('and', item)
        else:
            print(item + ',', end=' ')

def order_func():
    all_meals = load_data("data/meals.json")
    meals = all_meals['meals']

    all_combos = load_data("data/combos.json")
    combos = all_combos['combos']

    display_menu(meals, combos)

    print("Please enter the names of your orders here, separating them with a ',': ")

    order = input()

    result = order_checker(order)

    return result
