# Define the menu of the restaurant
menu = {
    'Biryani': 800,
    'Chapli Kebab': 700,
    'Ras Malai': 500,
    'Chicken Sandwiches': 600,
    'Salad': 100,
}

# Greet the customer
print("Welcome to SHAH Restaurant")
print("Biryani: Rs 800\nChapli Kebab: Rs 700\nRas Malai: Rs 500\nChicken Sandwiches: Rs 600\nSalad: Rs 100")

order_total = 0

# Take first order
item = input("Enter the name of the item you want to order: ")

if item in menu:
    order_total += menu[item]
    print(f"Your item '{item}' has been added to your order.")
else:
    print(f"Sorry! The item '{item}' is not available yet.")

# Ask if they want to order more
another_order = input("Do you want to add another item? (Yes/No): ")

if another_order.strip().lower() == "yes":
    item_2 = input("Enter the name of the second item: ")
    
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2}' has been added to your order.")
    else:
        print(f"Sorry! The item '{item_2}' is not available.")

# Show total
print(f"\nThe total amount to pay is: Rs {order_total}")
