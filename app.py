import sqlite3

def create_tables():
    connection = sqlite3.connect('ice_cream_parlor.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS seasonal_flavors (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY,
        name TEXT,
        quantity INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS suggestions (
        id INTEGER PRIMARY KEY,
        flavor_name TEXT,
        allergy_concerns TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS allergens (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cart (
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        product_name TEXT
    )
    ''')

    connection.commit()
    connection.close()

create_tables()

def add_seasonal_flavor(name, description):
    connection = sqlite3.connect('ice_cream_parlor.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO seasonal_flavors (name, description) VALUES (?, ?)', (name, description))
    connection.commit()
    connection.close()

def get_seasonal_flavors():
    connection = sqlite3.connect('ice_cream_parlor.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM seasonal_flavors')
    flavors = cursor.fetchall()
    connection.close()
    return flavors

def add_ingredient(name, quantity):
    connection = sqlite3.connect('ice_cream_parlor.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO ingredients (name, quantity) VALUES (?, ?)', (name, quantity))
    connection.commit()
    connection.close()

def get_ingredients():
    connection = sqlite3.connect('ice_cream_parlor.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM ingredients')
    ingredients = cursor.fetchall()
    connection.close()
    return ingredients

def add_suggestion(flavor_name, allergy_concerns):
    connection = sqlite3.connect('ice_cream_parlor.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO suggestions (flavor_name, allergy_concerns) VALUES (?, ?)', (flavor_name, allergy_concerns))
    connection.commit()
    connection.close()

def get_suggestions():
    connection = sqlite3.connect('ice_cream_parlor.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM suggestions')
    suggestions = cursor.fetchall()
    connection.close()
    return suggestions

def add_allergen(name):
    connection = sqlite3.connect('ice_cream_parlor.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO allergens (name) VALUES (?)', (name,))
    connection.commit()
    connection.close()

def get_allergens():
    connection = sqlite3.connect('ice_cream_parlor.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM allergens')
    allergens = cursor.fetchall()
    connection.close()
    return allergens

def add_to_cart(product_id, product_name):
    connection = sqlite3.connect('ice_cream_parlor.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO cart (product_id, product_name) VALUES (?, ?)', (product_id, product_name))
    connection.commit()
    connection.close()

def get_cart():
    connection = sqlite3.connect('ice_cream_parlor.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM cart')
    cart = cursor.fetchall()
    connection.close()
    return cart

def remove_from_cart(product_id):
    connection = sqlite3.connect('ice_cream_parlor.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM cart WHERE product_id = ?', (product_id,))
    connection.commit()
    connection.close()

def search_flavors(keyword):
    connection = sqlite3.connect('ice_cream_parlor.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM seasonal_flavors WHERE name LIKE ?', ('%' + keyword + '%',))
    flavors = cursor.fetchall()
    connection.close()
    return flavors

def main():
    while True:
        print("\nIce Cream Parlor Menu")
        print("1. Add Seasonal Flavor")
        print("2. View Seasonal Flavors")
        print("3. Add Ingredient")
        print("4. View Ingredients")
        print("5. Add Flavor Suggestion")
        print("6. View Flavor Suggestions")
        print("7. Add Allergen")
        print("8. View Allergens")
        print("9. Add to Cart")
        print("10. View Cart")
        print("11. Remove from Cart")
        print("12. Search Flavors")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter flavor name: ")
            description = input("Enter flavor description: ")
            add_seasonal_flavor(name, description)
        elif choice == '2':
            flavors = get_seasonal_flavors()
            for flavor in flavors:
                print(flavor)
        elif choice == '3':
            name = input("Enter ingredient name: ")
            quantity = int(input("Enter quantity: "))
            add_ingredient(name, quantity)
        elif choice == '4':
            ingredients = get_ingredients()
            for ingredient in ingredients:
                print(ingredient)
        elif choice == '5':
            flavor_name = input("Enter flavor name: ")
            allergy_concerns = input("Enter allergy concerns: ")
            add_suggestion(flavor_name, allergy_concerns)
        elif choice == '6':
            suggestions = get_suggestions()
            for suggestion in suggestions:
                print(suggestion)
        elif choice == '7':
            allergen_name = input("Enter allergen name: ")
            add_allergen(allergen_name)
        elif choice == '8':
            allergens = get_allergens()
            for allergen in allergens:
                print(allergen)
        elif choice == '9':
            product_id = int(input("Enter product ID: "))
            product_name = input("Enter product name: ")
            add_to_cart(product_id, product_name)
        elif choice == '10':
            cart = get_cart()
            for item in cart:
                print(item)
        elif choice == '11':
            product_id = int(input("Enter product ID to remove: "))
            remove_from_cart(product_id)
        elif choice == '12':
            keyword = input("Enter search keyword: ")
            results = search_flavors(keyword)
            for result in results:
                print(result)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
