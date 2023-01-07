arr = []


def take_inputs_for_list(size):
    for i in range(size):
        arr.append(int(input()))


def append_to_list(element):
    arr.append(element)


def remove_from_list(element):
    arr.remove(element)


def remove_last_element_from_list():
    arr.pop()


def print_list():
    [print(element) for element in arr]


if __name__ == "__main__":
    size = eval(input("Enter the size of list: "))
    take_inputs_for_list(size)
    append_to_list(1)
    append_to_list(2)
    print(arr)
