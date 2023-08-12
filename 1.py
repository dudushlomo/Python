import os
from time import sleep
"""
import must be in top of file.
Importing os library for os clear or cls command. that's option doesn't works in pycharm, to use it compile the file to
exe file or run in linux terminal with the command python or python3.
if you wish to compile the file to exe use this:
https://pyinstaller.org/en/stable/ make sure you type the commands in pycharm terminal.
And time for sleep function that allows the user to see the prompt before returning to the previous menu.
"""
"""
Welcome to my SV supermarket program.
In this program we can make a database of products by categories, mange costumer cart.
We can add a product to any category we already made, we must create the category first.
We can add category or delete category, prints products by category.
We can Delete a product, Change product name, Update product details and Show products.
We can Add product to cart, Remove product from cart, Show cart total sum, and total sum include 17% tax
and show all cart items include sum, and total sum include 17% tax

In my super program there no free items, price item that insert as .3 will be 0.3 that's due to python rules.
If you decided to add or remove item quantity you must do it. if you regret do it and then do the opposite operation.
When updating a product the values change both in product's details and in cart items details.

If you want to examine the program faster you can use that database just copy and past below global variables define:
products = [{'ID': 132, 'Category': 'meat', 'Name': 'antrikot', 'Calories': 50.0, 'Proteins': 50.0, 'Price': 50.0},
            {'ID': 111, 'Category': 'meat', 'Name': 'sinta', 'Calories': 1231321.0, 'Proteins': 21.0, 'Price': 12.0}]
categories = ["meat", "dairy"]
ids = [132, 111]
names = ["antrikot", "sinta"]
cart_items = [{'ID': 111, 'Name': 'sinta', 'Price': 12.0, 'Quantity': 20, 'Total Price': 240.0},
              {'ID': 132, 'Name': 'antrikot', 'Price': 50.0, 'Quantity': 15, 'Total Price': 750.0}]
cart_names = ['sinta', 'antrikot']
cart_ids = [111, 132]

I hope that you will enjoy!
"""

"""
Global variables define
products is a list of dictionaries for each product there is dictionary with the keys: ID, Category, Name, Calories,
Proteins and Price.  
categories is a list with categories names.
ids is a list of all products ID's. For better indexing later.
names is a list of all products names. For better indexing later.
cart_items is a list of dictionaries for each product there is dictionary with the keys: ID, Name, Price, Quantity,
Total and Price.
cart_names is a list of all cart products names. For better indexing later.
cart_ids is a list of all cart products names. For better indexing later.
"""
products = []
categories = []
ids = []
names = []
cart_items = []
cart_names = []
cart_ids = []

"""
adding_category function adding a category only if it not exist. or exit the function if nothing typed.
"""


def adding_category():
    global categories
    while True:
        new_category = input("Please enter a category name or press enter to go back:")
        if new_category == "":
            print("No category added, bye!")
            sleep(5)
            return
        elif new_category not in categories:
            categories.append(new_category)
            print("Category added")
            sleep(5)
            break
        else:
            print("Category already exist, no category added")
            continue


"""
delete_category function deletes category only if it exist and empty.
If it not exist it shows the categories that exist. if it not empty there is a prompt that says that, and nothing change
"""


def delete_category():
    global categories
    global products
    while True:
        category_input = input("Enter category name:")
        if category_input == "":
            print("Category name cant be empty, bye!")
            sleep(5)
            return
        elif category_input not in categories:
            print("This category doesn't exist")
            show_categories()
            return
        else:
            b = False
            for product in products:
                if product["Category"] == category_input:
                    b = True
            if b:
                print("This category have product(s), remove all product(s) first.")
                print("You can print all product(s) in the category by the menu")
                print("Nothing changed")
                sleep(5)
                return
            else:
                categories.remove(category_input)
                print("Category deleted successfully")
                sleep(5)
                return


"""
print_products_by_category function prints products in desired category.
if the category doesn't exist or empty the functions says that.
"""


