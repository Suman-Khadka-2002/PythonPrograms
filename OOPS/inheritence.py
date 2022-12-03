class Vehicle():
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand


    def get_details(self):
        return f"{self.name} {self.brand}"



class Car(Vehicle):
    pass



if __name__ == "__main__":
    c1 = Car("Sadan", "Maruti")
    print(c1.get_details())