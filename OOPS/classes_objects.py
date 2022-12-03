class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


    def get_animal_details(self): # method
        return f'{self.name} {self.species}'


if __name__ == '__main__':
    a = Animal("randy", "dog")  # a is an instance of Animal class
    print(a.get_animal_details()) # a is calling a method