def print_products_by_category():
    global categories
    global products
    while True:
        category_input = input("Enter category name:")
        if category_input == "":
            print("Category name cant be empty, bye!")
            sleep(5)
            return
        elif category_input not in categories:
            print("This category doesn't exist")
            sleep(5)
            show_categories()
            return
        else:
            b = False
            for product in products:
                if product["Category"] == category_input:
                    b = True
            if b:
                print(f"Those are the products in {category_input} category:")
                for product in products:
                    if product["Category"] == category_input:
                        print("")
                        print("ID : ", product["ID"])
                        print("Name : ", product["Name"])
                sleep(10)
                return
            else:
                print(f"The category {category_input} is empty")
                sleep(5)
                return


# show_categories function shows the categories that exist, if there no categories the function sys that.


def show_categories():
    global categories
    if not categories:
        print("There is no categories yet, you can add a category from the menu")
        sleep(5)
    else:
        print("Those are the categories that exist:")
        for category in categories:
            print(category)
        sleep(5)


"""
adding_product function add a new product with values to the keys: ID, Category, Name, Calories, Proteins and Price.
The function have value check for errors. if there is a problem with the value the function says what is the problem.
"""


def adding_product(category):
    global products
    global ids
    global names
    new_product = {}
    print("Lets add a new product")
    while True:
        try:
            id_input = int(input("Enter product ID:"))
            if id_input < 0:
                print("Product ID can't be negative number")
                continue
            elif id_input not in ids:
                ids.append(id_input)
                new_product["ID"] = id_input
            else:
                print("This ID already Exist")
                continue
        except ValueError:
            print("Product ID must be an integer")
            continue
        else:
            break
    new_product["Category"] = category
    while True:
        name_input = input("Enter product name:")
        if name_input == "":
            print("Product name can't be empty")
            continue
        elif name_input not in names:
            names.append(name_input)
            new_product["Name"] = name_input
            break
        else:
            print("This product name already Exist")
            continue
    while True:
        try:
            cal = float(input("Enter calories value:"))
            if cal <= 0:
                print("Calories value can't be negative or zero")
                continue
            else:
                new_product["Calories"] = cal
                break
        except ValueError:
            print("Please enter a number not a string")
            continue
    while True:
        try:
            proteins = float(input("Enter proteins value:"))
            if proteins <= 0:
                print("Calories value can't be negative or zero")
                continue
            else:
                new_product["Proteins"] = proteins
                break
        except ValueError:
            print("Please enter a number not a string")
            continue
    while True:
        try:
            price = float(input("Enter product price:"))
            if price <= 0:
                print("Product price must be grater then 0")
                continue
            else:
                new_product["Price"] = price
        except ValueError:
            print("Please enter a number not a string")
            continue
        else:
            break
    products.append(new_product)
    print("Product added")
    sleep(5)


"""
updating_product_by_name function updates values of product keys: ID, Category, Name, Calories, Proteins and Price.
The function get the product name from the calling function update_product_menu
The function have value check for errors. if there is a problem with the value the function says what is the problem.
When finishing updating the user can exit the function.
"""


