# MVP app for a chef keeping track of dishes

dishes = ["Pancakes", "Waffles"]

print("Welcome to my chef app")

# Basic CLI
while True:

    # Outputs all dishes
    print("\nList of dishes:")
    for i in range(len(dishes)): print(f"\t{str(i+1)}. {dishes[i]}")

    # Command menu
    print("\nSelect from the following commands")
    print("\ta. Add dish")
    print("\tb. Delete dish")
    print("\tc. Quit\n")
    cmd = input("Command: ")


    # Switch-like statement for each command
    if cmd == "a":
        name = input("Name of dish: ")
        dishes.append(str(name))

    elif cmd == "b":
        remove_index = input("Number of dish to be removed: ")

        if not remove_index.isnumeric() or int(remove_index)-1 < 0 or int(remove_index)-1 >= len(dishes):
            print("Erorr: please enter a valid dish")
        else:
            dishes.pop(int(remove_index) - 1)

    else:
        break
