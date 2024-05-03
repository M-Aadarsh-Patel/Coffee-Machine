from Menu import MENU

Machine_resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
    "money" : 0
}

def caluculate_coins(Quarters, Dimes, Nikels, Pennies):
    return (Quarters * 0.25) + (Dimes) + (Nikels) + (Pennies)

def report(Coffee_Machine_resources):
    print(f"Water: {Coffee_Machine_resources['water']}ml")
    print(f"Milk: {Coffee_Machine_resources['milk']}ml")
    print(f"Coffee: {Coffee_Machine_resources['coffee']}g")
    print(f"Money: ${Coffee_Machine_resources['money']}")

while True:
    Order = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()

    if Order == 'report':
        report(Coffee_Machine_resources=Machine_resources)
        continue

    Order_ingredients = MENU[f"{Order}"]['ingredients']

    for ingredients in Order_ingredients:
        if Machine_resources[ingredients] >= Order_ingredients[ingredients]:
            ingredients_sufficient = True
        else:
            ingredients_sufficient = False
            print(f"Sorry, the Machine does not have enough resources to make a {Order.title()}")
            break

    if ingredients_sufficient == True:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many diems?: "))
        nikels = int(input("How many nikels?: "))
        pennies = int(input("How many pennies?: "))

        money_recived = caluculate_coins(Quarters=quarters, Dimes=dimes, Nikels=nikels, Pennies=pennies)

        change = money_recived - MENU[f"{Order}"]['cost']

        if change < 0:
            print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Here is ${change} in change.")
            print(f"Here is your {Order.title()}☕, Enjoy.")

            Machine_resources['money'] += money_recived
            
            for ingredients in Order_ingredients:
                Machine_resources[ingredients] -= Order_ingredients[ingredients]

    if Order == 'off':
        break