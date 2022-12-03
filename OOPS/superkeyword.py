from datetime import datetime
class Animal:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species


class Dog(Animal):
    def __init__(self, name, species, birth_date) -> None:
        super().__init__(name, species)
        self.birth_date = birth_date
    
    def get_age(self):
        curr_age = datetime.now().year - int(self.birth_date) 
        return f"The current age of the dog is {curr_age}"

if __name__ == '__main__':
    d1 = Dog("sally", "japanese", "2019")

    age_of_dog = d1.get_age()
    print(age_of_dog)