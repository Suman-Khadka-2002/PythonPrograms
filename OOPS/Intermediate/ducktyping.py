class Duck:
    def swim_fly(self):
        print("I am a duck and I can swim and fly")


class Goose:
    def swim_fly(self):
        print("I am a goose and I can swim and fly")


class Hippo:
    def walk(self):
        print("I am a hippo and I can swim but can't fly")


if __name__ == "__main__":
    for obj in Duck(), Goose(), Hippo():
        # it will fail for the Hippo object since it doesn't have swim_fly method
        obj.swim_fly()
