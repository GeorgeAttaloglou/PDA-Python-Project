class Food:
    def __init__(self, name, description, price):
      self.name = name
      self.description = description
      self.price = price
    
    def __repr__(self):
     return str(self)
    
    def __str__(self):
     return f"{self.name},{self.description},{self.price}"
               
F0 = Food("Chicken Burger", "Burger with chicken patty, bacon, cheese, tomato and mayo", 4.20)
F1 = Food("Ham Burger", "Burger with patty, cheese, ketchup, mustard", 2.85)
F2 = Food("Green Burger", "Burger with juicy patty, cheese, fresh tomato, lettuce, onion, pickles, ketchup, and dressing sauce", 4.20)
F3 = Food("Club Sandwich", "Club sandwich with 3 rich layers of Philadelphia on toasted sandwich bread with juicy chicken fillet, bacon, tomato, lettuce, and french fries", 10.90)
F4 = Food("Caesar Salad", "Fresh green salad with juicy chicken on a lettuce base, with corn, croutons, grated cheese, and olive oil vinaigrette", 6.90)
F5 = Food("Quinoa with Vegetables", "Refreshing salad with quinoa, red pepper, cherry tomatoes, cucumber, mint, fresh parsley, and lemon olive oil sauce", 6.30)
    
#Λίστα του με όνομα μενού που περιεχει τα διαθέσημα φαγητά για παραγγελία
menu=[F0,F1,F2,F3,F4,F5]