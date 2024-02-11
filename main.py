from rescource_data import MENU, resources
import os

# Ask the user what flavour they want return flavour type
# Allow machine to be turned off with the keyword 'off' 
# Allow user to enter keyword report, which will generate a report that shows current rescource values
def get_order():
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



# Check if there are enough rescources
def check_rescources(): 
    order = get_order()["ingredients"]

    for i in order:
        if resources[i] < order[i]:
            print(f"Sorry not enough {i}!") 
        else:
            resources[i] -= order[i]

    return resources


# Process coins 
def enter_coins():
    while True:
        try:
            pennies = (int(input("How many pennies?: ")) / 100)
            nickles = (int(input("How many nickles?: ")) / 100) * 5
            dimes = (int(input("How many dimes?: ")) / 100) * 10 
            quarters = (int(input("How many quarters?: ")) / 100) * 25
            amount = pennies + nickles + dimes + quarters
            return amount

        except ValueError:
            print("Please enter a valid amount!\n")       
            

print(enter_coins())
# Check if transaction is successful