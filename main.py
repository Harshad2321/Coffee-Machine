MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def money_entered():
    print("Please insert the money!!")
    total = int(input("Enter the number of pennies $:")) * 0.01
    total += int(input("Enter the number of Dime $:")) * 0.1
    total += int(input("Enter the number of Nickel $:")) * 0.05
    total += int(input("Enter the number of Quarter $:")) * 0.25
    return total

MONEY_EARNED = 0
machine = True
while machine:
    user_choice = input(
        "Enter the number of what you want:\n1: espresso\n2: latte\n3: cappuccino\nWhat would you like? (or type 'report' to check resources): ")

    if user_choice == "report":
        for key, value in resources.items():
            print(f"{key} : {value}")
        print(f"The total money earned is ${MONEY_EARNED:.2f}....")

    else:
        total = money_entered()

        if user_choice == '1':  # Espresso
            cost = MENU["espresso"]["cost"]
            ingredients = MENU["espresso"]["ingredients"]
        elif user_choice == '2':  # Latte
            cost = MENU["latte"]["cost"]
            ingredients = MENU["latte"]["ingredients"]
        elif user_choice == '3':  # Cappuccino
            cost = MENU["cappuccino"]["cost"]
            ingredients = MENU["cappuccino"]["ingredients"]
        else:
            print("Please enter a valid option!")
            continue

        if total >= cost:
            # Check if resources are sufficient
            if resources["water"] < ingredients["water"] or resources["coffee"] < ingredients["coffee"] or (
                    ("milk" in ingredients) and resources["milk"] < ingredients["milk"]):
                print("Sorry, there are not enough ingredients.")
                print("Here is your money back.")
                total = 0
            else:
                # Deduct ingredients
                resources["water"] -= ingredients["water"]
                resources["coffee"] -= ingredients["coffee"]
                if "milk" in ingredients:
                    resources["milk"] -= ingredients["milk"]
                # Calculate and give back change
                change = total - cost
                print(f"You have given ${total:.2f} and your bill is ${cost}.")
                print(f"Here is your change ${change:.2f}.")
                print(f"Here is your {user_choice} ☕️. Enjoy!")
                MONEY_EARNED += total
        elif total < cost:
            print(f"You have given ${total:.2f}, but your bill is ${cost}.")
            print(f"Here is your money back. Please give the correct amount.")

        # Ask if the user wants to continue or exit
        continue_choice = input("Would you like another drink? (yes/no): ").lower()
        if continue_choice != 'yes':
            machine = False
            print("Thank you for using the coffee machine. Goodbye!")

