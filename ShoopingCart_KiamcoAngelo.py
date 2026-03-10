class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, price):
        self.cart[item] = price
        print(item, "added to cart.")

    def remove_item(self, item):
        if item in self.cart:
            del self.cart[item]
            print(item, "removed from cart.")
        else:
            print("Item not found in cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("\nItems in your cart:")
            for item, price in self.cart.items():
                print(item, "- ₱", price)

    def checkout(self):
        total = sum(self.cart.values())
        print("\nTotal amount: ₱", total)
        print("Thank you for shopping!")


mycart = ShoppingCart()

while True:
    print("\nShopping Cart Menu")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        price = float(input("Enter price: "))
        mycart.add_item(item, price)

    elif choice == "2":
        item = input("Enter item name to remove: ")
        mycart.remove_item(item)

    elif choice == "3":
        mycart.view_cart()

    elif choice == "4":
        mycart.checkout()

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")