def updating_product_by_name(product_name):
    global products
    global ids
    global names
    global categories
    global cart_items
    if product_name not in names:
        print(f"There in no such product with the name: {product_name}")
        sleep(5)
    else:
        for item in products:
            if item["Name"] == product_name:
                while True:
                    print("Changeable values are (product ID can't change):")
                    print("1.Category")
                    print("2.Product name")
                    print("3.Calories")
                    print("4.Proteins")
                    print("5.Price")
                    print("6.I dont want to change anything, Go back")
                    uv = input("Value number that you want to update is:")
                    if uv == "1":
                        while True:
                            category_input = input("Enter new category name:")
                            if category_input not in categories:
                                print("This category doesn't exist")
                                show_categories()
                                continue
                            elif category_input == item["Category"]:
                                print("This is already the category, nothing changed")
                                break
                            else:
                                item["Category"] = category_input
                                print("Product category changed successfully")
                                break
                    elif uv == "2":
                        while True:
                            name_input = input("Enter new product name:")
                            if name_input not in names:
                                names.append(name_input)
                                names.remove(item["Name"])
                                for citem in cart_items:
                                    if citem["Name"] == item["Name"]:
                                        citem["Name"] = name_input
                                item["Name"] = name_input
                                print("Product name changed successfully")
                                break
                            else:
                                print("This product name already exist")
                                continue
                    elif uv == "3":
                        while True:
                            try:
                                cal = float(input("Enter new calories value:"))
                                if cal <= 0:
                                    print("Calories value can't be negative or zero")
                                    continue
                                else:
                                    item["Calories"] = cal
                                    print("Product calories changed successfully")
                                    break
                            except ValueError:
                                print("Please enter a number not a string")
                                continue
                    elif uv == "4":
                        while True:
                            try:
                                proteins = float(input("Enter new proteins value:"))
                                if proteins <= 0:
                                    print("Calories value can't be negative or zero")
                                    continue
                                else:
                                    item["Proteins"] = proteins
                                    print("Product proteins changed successfully")
                                    break
                            except ValueError:
                                print("Please enter a number not a string")
                                continue
                    elif uv == "5":
                        while True:
                            try:
                                price = float(input("Enter new product price:"))
                                if price <= 0:
                                    print("Product price must be grater then 0")
                                    continue
                                else:
                                    item["Price"] = price
                                    for citem in cart_items:
                                        if citem["Name"] == item["Name"]:
                                            citem["Price"] = item["Price"]
                                            citem["Total Price"] = citem["Price"] * citem["Quantity"]
                                    print("Product price changed successfully")
                            except ValueError:
                                print("Please enter a number not a string")
                                continue
                            else:
                                break
                    elif uv == "6":
                        print("Going back")
                        sleep(5)
                        return
                    else:
                        print("This is not an option, Try again")
                        continue


"""
updating_product_by_id function updates values of product keys: ID, Category, Name, Calories, Proteins and Price.
The function get the product ID from the calling function update_product_menu
The function have value check for errors. if there is a problem with the value the function says what is the problem.
When finishing updating the user can exit the function.
"""


def updating_product_by_id(product_id):
    global products
    global ids
    global names
    global categories
    global cart_items
    if product_id not in ids:
        print(f"There in no such product with the ID {product_id}")
        sleep(5)
    else:
        for item in products:
            if item["ID"] == product_id:
                while True:
                    print("Changeable values are (product ID can't change):")
                    print("1.Category")
                    print("2.Product name")
                    print("3.Calories")
                    print("4.Proteins")
                    print("5.Price")
                    print("6.I dont want to change anything, Go back")
                    uv = input("Value number that you want to update is:")
                    if uv == "1":
                        while True:
                            category_input = input("Enter new category name:")
                            if category_input not in categories:
                                print("This category doesn't exist")
                                show_categories()
                                continue
                            elif category_input == item["Category"]:
                                print("This is already the category, nothing changed")
                                break
                            else:
                                item["Category"] = category_input
                                print("Product category changed successfully")
                                break
                    elif uv == "2":
                        while True:
                            name_input = input("Enter new product name:")
                            if name_input not in names:
                                names.append(name_input)
                                names.remove(item["Name"])
                                for citem in cart_items:
                                    if citem["Name"] == item["Name"]:
                                        citem["Name"] = name_input
                                item["Name"] = name_input
                                print("Product name changed successfully")
                                break
                            else:
                                print("This product name already Exist")
                                continue
                    elif uv == "3":
                        while True:
                            try:
                                cal = float(input("Enter new calories value:"))
                                if cal <= 0:
                                    print("Calories value can't be negative or zero")
                                    continue
                                else:
                                    item["Calories"] = cal
                                    print("Product calories changed successfully")
                                    break
                            except ValueError:
                                print("Please enter a number not a string")
                                continue
                    elif uv == "4":
                        while True:
                            try:
                                proteins = float(input("Enter new proteins value:"))
                                if proteins <= 0:
                                    print("Calories value can't be negative or zero")
                                    continue
                                else:
                                    item["Proteins"] = proteins
                                    print("Product proteins changed successfully")
                                    break
                            except ValueError:
                                print("Please enter a number not a string")
                                continue
                    elif uv == "5":
                        while True:
                            try:
                                price = float(input("Enter new product price:"))
                                if price <= 0:
                                    print("Product price must be grater then 0")
                                    continue
                                else:
                                    item["Price"] = price
                                    for citem in cart_items:
                                        if citem["Name"] == item["Name"]:
                                            citem["Price"] = item["Price"]
                                            citem["Total Price"] = citem["Price"] * citem["Quantity"]
                                    print("Product price changed successfully")
                            except ValueError:
                                print("Please enter a number not a string")
                                continue
                            else:
                                break
                    elif uv == "6":
                        print("Going back")
                        sleep(5)
                        return
                    else:
                        print("This is not an option, Try again")
                        continue


