from Menu import MENU

Machine_resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
    "money" : 0
}
while True:
    Order = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()

    if Order == 'report':

        print(f"Water: {Machine_resources['water']}ml")
        print(f"Milk: {Machine_resources['milk']}ml")
        print(f"Coffee: {Machine_resources['coffee']}g")
        print(f"Money: ${Machine_resources['money']}")

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
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many diems?: ")) * 0.10
        nikels = int(input("How many nikels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01

        money_recived = quarters + dimes + nikels + pennies

        change = money_recived - MENU[f"{Order}"]['cost']

        if change < 0:
            print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Here is ${change} in change.")
            print(f"Here is your {Order.title()}☕, Enjoy.")

            Machine_resources['money'] += money_recived
            
            for ingredients in Order_ingredients:
                Machine_resources[ingredients] -= Order_ingredients[ingredients]
