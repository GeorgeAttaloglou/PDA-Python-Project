import Food

order = []
quantity = []

def Add_Item():
    print(" Option #0: Chicken Burger\n Option #1: Ham Burger\n Option #2: Green Burger\n Option #3: Club Sandwich\n Option #4: Caesar's Salad\n Option #5: Quinoa with Vegetables")
    food_input = int(input("Enter the product number from the menu: "))
    
    if food_input < 0 or food_input > 5:
        print("\nThe option does not exist, please try again.\n")
        return
    
    quantity.append(int(input("Enter quantity: ")))
    
    match food_input:
        case 0:
            order.append(Food.F0)
        case 1:
            order.append(Food.F1)
        case 2:
            order.append(Food.F2)
        case 3:
            order.append(Food.F3)
        case 4:
            order.append(Food.F4)
        case 5:
            order.append(Food.F5)


def Delete_Item():
    for i, Food in enumerate(order):
        print(i + 1, Food.name, quantity[i], Food.price, Food.price * quantity[i])

    # deletes the item selected by the user
    delete_input = int(input("Enter the product number you want to delete: ")) - 1
    if delete_input < len(order):
        order.pop(delete_input)
        quantity.pop(delete_input)
    else:
        print("The option does not exist in the order.")


while True:
    print("Options: \n==========\n1. Add product\n2. Show Order\n3. Remove product from order\n4. Payment")

    user_choice = input("Enter choice: ")

    while user_choice == "1":

        Add_Item()

        repeat_input = input("Do you want to add another? (y/n): ")
        if repeat_input.lower() == "y": continue
        if repeat_input.lower() == "n": break
        else: print("Invalid choice"); break

    if user_choice == "2":
        for i, Food in enumerate(order):
            print(f"\n{i + 1}: {Food.name}, Quantity: {quantity[i]}, Unit Price: {Food.price}, Total Value: {Food.price * quantity[i]}")

    while user_choice == "3":

        Delete_Item()

        repeat_input = input("Do you want to delete another item? (y/n): ")
        if repeat_input == "y": continue
        if repeat_input == "n": break
        else: print("Invalid choice"); break   

    if user_choice == "4":
        total_owed = 0

        payment = float(input("Enter the payment amount: "))
        for i in range(len(order)):
            order_total = order[i].price * quantity[i]
            total_owed += order_total
            
        change = payment - total_owed
        if change < 0:
            print("The payment amount is less than the total order amount.")
            continue
        print("The change is: ", change)
        
        break