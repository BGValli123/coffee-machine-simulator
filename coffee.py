MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 3.0,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def check_resources(order):
    for item in order:
        if order[item] > resources.get(item, 0):
            print(f"Sorry, not enough {item}")
            return False
    return True

def process_coins():
    print("Insert coins:")
    total = int(input("Quarters: ")) * 0.25
    total += int(input("Dimes: ")) * 0.10
    total += int(input("Nickels: ")) * 0.05
    total += int(input("Pennies: ")) * 0.01
    return total

def make_coffee(choice):
    for item in MENU[choice]["ingredients"]:
        resources[item] -= MENU[choice]["ingredients"][item]
    print(f"Here is your {choice} ☕ Enjoy!")

while True:
    choice = input("Choose (espresso/latte/cappuccino) or 'report' or 'off': ").lower()

    if choice == "off":
        break

    elif choice == "report":
        print(resources)

    elif choice in MENU:
        if check_resources(MENU[choice]["ingredients"]):
            payment = process_coins()
            if payment >= MENU[choice]["cost"]:
                change = round(payment - MENU[choice]["cost"], 2)
                print(f"Here is ${change} in change")
                resources["money"] += MENU[choice]["cost"]
                make_coffee(choice)
            else:
                print("Sorry, not enough money. Refunded.")