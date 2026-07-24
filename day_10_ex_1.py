print("Restaurants")
print("1. KFC")
print("2. Domino's")
print("3. Haldirams")

restaurant = input("Choose a restaurant (1-3): ")

if restaurant == "1":
    print("Menu:")
    print("1 = chicken burger")
    print("2 = chicken nuggets")
    print("3 = chicken sandwich")

    meal = input("Choose a meal: ")
    if meal == "1":
        print("You ordered a chicken burger!")
    elif meal == "2":
        print("You ordered chicken nuggets!")
    elif meal == "3":
        print("You ordered a chicken sandwich!")
    else:
        print("Invalid choice")

elif restaurant == "2":
    print("Menu:")
    print("1 = pizza")
    print("2 = burger")
    print("3 = sandwich")
    meal = input("Choose a meal: ")
    if meal == "1":
        print("Menu:")
        print("1 = chicken pizza")
        print("2 = paneer pizza")
        print("3 = capsicum pizza")
        pizza_choice = input("Choose a pizza: ")
        if pizza_choice == "1":
            print("You ordered a chicken pizza!")
        elif pizza_choice == "2":
            print("You ordered a paneer pizza!")
        elif pizza_choice == "3":
            print("You ordered a capsicum pizza!")
        else:
            print("Invalid pizza choice!")
    elif meal == "2":
        print("You ordered a burger!")      
    elif meal == "3":
        print("You ordered a sandwich!")    
    else:
        print("Invalid choice")

elif restaurant == "3":
    print("Menu:")
    print("1 = Rice & Curry")
    print("2 = Pasta")
    print("3 = Sandwich")

    meal = input("Choose a meal: ")

    if meal == "1":
        print("You ordered Rice & Curry")
    elif meal == "2":
        print("You ordered Pasta")
    elif meal == "3":
        print("You ordered a Sandwich")
    else:
        print("Invalid choice")

else:
    print("Invalid restaurant choice")
