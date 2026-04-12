class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

    def rental_price(self, days):
        pass


class Car(Vehicle):
    def __init__(self, brand, model, seating):
        super().__init__(brand, model)
        self.seating = seating

    def rental_price(self, days):
        return days * 1000

    def show_details(self):
        super().show_details()
        print("Seating:", self.seating)


class Bike(Vehicle):
    def __init__(self, brand, model, cc):
        super().__init__(brand, model)
        self.cc = cc

    def rental_price(self, days):
        return days * 500

    def show_details(self):
        super().show_details()
        print("Engine CC:", self.cc)


# 🔥 Vehicles Data
vehicles = {
    "Car": {
        "c1": {"brand": "Toyota", "model": "Innova", "seating": 7},
        "c2": {"brand": "Honda", "model": "City", "seating": 5},
        "c3": {"brand": "Hyundai", "model": "Creta", "seating": 5},
        "c4": {"brand": "Maruti", "model": "Swift", "seating": 5},
        "c5": {"brand": "Tata", "model": "Nexon", "seating": 5},
        "c6": {"brand": "Mahindra", "model": "XUV700", "seating": 7},
        "c7": {"brand": "Kia", "model": "Seltos", "seating": 5},
        "c8": {"brand": "Skoda", "model": "Slavia", "seating": 5}
    },
    "Bike": {
        "b1": {"brand": "Yamaha", "model": "R15", "cc": 155},
        "b2": {"brand": "KTM", "model": "Duke 200", "cc": 200},
        "b3": {"brand": "Royal Enfield", "model": "Classic 350", "cc": 350},
        "b4": {"brand": "Bajaj", "model": "Pulsar 220", "cc": 220},
        "b5": {"brand": "TVS", "model": "Apache RTR 160", "cc": 160},
        "b6": {"brand": "Honda", "model": "Hornet 2.0", "cc": 184},
        "b7": {"brand": "Suzuki", "model": "Gixxer", "cc": 155},
        "b8": {"brand": "Kawasaki", "model": "Ninja 300", "cc": 296}
    }
}

# 🔽 Choose vehicle type
v_type = input("Enter vehicle type (Car/Bike): ")

if v_type in vehicles:

    print("\nAvailable vehicles:")
    for vid, details in vehicles[v_type].items():
        print(f"{vid} - {details['brand']} {details['model']}")

    choice = input("\nEnter vehicle ID: ").lower()

    if choice in vehicles[v_type]:
        data = vehicles[v_type][choice]

        try:
            days = int(input("Enter number of rental days: "))
        except ValueError:
            print("Invalid number")
            exit()

        if v_type == "Car":
            obj = Car(data["brand"], data["model"], data["seating"])
        else:
            obj = Bike(data["brand"], data["model"], data["cc"])

        print("\n--- Vehicle Details ---")
        obj.show_details()
        print("Rental Price:", obj.rental_price(days))

    else:
        print("Invalid vehicle ID")

else:
    print("Invalid vehicle type")
