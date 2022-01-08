from data import *

def report(resources, profit):
    for i in resources:
        unit = "ml"
        if i == "coffee":
            unit = "g"
        print(f'{i.capitalize()}: {resources[i]}{unit}')
    print(f'Money: ${profit}')

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def money_sufficient(total: int, coffee: str):
    res = True
    money_needed = menu[coffee]["cost"]
    if total < money_needed:
        print("Sorry that's not enough money. Money refunded.")
        res = False
    else:
        change = round(total - money_needed, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += money_needed
    return res

def make_coffee(resources, coffee):
    for i in resources:
        print(i, resources[i], menu[coffee]["ingredients"][i])
        resources[i] -= menu[coffee]["ingredients"][i]
    print(f"Here is your {coffee} ☕️. Enjoy!")

def restock():
    print("Restocking...")
    choice = str(input("What do you want to restock? Type 'coffee', 'milk', 'water' or 'all': "))
    quantity = int(input("How much do you need? "))
    global profit
    profit -= (75*quantity)/150
    resources[choice] += quantity


def main():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "report":
            report(resources, profit)
        elif choice == "off":
            is_on = False
        elif choice == "restock":
            restock()
        else:
            if is_resource_sufficient(menu[choice]["ingredients"]):
                total = process_coins()
                if money_sufficient(total, choice):
                    make_coffee(resources, choice)





if __name__ == "__main__":
    main()