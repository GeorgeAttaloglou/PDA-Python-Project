import Food

order = []
quantity = []
total_owed = 0

while True:
    print("Επιλογές: \n==========\n1. Έναρξη Παραγγελίας\n2. Εμφάνιση Παραγγελίας\n3. Αφαίρεση προϊόντος από την παραγγελία\n4. Πληρωμή")

    user_input = (input("Εισάγετε επιλογή: "))

    #Επιλογή αντικειμένου για την παραγγελία
    while user_input=="1":

        print(" Επιλογή #0: Chicken Burger\n Επιλογή #1: Ham Burger\n Επιλογή #2: Green Burger\n Επιλογή #3: Club Sandwich\n Επιλογή #4: Σαλάτα ceasar's\n Επιλογή #5: Κινόα με Λαχανικά")
        food_input = int(input("Εισάγετε τον αριθμό προϊόντος από το μενού: "))
    
        if food_input<0 or food_input>5:
            print("\nΗ επιλογή δεν υπάρχει, προσπαθήστε ξανά.\n")
            continue
        
        quantity.append (float(input("Εισάγετε ποσότητα: ")))
    
        if food_input == 0:
            order.append(Food.F0)
        elif food_input == 1:
            order.append(Food.F1)
        elif food_input == 2:
            order.append(Food.F2)
        elif food_input == 3:
            order.append(Food.F3)
        elif food_input == 4:
            order.append(Food.F4)
        elif food_input == 5:
            order.append(Food.F5)

        #reusable κομμάτι κώδικα για εισαγωγή ή τερματισμό
        repeat_input = input("Επιθυμείτε να εισάγετε άλλο? (y/n): ")
        if repeat_input=="y": continue
        if repeat_input=="n": break
        else : print("Μη έγγυρη επιλογή"); break

    #εμφάνηση της παραγγελίας στον χρήστη
    if user_input=="2":
        print(order)
        print(quantity)
        print("\n =========== \n αριθμός/όνομα/ποσότητα/τιμή τμχ/ΑΞΙΑ\n")
        for i,Food in enumerate(order):
            print(i,Food.name, quantity[i], Food.price, Food.price*quantity[i])

    while user_input=="3":
        for i,Food in enumerate(order):
            print(i,Food.name, quantity[i], Food.price, Food.price*quantity[i])
    
        #διαγράφει το αντικείμενο που επιλέγει ο χρήστης
        delete_input = int(input("Εισάγετε τον αριθμό προϊόντος που θέλετε να διαγράψετε: "))
        if delete_input < len(order):
            order.pop(delete_input)
            quantity.pop(delete_input)
        else:
            print("Η επιλογή δεν υπάρχει στην παραγγελία.")
        repeat_input = input("Επιθυμείτε να διαγραψετε άλλο αντικείμενο? (y/n): ")
        if repeat_input=="y": continue
        if repeat_input=="n": break
        else : print("Μη έγγυρη επιλογή"); break   

    if user_input=="4":
        total_owed=0
        payment = int(input("Εισάγετε το ποσό πληρωμής: "))
        for i in range(len(order)):
            order_total=order[i].price*quantity[i]
            total_owed+=order_total
        change = payment-total_owed
        print("Τα ρέστα είναι: ",change)
        break