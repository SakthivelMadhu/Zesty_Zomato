import json

# Menu Management
def display_menu(menu):
    print("----- MENU -----")
    for dish in menu:
        print(f"Dish ID: {dish['id']}")
        print(f"Name: {dish['name']}")
        print(f"Price: {dish['price']}")
        print(f"Availability: {'Yes' if dish['available'] else 'No'}")
        print("----------------")

def add_dish(menu):
    dish_id = input("Enter the dish ID: ")
    dish_name = input("Enter the dish name: ")
    dish_price = float(input("Enter the dish price: "))
    dish_available = input("Is the dish available? (yes/no): ").lower() == "yes"

    new_dish = {
        "id": dish_id,
        "name": dish_name,
        "price": dish_price,
        "available": dish_available
    }

    menu.append(new_dish)
    print("Dish added to the menu.")

def remove_dish(menu):
    dish_id = input("Enter the dish ID to remove: ")
    for dish in menu:
        if dish['id'] == dish_id:
            menu.remove(dish)
            print("Dish removed from the menu.")
            return
    print("Dish not found in the menu.")

def update_availability(menu):
    dish_id = input("Enter the dish ID to update availability: ")
    for dish in menu:
        if dish['id'] == dish_id:
            dish['available'] = not dish['available']
            print("Availability updated.")
            return
    print("Dish not found in the menu.")

# Order Management
def take_order(menu, orders):
    customer_name = input("Enter customer name: ")
    order_dishes = input("Enter dish IDs (comma-separated): ").split(",")

    order_exists = False
    for dish_id in order_dishes:
        for dish in menu:
            if dish['id'] == dish_id.strip() and dish['available']:
                order_exists = True
                break

    if order_exists:
        order_id = len(orders) + 1
        new_order = {
            "id": order_id,
            "customer_name": customer_name,
            "dishes": order_dishes,
            "status": "received"
        }
        orders.append(new_order)
        print(f"Order taken successfully. Order ID: {order_id}")
    else:
        print("Invalid dish ID or dish not available.")

def update_order_status(orders):
    order_id = int(input("Enter the order ID to update status: "))
    for order in orders:
        if order['id'] == order_id:
            print("1. Preparing")
            print("2. Ready for pickup")
            print("3. Delivered")
            status_choice = input("Enter the new status (1/2/3): ")
            if status_choice == "1":
                order['status'] = "preparing"
            elif status_choice == "2":
                order['status'] = "ready for pickup"
            elif status_choice == "3":
                order['status'] = "delivered"
            else:
                print("Invalid status choice.")
            print("Status updated.")
            return
    print("Order not found.")

def review_orders(orders):
    print("----- ORDERS -----")
    for order in orders:
        print(f"Order ID: {order['id']}")
        print(f"Customer Name: {order['customer_name']}")
        print(f"Dishes: {', '.join(order['dishes'])}")
        print(f"Status: {order['status']}")
        print("------------------")

def calculate_total_price(menu, order):
    total_price = 0
    for dish_id in order['dishes']:
        for dish in menu:
            if dish['id'] == dish_id:
                total_price += dish['price']
                break
    return total_price

# Data Persistence (Extra Adventure)
def save_data(menu, orders):
    data = {
        "menu": menu,
        "orders": orders
    }
    with open("data.json", "w") as file:
        json.dump(data, file)

def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        return data["menu"], data["orders"]
    except FileNotFoundError:
        return [], []

# Main Loop
def main():
    menu, orders = load_data()

    while True:
        print("1. Display Menu")
        print("2. Add Dish")
        print("3. Remove Dish")
        print("4. Update Dish Availability")
        print("5. Take Order")
        print("6. Update Order Status")
        print("7. Review Orders")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu(menu)
        elif choice == "2":
            add_dish(menu)
        elif choice == "3":
            remove_dish(menu)
        elif choice == "4":
            update_availability(menu)
        elif choice == "5":
            take_order(menu, orders)
        elif choice == "6":
            update_order_status(orders)
        elif choice == "7":
            review_orders(orders)
        elif choice == "8":
            save_data(menu, orders)
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
