class Car :
    def __init__(self, brand,color,fuel):
        self.brand = brand
        self.color = color
        self.fuel = fuel

    def start(self) :
        print(f"{self.brand}, {self.color} is starting")

    def drive (self) :
        if self.fuel >= 10:
            self.fuel -= 10
            print(f"Fuel left is {self.fuel}")
        else :
            print("Not enough fuel to drive")

    def refuel (self,amount) :
        if amount > 0 :
   
            self.fuel += amount
            print(f"Car is refueled. fuel is now {self.fuel}")

    def status (self) :
         print(f"{self.brand} | Fuel: {self.fuel}")

class ElectricCar(Car) :
    def __init__(self, brand,color,battery):
        super().__init__(brand,color,0)
        self.battery = battery

    def drive(self) :
        if self.battery >= 10 :
            self.battery -= 10
            print(f"Battery left {self.battery}")
        else :
            print("Not enough battery to drive")

    def charge(self, amount) :
        if amount > 0 :
       
            self.battery += amount
            if self.battery > 100:
                self.battery = 100
            print(f"Electric car is charged now. battery is {self.battery}")

    def status(self):
         print(f"{self.brand} | Battery: {self.battery}")

brand = input("enter the brand of the car:")
color = input("Enter the color of the car: ")
fuel = int(input("Enter the fuel of the car:"))
car1 = Car(brand, color,fuel)



brand = input("enter the brand of the Electric car:")
color = input("Enter the color of the Electric Car: ")
battery = int(input("Enter the battery of electic car"))
car2 = ElectricCar(brand,color,battery)

while True:
    print("1. Drive the car")
    print("2. Refuel the car")
    print("3. Drive the electric car")
    print("4. Charge the electric Car")
    print("5. Check status")
    print("6. Exit")

    choice = input ("Enter your choice: ")

    if choice == "1" :
            car1.drive()

    elif choice == "2":
            amount= int(input("Enter the amount to refuel:"))
            car1.refuel(amount)

    elif choice == "3":
            car2.drive()

    elif choice == "4":
            amount = int(input("Enter the amount to charge:"))
            car2.charge(amount)
        
    elif choice == "5" :
            car1.status()
            car2.status()
    
    elif choice == "6":
        print("Exiting program")
        break





    
