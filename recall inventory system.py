import json
class Product :
    def __init__(self,name,quantity,price):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def sell(self,requested_quantity) :
        if self.quantity >= requested_quantity:
            self.quantity-=requested_quantity
            print(f"Now the remaining quantity is: {self.quantity} ")
        
        else :
            print("Not enough quantity. Please restock")

    def restock(self, restocked_amount) :
        self.quantity += restocked_amount

        print(f"Amount after restock is {self.quantity}")

    def to_dict (self) :
        return {
            "name" : self.name,
            "quantity" : self.quantity,
            "price" : self.price
        }
    
def save_products(products):
    data = []
    for p in products:
        data.append(p.to_dict())

    with open("products.json", "w") as file:
        json.dump(data, file)

def load_products():
    products = []
    try:
        with open("products.json", "r") as file :
          data = json.load(file)

        for item in data :
           product = Product(item["name"], item["quantity"], item["price"])
           products.append(product)
    except FileNotFoundError:
        pass

    return products

products = load_products()
while True :

    print("1. Add Products")
    print("2. Sell products")
    print("3. View products")
    print("4. Restock Products")
    print("5. Exit")

    choice = input("Enter your choice : ")

    if choice == '1':
        name = input("Enter the name of the product: ")
        quantity = int(input("Enter the quantity of the product: "))
        price = int(input("Enter the price of the product: "))
        new_product = Product(name,quantity,price)
        products.append(new_product)
        save_products(products)

        print("Product added successfully")

    elif choice == '2' :
        name = input("Enter the name of the product: ")
        selected_product = None

        for p in products :
            if p.name == name:
                selected_product = p
                break

        if selected_product:
            requested_amount = int(input("Enter the amount that you want: "))

            selected_product.sell(requested_amount)
            save_products(products)
        else :
            print("Product not found")

    elif choice == '3' :

            for product in products :
              print(f"{product.name} | {product.quantity}| {product.price}")

    elif choice == '4' :
        name = input("Enter the name of the product: ")
        selected_product = None

        for p in products :
            if p.name == name :
                selected_product = p
                break
        if selected_product:
            restocked_amount = int(input("Enter the amount to restock: "))
            selected_product.restock(restocked_amount)
            save_products(products)

        else :
            print("Product Not Found")


    elif choice == '5' :
        print("Exiting program")
        break

    else :
        print("Invalid choice")
    





  

