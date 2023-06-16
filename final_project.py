
import random

"""
Admin username = admin
Admin password = admin@123
"""


class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = str(random.randint(100, 500))
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

    def __repr__(self):
        return f"FoodItem({self.food_id}, {self.name}, {self.quantity}, {self.price}, {self.discount}, {self.stock})"


class Admin:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, food_item):
        self.food_items.append(food_item)

    def edit_food_item(self, food_id, new_food_item):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = new_food_item.name
                food_item.quantity = new_food_item.quantity
                food_item.price = new_food_item.price
                food_item.discount = new_food_item.discount
                food_item.stock = new_food_item.stock
                break
        else:
            print("Sorry! No matching food found with the given id")

    def view_food_items(self):
        return self.food_items

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                break


class User:
    def __init__(self, name, phone_number, email, address, password):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

    def view_profile(self):
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")

    def place_order(self, food_items):
        self.orders.append(food_items)

    def view_order_history(self):
        return self.orders

    def update_profile(
        self, new_name, new_phone_number, new_email, new_address, new_password
    ):
        self.name = new_name
        self.phone_number = new_phone_number
        self.email = new_email
        self.address = new_address
        self.password = new_password


# Login Options
def takeUserLoginSelection():
    print("1) Admin Login")
    print("2) User Login")
    print("3) Exit Application")
    user_input = input("Choose your option: ")
    return user_input


# Admin Login
def adminLogin():
    count = 0
    while count < 3:
        user_name = input("Enter the User Name:")
        password = input("Enter the Password:")
        if user_name == "admin" and password == "admin@123":
            print("Logged in as Admin")
            adminDashboard()
            break
        else:
            print("Wrong Username or Password. Try Again!")
            count += 1
    if count == 3:
        print("Too Many Unsuccessfull Attempts.")


# Admin Options
def adminOptions():
    print("1) Add new food item")
    print("2) View all food items")
    print("3) Edit food item")
    print("4) Remove a food item")
    print(
        "5) Log off"
    )  # An additional option to terminate the application whenever needed
    selected_option = input("Choose your option:")
    return selected_option


# Food Details
def askForFoodDetails():
    name = input("Enter the food name: ")
    quantity = input("Enter the food quantity: ")
    price = input("Enter the price: ")
    discount = input("Enter the discount: ")
    stock = input("Enter the amount of stock left in the restaurant: ")
    return name, quantity, price, discount, stock


# Admin Dashboard
def adminDashboard():
    admin = Admin()
    while True:
        try:
            selected_option = adminOptions()
            if int(selected_option) == 1:
                name, quantity, price, discount, stock = askForFoodDetails()
                food_item = FoodItem(name, quantity, price, discount, stock)
                admin.add_food_item(food_item)
            elif int(selected_option) == 2:
                print(admin.view_food_items())
            elif int(selected_option) == 3:
                food_id = input("Enter the food id to edit the food item: ")
                name, quantity, price, discount, stock = askForFoodDetails()
                new_food_item = FoodItem(name, quantity, price, discount, stock)
                admin.edit_food_item(food_id, new_food_item)
            elif int(selected_option) == 4:
                food_id = input("Enter the food id to remove the food item: ")
                admin.remove_food_item(food_id)
            elif int(selected_option) == 5:
                print("Loging off...")
                break

        except ValueError:
            print("Please Enter Valid Input")
            selected_option = adminOptions()


def userMenu():
    print("Tandoori Chicken (4 pieces) [INR 240]")
    print("Vegan Burger (1 Piece) [INR 320]")
    print("Truffle Cake (500gm) [INR 900]")


def userOptions():
    print("1) Place New Order")
    print("2) Order History")
    print("3) Update Profile")
    print("4) View Profile")
    print(
        "5) Log off"
    )  # An additional option to terminate the application whenever needed
    selected_option = input("Choose your option:")
    return selected_option


orders = []


def getOrders(order):
    global orders
    items = {"1": "Tandoori Chicken", "2": "Vegan Burger", "3": "Truffle Cake"}
    item = []
    for i in order:
        for j in i:
            item.append(items[j])
    orders.append(item)
    return orders


def userDashboard(user):
    user_order = []
    items = {"1": "Tandoori Chicken", "2": "Vegan Burger", "3": "Truffle Cake"}
    while True:
        try:
            selected_option = userOptions()

            if int(selected_option) == 1:
                if len(user_order) != 0:
                    print("Your Orders ", getOrders(user_order))
                userMenu()
                user_input = input("Enter a list of options separated by spaces: ")
                user_order = list(user_input.split(" "))
                user.place_order(user_order)
            elif int(selected_option) == 2:
                hist = user.view_order_history()
                if len(hist) == 0:
                    print("No orders to show")
                else:
                    for i in hist:
                        print("|", end="")
                        for j in i:
                            print(items[j], end=" | ")
                        print("\n*********")

            elif int(selected_option) == 3:
                new_name = input("Enter the full name: ")
                new_phone_number = input("Enter your personal mobile number: ")
                new_email = input("Enter your personal emial: ")
                new_address = input("Enter your address: ")
                new_password = input("Enter a password: ")
                user.update_profile(
                    new_name, new_phone_number, new_email, new_address, new_password
                )
            elif int(selected_option) == 4:
                user.view_profile()
                hist = user.view_order_history()
                print("Order History: ")
                if len(hist) == 0:
                    print("No orders to show")
                else:
                    for i in hist:
                        print("|", end="")
                        for j in i:
                            print(items[j], end=" | ")
                        print("\n*********")
            elif int(selected_option) == 5:
                print("Loging off...")
                break

        except ValueError:
            print("Please Enter Valid Input")
            selected_option = adminOptions()


def userLogin(user):
    print("Now please enter the valid credentials to login.")
    count = 0
    while count < 3:
        user_name = input("Enter the User Name:")
        password = input("Enter the Password:")
        if user_name == user.name and password == user.password:
            print(f"Logged in as {user.name}")
            userDashboard(user)
            break
        else:
            print("Wrong Username or Password. Try Again!")
            count += 1
    if count == 3:
        print("Too Many Unsuccessfull Attempts.")


def registerUser():
    full_name = input("Enter the full name: ")
    phone_number = input("Enter your personal mobile number: ")
    email = input("Enter your personal emial: ")
    address = input("Enter your address: ")
    password = input("Enter a password: ")
    user = User(full_name, phone_number, email, address, password)
    userLogin(user)


def main():
    while True:
        user_input = takeUserLoginSelection()
        try:
            if int(user_input) > 3 or int(user_input) < 1:
                print("Please Select one of the available options.")
            elif int(user_input) == 1:
                print("Logging in as Admin")
                adminLogin()
                break
            elif int(user_input) == 2:
                print("Complete the user registration")
                registerUser()
                break
            elif int(user_input) == 3:
                print("Exiting the Application.")
                break

        except ValueError:
            print("Please Enter Valid Input")
            user_input = takeUserLoginSelection()


if __name__ == "__main__":
    main()