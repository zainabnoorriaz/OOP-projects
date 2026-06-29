import json
class Product :
    def __init__(self,name,quantity,price) :
        self.name = name
        self.quantity = quantity
        self.price = price

    def sell_products(self, requested_amount) :

        if self.quantity >= requested_amount:
            self.quantity -= requested_amount
            print(f"{requested_amount} {self.name}(s) was sold.")
            print(f"Remaining stock is {self.quantity}")
        else :
            print("Not enough Quantity. Please Restock")

    def restock_products (self, restocked_products):
        self.quantity += restocked_products
        print(f"{restocked_products} {self.name}(s) have been restocked. New quantity is {self.quantity}")

    def to_dict(self) :
        return {
            "name" : self.name,
            "quantity" : self.quantity,
            "price" : self.price
        }

def save_products(products) :
    data = []
    for p in products:
        data.append(p.to_dict())

    with open("products.json", "w") as file:
        json.dump(data,file)

def load_prodcuts():
    products = []
    try:

      with open ("products.json", "r") as file:
        data = json.load(file)

      for item in data :
        product = Product(
            item["name"],
            item["quantity"],
            item["price"]
        )
        products.append(product)
    except FileNotFoundError:
        pass

    return products

products = load_prodcuts()
while True: 
 print("______MENU______")
 print("1. Add Product")
 print("2. Sell product")
 print("3. Restock Product")
 print("4. View all products")
 print("5. Exit program")

 choice = input("Enter your choice:")

 if choice == '1' :
    name = input("Enter the name of the product: ")
    quantity = int(input("Enter the quantity of the product: "))
    price = int(input("Enter the price of the product: "))
    new_product = Product(name,quantity,price)
    products.append(new_product)
    save_products(products)
    print("Product added successfully")

 elif choice == '2':
    name = input("Enter product name: ")

    selected_product = None

    for p in products:
        if p.name == name:
            selected_product = p
            break

    if selected_product:
        quantity = int(input("Enter quantity to sell: "))
        selected_product.sell_products(quantity)
        save_products(products)

    else:
        print("Product not found")

 elif choice == '3':
    name = input("Enter product name: ")

    selected_product = None

    for p in products:
        if p.name == name:
            selected_product = p
            break

    if selected_product:
        quantity = int(input("Enter quantity to restock: "))
        selected_product.restock_products(quantity)
        save_products(products)

    else:
        print("Product not found")

 elif choice == '4' :
    for p in products :
        print(f"{p.name} | {p.quantity} | {p.price}" )

 elif choice == '5' :
    print("Exiting the program")
    break

