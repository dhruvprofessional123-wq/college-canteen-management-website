# ============================================================
#             ABC COLLEGE CANTEEN
#          OFFLINE COMMAND LINE SYSTEM
# ============================================================

import os
from datetime import datetime


# ============================================================
# MENU
# ============================================================

menu = {
    1: ("Samosa", 20),
    2: ("Vada Pav", 25),
    3: ("Veg Sandwich", 40),
    4: ("Masala Maggi", 50),
    5: ("Veg Noodles", 60),
    6: ("Cheese Burger", 70),
    7: ("French Fries", 60),
    8: ("Tea", 15),
    9: ("Cold Coffee", 50),
    10: ("Cold Drink", 30)
}


# ============================================================
# CART
# ============================================================

cart = {}


# ============================================================
# CLEAR SCREEN
# ============================================================

def clear_screen():

    os.system("cls" if os.name == "nt" else "clear")


# ============================================================
# HEADER
# ============================================================

def header():

    print("=" * 60)
    print("              ABC COLLEGE CANTEEN")
    print("=" * 60)
    print("          Fresh Food • Affordable Prices")
    print("=" * 60)


# ============================================================
# SHOW MENU
# ============================================================

def show_menu():

    clear_screen()

    header()

    print()
    print("FOOD MENU")
    print("-" * 60)

    print(f"{'No.':<6}{'Food Item':<30}{'Price':>10}")
    print("-" * 60)

    for number, item in menu.items():

        name, price = item

        print(
            f"{number:<6}"
            f"{name:<30}"
            f"₹{price:>8}"
        )

    print("-" * 60)


# ============================================================
# ADD FOOD
# ============================================================

def add_food():

    show_menu()

    try:

        choice = int(
            input("\nEnter food number: ")
        )

        if choice not in menu:

            print("\n❌ Invalid food number.")
            input("\nPress Enter to continue...")
            return

        quantity = int(
            input("Enter quantity: ")
        )

        if quantity <= 0:

            print("\n❌ Quantity must be greater than 0.")
            input("\nPress Enter to continue...")
            return

        if choice in cart:

            cart[choice] += quantity

        else:

            cart[choice] = quantity

        name, price = menu[choice]

        print(
            f"\n✅ {quantity} x {name} "
            f"added to cart."
        )

    except ValueError:

        print("\n❌ Please enter a valid number.")

    input("\nPress Enter to continue...")


# ============================================================
# VIEW CART
# ============================================================

def view_cart():

    clear_screen()

    header()

    print()
    print("YOUR CART")
    print("-" * 60)

    if not cart:

        print("Your cart is empty.")

        input("\nPress Enter to continue...")
        return

    print(
        f"{'Food Item':<25}"
        f"{'Qty':<10}"
        f"{'Price':<10}"
        f"{'Total':>10}"
    )

    print("-" * 60)

    grand_total = 0

    for number, quantity in cart.items():

        name, price = menu[number]

        total = price * quantity

        grand_total += total

        print(
            f"{name:<25}"
            f"{quantity:<10}"
            f"₹{price:<9}"
            f"₹{total:>9}"
        )

    print("-" * 60)

    print(
        f"{'GRAND TOTAL':<45}"
        f"₹{grand_total:>9}"
    )

    print("-" * 60)

    input("\nPress Enter to continue...")


# ============================================================
# REMOVE FOOD
# ============================================================

def remove_food():

    if not cart:

        clear_screen()

        header()

        print("\nYour cart is empty.")

        input("\nPress Enter to continue...")
        return

    view_cart()

    try:

        choice = int(
            input("\nEnter food number to remove: ")
        )

        if choice not in cart:

            print("\n❌ That item is not in your cart.")

            input("\nPress Enter to continue...")
            return

        quantity = int(
            input("Enter quantity to remove: ")
        )

        if quantity <= 0:

            print("\n❌ Invalid quantity.")

            input("\nPress Enter to continue...")
            return

        cart[choice] -= quantity

        if cart[choice] <= 0:

            del cart[choice]

        print("\n✅ Cart updated.")

    except ValueError:

        print("\n❌ Please enter a valid number.")

    input("\nPress Enter to continue...")


# ============================================================
# CALCULATE TOTAL
# ============================================================

def calculate_total():

    total = 0

    for number, quantity in cart.items():

        name, price = menu[number]

        total += price * quantity

    return total


# ============================================================
# PLACE ORDER
# ============================================================

def place_order():

    clear_screen()

    header()

    if not cart:

        print("\n❌ Your cart is empty.")

        input("\nPress Enter to continue...")
        return

    print("\nORDER DETAILS")
    print("-" * 60)

    student_name = input(
        "Enter student name: "
    )

    roll_number = input(
        "Enter roll number: "
    )

    print("\nYour Order")
    print("-" * 60)

    grand_total = calculate_total()

    for number, quantity in cart.items():

        name, price = menu[number]

        total = price * quantity

        print(
            f"{name} "
            f"x {quantity} "
            f"= ₹{total}"
        )

    print("-" * 60)

    print(
        f"TOTAL AMOUNT: ₹{grand_total}"
    )

    print("-" * 60)

    confirm = input(
        "\nConfirm order? (y/n): "
    ).lower()

    if confirm != "y":

        print("\n❌ Order cancelled.")

        input("\nPress Enter to continue...")
        return

    order_time = datetime.now().strftime(
        "%d-%m-%Y %I:%M %p"
    )

    print("\n")
    print("=" * 60)
    print("              ORDER CONFIRMED")
    print("=" * 60)

    print(f"Student : {student_name}")
    print(f"Roll No : {roll_number}")
    print(f"Time    : {order_time}")

    print("-" * 60)

    for number, quantity in cart.items():

        name, price = menu[number]

        total = price * quantity

        print(
            f"{name} x {quantity} = ₹{total}"
        )

    print("-" * 60)

    print(
        f"TOTAL: ₹{grand_total}"
    )

    print("=" * 60)

    print("\n🍴 Please collect your order from")
    print("   the college canteen counter.")

    print("\nThank you for ordering!")

    cart.clear()

    input("\nPress Enter to continue...")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        clear_screen()

        header()

        print()
        print("MAIN MENU")
        print("-" * 60)

        print("1. View Food Menu")
        print("2. Add Food to Cart")
        print("3. View Cart")
        print("4. Remove Food from Cart")
        print("5. Place Order")
        print("6. Exit")

        print("-" * 60)

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            show_menu()

            input("\nPress Enter to continue...")

        elif choice == "2":

            add_food()

        elif choice == "3":

            view_cart()

        elif choice == "4":

            remove_food()

        elif choice == "5":

            place_order()

        elif choice == "6":

            clear_screen()

            print("=" * 60)
            print("       THANK YOU FOR VISITING")
            print("          ABC COLLEGE CANTEEN")
            print("=" * 60)

            break

        else:

            print(
                "\n❌ Invalid choice. "
                "Please select 1-6."
            )

            input("\nPress Enter to continue...")


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":

    main()