"""
update_product_menu function is a menu to choose how to update a product. by name or ID.
The function have value check for errors. if there is a problem with the value the function says what is the problem.
The function have option to go back to previous menu.
"""


def update_product_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Product Update Menu")
        print("")
        print("Please Choose an option")
        print("1.Update by product name")
        print("2.Update by product ID")
        print("3.Go back")
        dpmo = input("Chosen option number is:")
        if dpmo == "1":
            p_name = input("Enter product name:")
            if p_name == "":
                print("Product name cant be empty, try again")
                sleep(5)
                continue
            else:
                updating_product_by_name(p_name)
        elif dpmo == "2":
            while True:
                try:
                    p_id = int(input("Enter product ID:"))
                    if p_id < 0:
                        print("Product ID can't be negative number")
                        continue
                    else:
                        updating_product_by_id(p_id)
                except ValueError:
                    print("Product ID must be an integer")
                    continue
                else:
                    break
        elif dpmo == "3":
            break
        else:
            print("This is not an option, try again...")
            sleep(5)
            continue


"""
delete_product_by_name function removes product for the database by name.
The function get the name from calling function delete_product_menu.
If the item doesn't exist the function says that.
If item exist in cart the item will not remove from there. We sell everything we can, nothing goes to garbage.
"""


def delete_product_by_name(product_name):
    global products
    global names
    global ids
    if product_name not in names:
        print(f"There in no such product with the name: {product_name}")
        sleep(5)
    else:
        for item in products:
            if item["Name"] == product_name:
                products.remove(item)
                names.remove(product_name)
                ids.remove(item["ID"])
                print(f"The product {product_name} deleted")
                sleep(5)
                break
            else:
                continue


"""
delete_product_by_id function removes product for the database by ID.
The function get the ID from calling function delete_product_menu.
If the item doesn't exist the function says that.
If item exist in cart the item will not remove from there. We sell everything we can, nothing goes to garbage.
"""


def delete_product_by_id(product_id):
    global products
    global ids
    global names
    if product_id not in ids:
        print(f"There in no such product with the ID {product_id}")
        sleep(5)
    else:
        for item in products:
            if item["ID"] == product_id:
                products.remove(item)
                ids.remove(product_id)
                names.remove(item["Name"])
                print(f"The product {product_id} deleted")
                sleep(5)
                break
            else:
                continue


"""
change_product_name change the name of a product. the function gets two names. original name and new name.
The parameters checks occurred in the calling function. so only if the original name exist the function is being called.
The function changes the name of the product also in the cart item if it exist there.
"""


def change_product_name(oproduct_name, rproduct_name):
    global products
    global names
    global cart_items
    for item in products:
        if item["Name"] == oproduct_name:
            for citem in cart_items:
                if citem["Name"] == item["Name"]:
                    citem["Name"] = rproduct_name
            item["Name"] = rproduct_name
            names.remove(oproduct_name)
            names.append(rproduct_name)
            print(f"The product name {oproduct_name} changed to {rproduct_name}")
            sleep(5)
            break
        else:
            continue


"""
delete_product_menu is function that lets us to choose if we want to delete a product by name or by ID
The function also checks for some errors while inputs value for the right deleting function.
we have also an option to go back.
"""


