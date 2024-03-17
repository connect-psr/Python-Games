#TODO: 1] Check resources sufficient to make order..

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
    "water": 150,
    "milk":  400,
    "coffee": 200
}

#TODO: 2] Print report of all coffee machine data..

money = 0
on_Machine = True


def is_sufficient_resources(order_ingredients):
    """Return True if order can be made either False"""
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item} to make your drink..")
            return False
    return True


def coins_process():
    """Return the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many Quarters: ")) *0.25
    total += int(input("How many Dimes: ")) *0.1
    total += int(input("How many Nickels: ")) *0.05
    total += int(input("How many Pennies: ")) *0.01
    return total


def is_successful_transaction(received_money,cost_of_drink):
    """Return True if Money is sufficient either False"""
    if received_money >= cost_of_drink:
        change = received_money - cost_of_drink
        print(f"Here is your ${change} in change.")
        global money
        money += cost_of_drink
        return True
    else:
        print("Sorry!, But that's not enough money.. Money refunded.")
        return False


def make_coffee(order_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your{order_name} ☕..")


while on_Machine:
    choice = input("What would you like to drink ? (espresso/latte/cappuccino): ")
    if choice== "off":
        on_Machine= False
    elif choice == "report":
        print(f"Water: {resources['water']}ml ")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm ")
        print(f"Money: ${money} ")
    else:
        drink = MENU[choice]
        if is_sufficient_resources(drink["ingredients"]):
            payment = coins_process()
            if is_successful_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

