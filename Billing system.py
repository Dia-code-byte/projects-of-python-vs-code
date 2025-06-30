

items = {
    "apple": 20,
    "banana": 10,
    "milk": 30,
    "bread": 25,
    "eggs": 5
}

cart = {}

print("Welcome to EasyPeasy Store 🛒")
print("Available items and prices (per unit):")
for item, price in items.items():
    print(f"- {item.title()}: ₹{price}")

while True:
    product = input("\nEnter the item to buy (or type 'done' to finish): ").lower()
    if product == "done":
        break
    elif product in items:
        qty = int(input(f"How many {product}s? "))
        cart[product] = cart.get(product, 0) + qty
    else:
        print("❌ Item not available. Please choose from the list.")


print("\n🧾 Your Bill:")
total = 0
for item, qty in cart.items():
    price = items[item] * qty
    total += price
    print(f"{item.title()} x {qty} = ₹{price}")

print(f"\nTotal Amount: ₹{total}")
print("🙏 Thank you for shopping with EasyPeasy Store!")