def delete_product_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" Delete product menu")
        print("")
        print("Please Choose an option")
        print("1.Delete by product name")
        print("2.Delete by product ID")
        print("3.Go back")
        dpmo = input("Chosen option number is:")
        if dpmo == "1":
            p_name = input("Enter product name:")
            if p_name == "":
                print("Product name cant be empty, Nothing changed")
                sleep(5)
                continue
            else:
                delete_product_by_name(p_name)
        elif dpmo == "2":
            while True:
                try:
                    p_id = int(input("Enter product ID:"))
                    if p_id < 0:
                        print("Product ID can't be negative number")
                        continue
                    else:
                        delete_product_by_id(p_id)
                except ValueError:
                    print("Product ID must be an integer")
                    continue
                else:
                    break
        elif dpmo == "3":
            break
        else:
            print("This is not an option, try again...")
            sleep(5)
            continue


"""
products_menu is a function that shows all available operations on products.
The available operations are: Add a product, Delete a product, Change product name, Update product and Show products.
There is other option to go back to previous menu.
The function also inputs values for some of the functions. and check for value errors. if error exist it says.
There is option to go back to previous menu.
"""


def products_menu():
    global categories
    global names
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Products menu")
        print("")
        print("Please choose an option")
        print("1.Add a product")
        print("2.Delete a product")
        print("3.Change product name")
        print("4.Update product")
        print("5.Show products")
        print("6.Go back")
        pmo = input("Chosen option number is:")
        if pmo == "1":
            cat = input("Please enter a category to add the item:")
            if cat == "":
                print("Category name can't be empty, bye!")
                sleep(5)
                continue
            elif cat not in categories:
                print(f"There is no such category {cat}, No item added.")
                print("Add the category from the category menu if you wish to add category")
                sleep(5)
                continue
            else:
                adding_product(cat)
        elif pmo == "2":
            delete_product_menu()
        elif pmo == "3":
            oproduct_name = input("Please enter original product name:")
            if oproduct_name == "":
                print("Product name can't be empty, Nothing changed")
                sleep(5)
                continue
            elif oproduct_name not in names:
                print(f"There in no such product with the name: {oproduct_name}")
                continue
            rproduct_name = input("Please enter new product name:")
            if rproduct_name == "":
                print("Product name can't be empty, Nothing changed")
                sleep(5)
                continue
            elif oproduct_name == rproduct_name:
                print("Its the same name, Nothing changed")
                sleep(5)
                continue
            else:
                change_product_name(oproduct_name, rproduct_name)
        elif pmo == "4":
            update_product_menu()
        elif pmo == "5":
            show_products()
        elif pmo == "6":
            break
        else:
            print("This is not an option, try again...")
            sleep(5)
            continue


"""
show_products function shows all the products that exist in the database.
If there is no products the function says that.
"""


def show_products():
    os.system('cls' if os.name == 'nt' else 'clear')
    global products
    if not products:
        print("There is no products yet, create them by the menu. \n"
              "Don't forget to add the category first if its not exist")
        sleep(5)
        return
    else:
        print("The products that exist are:")
        print("")
        for item in products:
            for key in item:
                print(key, ":", item[key])
                print("")
        while True:
            back = input("Type back and press enter to go back")
            if back == "back":
                print("Good Job! Bye Bye :-)")
                sleep(5)
                break
            else:
                print("I told you to type back, not some thing else. Going back any way XD")
                sleep(5)
                break


"""
add_to_cart_by_name adding product to cart by product name.the function gets the name from 
calling function add_product_to_cart_menu.
If the product not  exist at all. the function says that.
If the product exist butt not in cart. the function. add it to cart with the keys:
ID, Name, Price, Quantity and Total Price.
The function check the value of quantity that inputs from us for errors.
If the product exist in cart we must add quantity. if we regret we have to use remove product functions.
"""


