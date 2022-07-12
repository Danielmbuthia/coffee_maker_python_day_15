MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
    "money": 0
}


def report():
    for key in resources:
        print(f"{key} : {resources[key]}")


def check_resources(coffee_type):
    water = MENU[coffee_type].get("ingredients")["water"]
    coffee = MENU[coffee_type]["ingredients"]["coffee"]
    milk = MENU[coffee_type].get("ingredients")["milk"]
    money_required = MENU[coffee_type]["cost"]
    return water, coffee, milk, money_required


def calculate_money(coffee_type, quarter_count, dimes_count, nickel_count, pennies_count):
    money = quarter_count * 0.25 + dimes_count * 0.1 + nickel_count * 0.05 + pennies_count * 0.01
    money_required = check_resources(coffee_type)[3]

    if money < money_required:
        print(f"You don't have enough money to purchase {coffee_type}")
        return
    elif money > money_required:
        change = money - money_required
        print(f"Here is {round(change, 2)} dollars in change")
        print(f"Here is your {coffee_type}. Enjoy!”")
    else:
        print(f"Here is your {coffee_type}. Enjoy!”")


def make_coffee(coffee_type):
    water_required = check_resources(coffee_type)[0]
    coffee_required = check_resources(coffee_type)[1]
    milk_required = check_resources(coffee_type)[2]
    money_required = check_resources(coffee_type)[3]

    if resources["water"] < water_required:
        print(f"You don't have enough water to make {coffee_type}")
        return
    if resources["coffee"] < coffee_required:
        print(f"You don't have enough coffee to make {coffee_type}")
        return
    if resources['milk'] < milk_required:
        print(f"You don't have enough milk to make {coffee_type}")
        return

    print("Please insert the coins")
    quarter_count = int(input("How many quarters? "))
    dimes_count = int(input("How many dimes? "))
    nickel_count = int(input("How many nickel? "))
    pennies_count = int(input("How many pennies? "))

    calculate_money(coffee_type, quarter_count, dimes_count, nickel_count, pennies_count)

    # every thing went well
    resources["water"] -= water_required
    resources["coffee"] -= coffee_required
    resources["milk"] -= milk_required
    resources["money"] += money_required


turn_off = False
while not turn_off:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino):")
    if coffee_choice.lower() == "report":
        report()
    elif coffee_choice.lower() == "off":
        turn_off = True
    else:
        make_coffee(coffee_choice.lower())
