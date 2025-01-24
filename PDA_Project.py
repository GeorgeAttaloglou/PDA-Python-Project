import Food

order = []
quantity = []

def Add_Item():
    print(" Επιλογή #0: Chicken Burger\n Επιλογή #1: Ham Burger\n Επιλογή #2: Green Burger\n Επιλογή #3: Club Sandwich\n Επιλογή #4: Σαλάτα ceasar's\n Επιλογή #5: Κινόα με Λαχανικά")
    food_input = int(input("Εισάγετε τον αριθμό προϊόντος από το μενού: "))
    
    if food_input < 0 or food_input > 5:
        print("\nΗ επιλογή δεν υπάρχει, προσπαθήστε ξανά.\n")
        return
    
    quantity.append(int(input("Εισάγετε ποσότητα: ")))
    
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
    for i,Food in enumerate(order):
        print(i + 1, Food.name, quantity[i], Food.price, Food.price*quantity[i])

    #διαγράφει το αντικείμενο που επιλέγει ο χρήστης
    delete_input = int(input("Εισάγετε τον αριθμό προϊόντος που θέλετε να διαγράψετε: ")) - 1
    if delete_input < len(order):
        order.pop(delete_input)
        quantity.pop(delete_input)
    else:
        print("Η επιλογή δεν υπάρχει στην παραγγελία.")


while True:
    print("Επιλογές: \n==========\n1. Προσθήκα προιόντος\n2. Εμφάνιση Παραγγελίας\n3. Αφαίρεση προϊόντος από την παραγγελία\n4. Πληρωμή")

    user_choice = (input("Εισάγετε επιλογή: "))

    while user_choice == "1":

        Add_Item()

        repeat_input = input("Επιθυμείτε να εισάγετε άλλο? (y/n): ")
        if repeat_input.lower() == "y": continue
        if repeat_input.lower() == "n": break
        else : print("Μη έγγυρη επιλογή"); break

    if user_choice == "2":
        for i,Food in enumerate(order):
            print(f"\n{i + 1}: {Food.name}, Ποσότητα: {quantity[i]}, Τιμή τεμαχίου: {Food.price}, Τελική αξία: {Food.price*quantity[i]}")

    while user_choice == "3":

        Delete_Item()

        repeat_input = input("Επιθυμείτε να διαγραψετε άλλο αντικείμενο? (y/n): ")
        if repeat_input == "y": continue
        if repeat_input == "n": break
        else : print("Μη έγγυρη επιλογή"); break   

    if user_choice == "4":
        total_owed = 0

        payment = float(input("Εισάγετε το ποσό πληρωμής: "))
        for i in range(len(order)):
            order_total = order[i].price * quantity[i]
            total_owed += order_total
            
        change = payment-total_owed
        if change < 0:
            print("Το ποσό πληρωμής είναι μικρότερο από το συνολικό ποσό της παραγγελίας.")
            continue
        print("Τα ρέστα είναι: ",change)
        
        break