def add_to_cart_by_name(product_name):
    global products
    global names
    global cart_items
    global cart_names
    global cart_ids
    new_cart_item = {}
    if product_name not in names:
        print(f"There in no such product with the name: {product_name}")
        sleep(5)
    else:
        for item in products:
            if item["Name"] == product_name:
                if item["Name"] not in cart_names and item["ID"] not in cart_ids:
                    cart_names.append(item["Name"])
                    cart_ids.append(item["ID"])
                    new_cart_item["ID"] = item["ID"]
                    new_cart_item["Name"] = item["Name"]
                    new_cart_item["Price"] = item["Price"]
                    while True:
                        try:
                            quantity = int(input("Enter product quantity:"))
                            if quantity <= 0:
                                print("Product quantity must be grater then 0")
                                continue
                            else:
                                new_cart_item["Quantity"] = quantity
                        except ValueError:
                            print("Please enter a integer number not a string or float number")
                            continue
                        else:
                            break
                    new_cart_item["Total Price"] = new_cart_item["Price"] * new_cart_item["Quantity"]
                    cart_items.append(new_cart_item)
                    print(f"The product {product_name} added")
                    sleep(5)
                    return
                else:
                    print("Product exist in cart, want to add quantity?")
                    for item_in_cart in cart_items:
                        if item_in_cart["Name"] == product_name:
                            while True:
                                try:
                                    quantity = int(input("Enter product quantity to add:"))
                                    if quantity <= 0:
                                        print("Product quantity must be grater then 0")
                                        continue
                                    else:
                                        item_in_cart["Quantity"] = item_in_cart["Quantity"] + quantity
                                        print("New quantity is: ", item_in_cart["Quantity"])
                                        item_in_cart["Total Price"] = item_in_cart["Price"] * item_in_cart[
                                            "Quantity"]
                                        sleep(5)
                                except ValueError:
                                    print("Please enter a integer number not a string or float number")
                                    continue
                                else:
                                    break
                        else:
                            continue


"""
add_to_cart_by_id adding product to cart by product ID. the function gets the ID from 
calling function add_product_to_cart_menu.
If the product not  exist at all. the function says that.
If the product exist butt not in cart. the function. add it to cart with the keys:
ID, Name, Price, Quantity and Total Price.
The function check the value of quantity that inputs from us for errors.
If the product exist in cart we must add quantity. if we regret we have to use remove product functions.
"""


def add_to_cart_by_id(p_id):
    global products
    global ids
    global cart_items
    global cart_names
    global cart_ids
    new_cart_item = {}
    if p_id not in ids:
        print(f"There in no such product with the ID {p_id}")
        sleep(5)
    else:
        for item in products:
            if item["ID"] == p_id:
                if item["Name"] not in cart_names and item["ID"] not in cart_ids:
                    cart_names.append(item["Name"])
                    cart_ids.append(item["ID"])
                    new_cart_item["ID"] = item["ID"]
                    new_cart_item["Name"] = item["Name"]
                    new_cart_item["Price"] = item["Price"]
                    while True:
                        try:
                            quantity = int(input("Enter product quantity:"))
                            if quantity <= 0:
                                print("Product quantity must be grater then 0")
                                continue
                            else:
                                new_cart_item["Quantity"] = quantity
                        except ValueError:
                            print("Please enter a integer number not a string or float number")
                            continue
                        else:
                            break
                    new_cart_item["Total Price"] = new_cart_item["Price"] * new_cart_item["Quantity"]
                    cart_items.append(new_cart_item)
                    print(f"The product {p_id} added")
                    sleep(5)
                    return
                else:
                    print("Product exist in cart, want to add quantity?")
                    for item_in_cart in cart_items:
                        if item_in_cart["ID"] == p_id:
                            while True:
                                try:
                                    quantity = int(input("Enter product quantity to add:"))
                                    if quantity <= 0:
                                        print("Product quantity must be grater then 0")
                                        continue
                                    else:
                                        item_in_cart["Quantity"] = item_in_cart["Quantity"] + quantity
                                        print("New quantity is: ", item_in_cart["Quantity"])
                                        item_in_cart["Total Price"] = item_in_cart["Price"] * item_in_cart[
                                            "Quantity"]
                                        sleep(5)
                                except ValueError:
                                    print("Please enter a integer number not a string or float number")
                                    continue
                                else:
                                    break
                        else:
                            continue


"""
add_product_to_cart_menu is a menu function that lets us choose between adding a product to cart by name or by ID.
The function checks foe some value errors.
There is option to go back to previous menu. 
"""


