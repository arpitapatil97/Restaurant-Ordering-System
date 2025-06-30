#defining menu
menu = {
    'Pizza' : 40,
    'Pasta' : 50,
    'Burger' : 60,
    'Salad' : 70,
    'Coffee' : 80
}

#greet message
print("Welcome to ArShay's restaurant\nHere is the menu:")
print('Pasta ; Rs 40\nPasta : Rs 50\nBurger : Rs 60\nSalad : Rs 70\nCoffee : Rs 80')

Total = 0
while True:
    order = input('Enter the item you want to order = ')
    if order in menu:
        Total += menu[order]
        print(f'Order for {order} has been added')
    else:
        print('Sorry, the item you are looking for is currently not available')

    choice = input('Do you want to order anything else? (Yes/No): ')
    match choice:
        case 'no':
            break
 
print(f'The total amount to be paid = {Total}')
