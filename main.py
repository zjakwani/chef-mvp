# MVP app for a chef keeping track of dishes


class Dish:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

# global list of dishes
sushi = Dish("Sushi", ["Rice", "Fish"])
maki = Dish("Maki Roll", ["Rice", "Fish", "Seaweed"])
spaghetti = Dish("Spaghetti", ["Sauce", "Pasta", "Cheese"])
lasagna = Dish("Lasagna", ["Pasta", "Meat", "Cheese", "Sauce", "Pasta"])
dishes = [sushi, maki, spaghetti, lasagna]


# string for the menu of commands
cmd_menu = """\nSelect from the following commands:
        a. Add dish
        b. Delete dish
        c. Quit
        d. Get dishes by ingredient
        e. Output all dishes\n"""

# In our input we have everything we need to make the dish
def dishes_by_ingredient():
    ingredient_list = get_ingredient_list()
    # set_ingredients = set(ingredient_list)

    # O(num_dishes * max_ingredients * input_size)
    filtered_list = []
    for dish in dishes:
        valid = True
        visited = [False for _ in range(len(ingredient_list))]

        for ingredient in dish.ingredients:

            contains = False
            for i in range(len(ingredient_list)):
                if visited[i]:
                    continue
                if ingredient == ingredient_list[i]:
                    visited[i] = True
                    contains = True
                    break

            if not contains:
                valid = False
                break

        if valid:
            filtered_list.append(dish)

    print("Here are the dishes you can make: ")
    output_dishes(filtered_list)


# Outputs all dishes
def output_dishes(dish_list):
    print("\nList of dishes:")
    for i in range(len(dish_list)):
        cur_dish = dish_list[i]
        print(f"\t{str(i+1)}. {cur_dish.name}")
        for i in range(len(cur_dish.ingredients)):
            print("\t\t" + str(i+1) + ". " + cur_dish.ingredients[i])

def get_ingredient_list():
    ingredient_list = []
    first_ingredient = input("Add an ingredient: ")
    ingredient_list.append(str(first_ingredient))

    while True:
        current_ingredient = input("Add an ingredient or press q to stop: ")
        if current_ingredient == "q":
            break
        else:
            ingredient_list.append(str(current_ingredient))
    return ingredient_list

def add_dish():
    name = input("Name of dish: ")

    ingredient_list = get_ingredient_list()

    new_dish = Dish(name, ingredient_list)
    dishes.append(new_dish)

def remove_dish():
    remove_index = input("Number of dish to be removed: ")

    if not remove_index.isnumeric() or int(remove_index)-1 < 0 or int(remove_index)-1 >= len(dishes):
        print("Error: please enter a valid dish")
    else:
        dishes.pop(int(remove_index) - 1)


# Basic CLI
def main():
    print("Welcome to my chef app")
    
    while True:

        print(cmd_menu)

        # Switch-like statement for each command
        cmd = input("Command: ")

        if cmd == "a":
            add_dish()
        elif cmd == "b":
            remove_dish()
        elif cmd == "d":
            dishes_by_ingredient()
        elif cmd == "e":
            output_dishes(dishes)
        else:
            break


if __name__ == "__main__":
    main()
