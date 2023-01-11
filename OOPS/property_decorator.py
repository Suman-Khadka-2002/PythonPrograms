class Student:
    def __init__(self, name, address=None):
        self.name = name
        self.address = address

    @property
    def get_name(self):
        return f"{self.name} lives in {self.address}"



if __name__ == "__main__":
    s = Student("Hari", "Kathmandu")
    print(s.get_name)
    print(s.get_name()) # it will throw an error
