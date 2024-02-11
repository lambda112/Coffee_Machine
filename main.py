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
    order = get_order()
    
    for i in resources:
        coffee_amount = order["ingredients"].get(i, False)

        if coffee_amount and resources[i] < coffee_amount:
            print(f"Sorry not enough {i}!") 

        elif coffee_amount: 
            resources[i] -= coffee_amount

    return resources

# Process coins 


# Check if transaction is successful