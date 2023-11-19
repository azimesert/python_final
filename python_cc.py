from load_data import load_data

def calorie_counter(orders):
    from combo_calories_counter import combo_calories_counter
    all_meals = load_data("data/meals.json")
    meals = all_meals['meals']

    all_combos = load_data("data/combos.json")
    combos = all_combos['combos']

    def get_meal_calories(order):
        for meal in meals:
            if order in (meal['name'], meal['id']):
                return meal['calories']
        return 0

    def get_combo_calories(order):
        for combo in combos:
            if order == combo['name']:
                return combo_calories_counter(order)
        return 0

    total = 0

    for order in orders:
        if 'combo' in order:
            total += get_combo_calories(order)
        else:
            total += get_meal_calories(order)

    return total
