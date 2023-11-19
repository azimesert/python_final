from load_data import load_data

def combo_calories_counter(orders):
    from calorie_counter import calorie_counter
    all_combos = load_data("data/combos.json")
    combos = all_combos['combos']
    combo_meal_list = []

    for combo in combos:
        if orders == combo['name']:
            combo_meal_list = combo['meals']
            break  # Exit the loop once we've found the matching combo

    total = calorie_counter(combo_meal_list)

    return total
