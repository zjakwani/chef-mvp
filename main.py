# MVP app for a chef keeping track of dishes

# global list of dishes
dishes = ["Pancakes", "Waffles"]


# string for the menu of commands
cmd_menu = """\nSelect from the following commands:
        a. Add dish
        b. Delete dish
        c. Quit\n"""


# Outputs all dishes
def output_dishes():
    print("\nList of dishes:")
    for i in range(len(dishes)):
        print(f"\t{str(i+1)}. {dishes[i]}")


# Basic CLI
def main():
    print("Welcome to my chef app")
    
    while True:

        output_dishes()
        print(cmd_menu)

        # Switch-like statement for each command
        cmd = input("Command: ")

        if cmd == "a":
            name = input("Name of dish: ")
            dishes.append(str(name))

        elif cmd == "b":
            remove_index = input("Number of dish to be removed: ")

            if not remove_index.isnumeric() or int(remove_index)-1 < 0 or int(remove_index)-1 >= len(dishes):
                print("Error: please enter a valid dish")
            else:
                dishes.pop(int(remove_index) - 1)

        else:
            break


if __name__ == "__main__":
    main()
