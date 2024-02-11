from resource_data import MENU, resources
import os


def get_order() -> dict:
    """Ask the user what flavour they want and then return flavour type.
    Allow machine to be turned off with the keyword 'off'.
    Allow user to enter keyword report, which will generate a report that shows current rescource values"""

    coffee_type = input("What would you like? (espresso, latte, cappuccino): ")
    while coffee_type not in MENU.keys():

        if coffee_type == "report":
            print(f"Coffee Machine Rescources: {resources}\n")
            
        elif coffee_type == "off":
            print("Machine Powering Off!")
            os._exit(200)

        coffee_type = input("What would you like? (espresso, latte, cappuccino): ")

    coffee_type = MENU[coffee_type]
    return coffee_type



def check_rescources(order: dict, deduct: bool = False) -> bool:
    """Check if there are enough resources to make coffee. Returns either true or false based on result. 
    Can provide deduct boolean to deduct from resources"""

    order = order["ingredients"]
    for i in order:

        if resources[i] < order[i]:
            print(f"Sorry not enough {i}!") 
            return False

        elif deduct:
            resources[i] -= order[i]

    return True



def enter_coins() -> float:
    """Allows user to enter money in the form of coins. Returns total of coins"""

    while True:
        try:
            pennies = (int(input("How many pennies?: ")) / 100)
            nickles = (int(input("How many nickles?: ")) / 100) * 5
            dimes = (int(input("How many dimes?: ")) / 100) * 10 
            quarters = (int(input("How many quarters?: ")) / 100) * 25

            coin_amount = pennies + nickles + dimes + quarters
            return coin_amount

        except ValueError:
            print("Please enter a valid amount!\n")       
            



            
def transaction(order: dict, amount) -> bool:
    """Check if transaction is successful. Returns result of check rescources or prints message if not enough money"""

    if order["cost"] > amount: 
        print("Sorry that's not enough money. Money refunded")

    else:
        print(f"Here is your ${round(amount - order['cost'], 2)} change!")
        try:
            resources["Money"] += order["cost"] 
        except KeyError:
            resources["Money"] = order["cost"] 

        return check_rescources(order, deduct=True)



def main():

    while True:
        customer_order = get_order()
        if not check_rescources(customer_order, deduct = False):
            break

        customer_amount = enter_coins()
        transaction(customer_order, customer_amount)


main()

