class Vehicle(object):

    Tax = 0.13

    def __init__(self, name, vehicle_type) -> None:
        self.name = name
        self.vehicle_type = vehicle_type

    def get_details(self):
        return f"{self.name} {self.vehicle_type}"
    
    @classmethod
    def update_tax(cls, new_tax):
        cls.Tax = new_tax


class Car(Vehicle):
    def __init__(self, name, vehicle_type, brand) -> None:
        super().__init__(name, vehicle_type)
        self.brand = brand

    def get_details(self):
        return super().get_details() + " " + self.brand


if __name__ == "__main__":

    c1 = Car("Avalon", "Car", "Toyota")
    details = c1.get_details()
    c1.update_tax(0.14)
    print(c1.Tax)
    print(details)