def add_product_to_cart_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Add product to cart menu")
        print("")
        print("Please Choose an option")
        print("1.Add by product name")
        print("2.Add by product ID")
        print("3.Go back")
        dpmo = input("Chosen option number is:")
        if dpmo == "1":
            p_name = input("Enter product name:")
            if p_name == "":
                print("Product name can't be empty, Nothing changed")
                sleep(5)
            else:
                add_to_cart_by_name(p_name)
        elif dpmo == "2":
            while True:
                try:
                    p_id = int(input("Enter product ID:"))
                    if p_id < 0:
                        print("Product ID can't be negative")
                        sleep(5)
                    else:
                        add_to_cart_by_id(p_id)
                except ValueError:
                    print("Product ID must be an integer")
                    continue
                else:
                    break
        elif dpmo == "3":
            break
        else:
            print("This is not an option, try again...")
            sleep(5)
            continue


"""
delete_product_from_cart_by_name delete product from cart by product name.the function gets the name from 
calling function remove_product_from_cart_menu.
If the product not  exist at all. the function says that.
If the product exist butt not in cart. the function. remove desired quantity or all the product from cart.
The function check the value of quantity that inputs from us for errors.
If the product exist in cart we must remove quantity at least. if we regret we have to use add product functions.
"""


def delete_product_from_cart_by_name(product_name):
    global cart_items
    global cart_ids
    global cart_names
    if product_name not in cart_names:
        print(f"There in no such product in cart with the name {product_name} in cart")
        sleep(5)
    else:
        for item in cart_items:
            if item["Name"] == product_name:
                q = item["Quantity"]
                while True:
                    try:
                        q_input = int(input(f"There is quantity of {q} how many to remove?"))
                        if q_input <= 0:
                            print("Quantity can't be negative or zero, try again")
                            continue
                        elif q_input > q:
                            print("That's too much, try again")
                            continue
                        elif 0 < q_input < q and q_input != q:
                            item["Quantity"] = item["Quantity"] - q_input
                            item["Total Price"] = item["Price"] * item["Quantity"]
                            print("New quantity is", item["Quantity"])
                            sleep(5)
                            return
                    except ValueError:
                        print("Please enter a integer number not a string or float number")
                    else:
                        if q_input == q:
                            cart_items.remove(item)
                            cart_ids.remove(item["ID"])
                            cart_names.remove(item["Name"])
                            print(f"The product {product_name} totally removed from cart")
                            sleep(5)
                            return
            else:
                continue


"""
delete_product_from_cart_by_id delete product from cart by product ID.the function gets the ID from 
calling function remove_product_from_cart_menu.
If the product not  exist at all. the function says that.
If the product exist butt not in cart. the function. remove desired quantity or all the product from cart.
The function check the value of quantity that inputs from us for errors.
If the product exist in cart we must remove quantity at least. if we regret we have to use add product functions.
"""


def delete_product_from_cart_by_id(product_id):
    global cart_items
    global cart_ids
    global cart_names
    if product_id not in cart_ids:
        print(f"There in no such product in cart with the ID {product_id} in cart")
        sleep(5)
    else:
        for item in cart_items:
            if item["ID"] == product_id:
                q = item["Quantity"]
                while True:
                    try:
                        q_input = int(input(f"There is quantity of {q} how many to remove?"))
                        if q_input <= 0:
                            print("Quantity can't be negative or zero, try again")
                            continue
                        elif q_input > q:
                            print("That's too much, try again")
                            continue
                        elif 0 < q_input < q and q_input != q:
                            item["Quantity"] = item["Quantity"] - q_input
                            item["Total Price"] = item["Price"] * item["Quantity"]
                            print("New quantity is", item["Quantity"])
                            sleep(5)
                            return
                    except ValueError:
                        print("Please enter a integer number not a string or float number")
                    else:
                        if q_input == q:
                            cart_items.remove(item)
                            cart_ids.remove(product_id)
                            cart_names.remove(item["Name"])
                            print(f"The product {product_id} totally removed from cart")
                            sleep(5)
                            return
            else:
                continue


"""
remove_product_from_cart_menu is a menu function that lets us choose between removing a product to cart
by name or by ID.
The function checks foe some value errors.
There is option to go back to previous menu. 
"""


