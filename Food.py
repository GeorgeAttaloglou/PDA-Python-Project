class Food:
    def __init__(self, name, description, price):
      self.name = name
      self.description = description
      self.price = price
    
    def __repr__(self):
     return str(self)
    
    def __str__(self):
     return f"{self.name},{self.description},{self.price}"
               
F0=Food("Chicken Burger","Burger με κοτόπουλο, bacon, τυρί edam, τομάτα, μαρούλι με μαγιονέζα",4.20)
F1=Food("Ham Burger","Burger με μπιφτέκι, τυρί, κέτσαπ, μουστάρδα",2.85)
F2=Food("Green Burger","Burger με ζουμερό μπιφτέκι, τυρί, φρέσκια τομάτα, μαρούλι,κρεμμύδι, πίκλες, κέτσαπ και dressing sauce",4.20)
F3=Food("Club Sandqich","Club sandwich με 3 πλούσιες στρώσεις Philadelphia σε φρυγανισμένο ψωμί του τοστ με ζουμερό κοτόπουλο φιλέρο, bacon, τομάτα, μαρούλι και τηγανητές πατάτες",10.90)
F4=Food("Σαλάτα ceasar's","Δροσερή πράσινη σαλάτα με ζουμερό κοτόπουλου σε βάση μαρουλιού, με καλαμπόκι, κρουτόν, τριμμένο τυρί και vinaigreve ελαιόλαδου",6.90)
F5=Food("Κινόα με Λαχανικά","Δροσερή σαλάτα με κινόα, κόκκινη πιπεριά, τοματίνια,αγγούρι, δυόσμο, φρέσκο μαϊντανό και sauce λαδολέμονο.",6.30)
    
#Λίστα του με όνομα μενού που περιεχει τα διαθέσημα φαγητά για παραγγελία
menu=[F0,F1,F2,F3,F4,F5]