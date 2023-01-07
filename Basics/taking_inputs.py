name = input("Please enter your name: ")  # taking string input
integer = int(input("Please enter your integer: "))  # taking integer input

# this one automatically determines the type of the variable
evaluated_element = eval(
    input("Please enter your element: ")
)  # taking evaluated element input

if __name__ == "__main__":
    # if we give integer it will print the <class 'int'>, if float then <class 'float'> and so on
    print(type(evaluated_element))
    print(integer)
    print(f"My name is {name}")
    print("My name is {}".format(name))