def remove_product_from_cart_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Remove product from cart menu")
        print("")
        print("Please Choose an option")
        print("1.Remove by product name")
        print("2.Remove by product ID")
        print("3.Go back")
        dpmo = input("Chosen option number is:")
        if dpmo == "1":
            p_name = input("Enter product name:")
            if p_name == "":
                print("Product name can't be empty, Nothing changed")
                sleep(5)
            else:
                delete_product_from_cart_by_name(p_name)
        elif dpmo == "2":
            while True:
                try:
                    p_id = int(input("Enter product ID:"))
                    if p_id < 0:
                        print("Product ID can't be negative")
                        sleep(5)
                    else:
                        delete_product_from_cart_by_id(p_id)
                    break
                except ValueError:
                    print("Product ID must be an integer")
                    continue
        elif dpmo == "3":
            break
        else:
            print("This is not an option, try again...")
            sleep(5)
            continue


# cart_sum function calculates the total sum of all the items in the cart


def cart_sum():
    csum = 0
    for item in cart_items:
        csum += item["Total Price"]
    return csum


"""
show_cart function shows the products that in the cart.
If the cart empty the function sys that.
The function shows also total sum and total sum include taxes.
"""


def show_cart():
    os.system('cls' if os.name == 'nt' else 'clear')
    global cart_items
    if not cart_items:
        print("Cart is empty")
        sleep(5)
    else:
        for item in cart_items:
            for key in item:
                print(key, ":", item[key])
                print("")
        csum = cart_sum()
        print(f"Cart total sum is: {csum}, cart total sum include 17% tax is: {csum * 1.17}")
        while True:
            back = input("Press enter or type something and then press enter to go back")
            if back == "":
                print("Good Job! Bye Bye :-)")
                sleep(5)
                break
            else:
                print("Good Job! Bye Bye :-)")
                sleep(5)
                break


"""
cart_menu shows menu to make operations in the cart the operations are:
Show products, Add product to cart, Remove product from cart, 
Show cart total sum and total sum include 17% tax,Show cart
There is option to go back to main menu.
"""


def cart_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Cart menu")
        print("")
        print("Please choose an option")
        print("1.Show products")
        print("2.Add product to cart")
        print("3.Remove product from cart")
        print("4.Show cart total sum, and total sum include 17% tax")
        print("5.Show cart")
        print("6.Back")
        cmoption = input("Chosen option number is:")
        if cmoption == "1":
            show_products()
        elif cmoption == "2":
            add_product_to_cart_menu()
        elif cmoption == "3":
            remove_product_from_cart_menu()
        elif cmoption == "4":
            csum = cart_sum()
            if csum == 0:
                print("Cart is empty so,")
            print(f"Cart total sum is: {csum}, cart total sum include 17% tax is: {csum * 1.17}")
            sleep(5)
            continue
        elif cmoption == "5":
            show_cart()
        elif cmoption == "6":
            break
        else:
            print("This is not an option, try again...")
            sleep(5)
            continue


"""
categories_menu shows menu to make operations on categories the operations are:
Add a category, Delete category, Show categories, Print products by category.
There is option to go back to main menu.
"""


def categories_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Categories menu")
        print("")
        print("Please choose an option")
        print("1.Add a category")
        print("2.Delete category")
        print("3.Show categories")
        print("4.Print products by category")
        print("5.Back")
        cmo = input("Chosen option number is:")
        if cmo == "1":
            adding_category()
        elif cmo == "2":
            delete_category()
        elif cmo == "3":
            show_categories()
        elif cmo == "4":
            print_products_by_category()
        elif cmo == "5":
            break
        else:
            print("This is not an option, try again...")
            sleep(5)
            continue


"""
This is the main menu of the program. let us choose between menus in the program. the option are:
Categories menu, Products menu, Cart menu and exit the program.
"""


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Main menu")
    print("")
    print("Please choose an option")
    print("1.Categories menu")
    print("2.Products menu")
    print("3.Cart menu")
    print("4.Exit")
    option = input("Chosen option number is:")
    if option == "1":
        categories_menu()
    elif option == "2":
        products_menu()
    elif option == "3":
        cart_menu()
    elif option == "4":
        print("Bye, it was nice to meet you :-D")
        sleep(5)
        break
    else:
        print("This is not an option, try again...")
        sleep(5)
        continue
