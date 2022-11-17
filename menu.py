#!/usr/bin/env python3
import random

# Menu items from https://www.youngjoni.com/menu/
def generatemenu(tips=0.20, tax=0.06875):
    appetizer = {
        "Cauliflower": 17,
        "Bibim Grain Bowl": 18,
        "Korean Sweet Potatoes": 16,
        "Chicory Caesar": 15,
        "Charred Savoy Cabbage": 15,
        "Confit Mushrooms": 19,
        "Kimchi Trio": 10,
        "PEI Mussels": 22,
        "Grilled Chicken Wings": 18,
    }
    maincourse = {
        "Korean BBQ Pizza": 23,
        "Basque": 21,
        "My Sha-Roni": 20,
        "Umami Mama": 20,
        "Broccolini": 19,
        "Old Reliable": 15,
        "Tavern Pie": 20,
        "La Parisienne": 23,
        "Margherita": 16,
        "Amalfi Coast": 18,
        "Perfect Pickle Pie": 20,
        "Whole Fish": 45,
        "Thai Sausage Ssäm": 26,
        "Pork Spare Ribs": 24,
    }
    desserts = {
        "Soft Serve Ice Cream with Sea Salt & Olive Oil": 8,
        "Soft Serve Sundae": 10,
        "Mini Cone Trio": 9,
        "Church Basement Cookie & Bar Plate": 12,
        "Seasonal Crisp": 12,
    }
    cocktails = {
        "Rickey": 15,
        "Bottineau": 14,
        "Spritz": 14,
        "Julep": 16,
        "Cobbler": 13,
        "Negroni": 14,
        "Sling": 15,
        "Old Fashioned": 16,
    }
    randapp = random.sample(list(appetizer), 2)
    randmain = random.choice(list(maincourse))
    randdessert = random.choice(list(desserts))
    randdrinks = random.sample(list(cocktails), 2)

    result = f"""Your meal includes: \U0001F60B {randapp[0]} and {randapp[1]} as appetizers; \U0001F355 {randmain} as the main course; \U0001F368 {randdessert} as dessert; \U0001F378 {randdrinks[0]} and {randdrinks[1]} as your drink choices. The total cost after gratuity and tax is ${(1+tips+tax)*(appetizer[randapp[0]] + appetizer[randapp[1]] + maincourse[randmain] + desserts[randdessert] + cocktails[randdrinks[0]] + cocktails[randdrinks[1]]):,.2f}."""
    return {"Result": result}
