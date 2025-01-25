# Coffee Machine Program

This is a simple Python-based Coffee Machine program that allows users to order different coffee drinks, manage resources, and handle payments. Perfect for learning basic programming concepts such as loops, conditionals, and functions!

---

## Features

- **Menu Options**:
  - Espresso
  - Latte
  - Cappuccino

- **Resource Management**:
  - Tracks water, milk, and coffee usage.
  - Checks if there are enough ingredients to prepare the selected drink.

- **Payment Handling**:
  - Accepts pennies, dimes, nickels, and quarters.
  - Calculates total money inserted.
  - Provides change if overpayment is made.

- **Report Functionality**:
  - Displays the current resources and total money earned.

- **User Interaction**:
  - Continuously serves drinks until the user decides to exit.

---

## Program Overview

### Menu Items
Each coffee drink has specific ingredient requirements and costs:

```python
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
```

### Resources
The coffee machine starts with predefined resources:

```python
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
```

### Payment Function
The program calculates the total amount entered by the user based on coin input:

```python
def money_entered():
    print("Please insert the money!!")
    total = int(input("Enter the number of pennies $:")) * 0.01
    total += int(input("Enter the number of Dime $:")) * 0.1
    total += int(input("Enter the number of Nickel $:")) * 0.05
    total += int(input("Enter the number of Quarter $:")) * 0.25
    return total
```

---

## How to Use

1. **Run the Program**:
   Execute the Python file in your terminal or IDE.

2. **Choose a Drink**:
   Select one of the available drinks by entering its corresponding number:
   - `1` for Espresso
   - `2` for Latte
   - `3` for Cappuccino

3. **Insert Coins**:
   Enter the number of pennies, dimes, nickels, and quarters to pay for the selected drink.

4. **Get Your Drink**:
   If the payment is sufficient and resources are available, you'll receive your drink and any change due.

5. **Check Resources**:
   Type `report` to see the current levels of water, milk, coffee, and total money earned.

6. **Continue or Exit**:
   After each drink, decide whether to order another or exit the program.

---

## Example Interaction

```
Enter the number of what you want:
1: espresso
2: latte
3: cappuccino
What would you like? (or type 'report' to check resources): 2

Please insert the money!!
Enter the number of pennies $:50
Enter the number of Dime $:0
Enter the number of Nickel $:0
Enter the number of Quarter $:10

You have given $2.50 and your bill is $2.50.
Here is your change $0.00.
Here is your latte ☕️. Enjoy!

Would you like another drink? (yes/no): no
Thank you for using the coffee machine. Goodbye!
```

## Contributing
Feel free to contribute to this project by submitting issues or pull requests. Suggestions for improvements are always welcome!

---

Enjoy your coffee! ☕

