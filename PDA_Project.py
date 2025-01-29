import Food

class PDA:
    def __init__(self):
        # Initialize empty lists to store order items and their quantities
        self.order = []
        self.quantity = []
    
    def display_menu(self):
        # Display the menu options with item numbers and prices
        print("\nMenu:")
        for i, food in enumerate(Food.menu):
            print(f" Option #{i}: {food.name} - ${food.price:.2f}")
    
    def add_item(self):
        self.display_menu()
        try:
            # Get the user's choice of food item
            food_index = int(input("Enter the product number: "))
            if 0 <= food_index < len(Food.menu):
                qty = int(input("Enter quantity: "))
                if qty > 0:
                    # Add the selected food item and quantity to the order
                    self.order.append(Food.menu[food_index])
                    self.quantity.append(qty)
                else:
                    print("Quantity must be positive.")
            else:
                print("Invalid option.")
        except ValueError:
            print("Invalid input, please enter numbers.")
    
    def delete_item(self):
        if not self.order:
            print("No items to delete.")
            return
        self.show_order()
        try:
            # Ask the user which item to delete
            delete_index = int(input("Enter item number to delete: ")) - 1
            if 0 <= delete_index < len(self.order):
                # Remove selected item from order and quantity lists
                self.order.pop(delete_index)
                self.quantity.pop(delete_index)
                print("Item removed successfully.")
            else:
                print("Invalid option.")
        except ValueError:
            print("Invalid input, please enter numbers.")
    
    def show_order(self):
        if not self.order:
            print("Your order is empty.")
            return
        print("\nCurrent Order:")
        total = 0
        for i, food in enumerate(self.order):
            subtotal = food.price * self.quantity[i]
            print(f"{i+1}: {food.name} - {self.quantity[i]} x ${food.price:.2f} = ${subtotal:.2f}")
            total += subtotal
        print(f"Total Amount: ${total:.2f}")
    
    def process_payment(self):
        if not self.order:
            print("No items in order.")
            return
        total_cost = sum(food.price * qty for food, qty in zip(self.order, self.quantity))
        try:
            # Prompt user to enter payment amount
            payment = float(input(f"Total due: ${total_cost:.2f}. Enter payment amount: "))
            if payment >= total_cost:
                print(f"Payment successful. Change: ${payment - total_cost:.2f}")
                # Clear the order after successful payment
                self.order.clear()
                self.quantity.clear()
            else:
                print("Insufficient payment. Try again.")
        except ValueError:
            print("Invalid input, please enter a valid amount.")
    
    def run(self):
        while True:
            # Display menu options for user interaction
            print("\nOptions:\n1. Add product\n2. Show Order\n3. Remove product from order\n4. Payment\n5. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.show_order()
            elif choice == "3":
                self.delete_item()
            elif choice == "4":
                self.process_payment()
            elif choice == "5":
                print("Thank you for using PDA.")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    pda = PDA()
    pda.run()
