def calculate_time(func):
    import time
    def time_calculation(a, b):
        start = time.time()
        result = func(a, b)
        end = time.time()
        print("The time taken by the function was %s"%(end-start))
        return result
    return time_calculation

@calculate_time
def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    result = add_numbers(5, 6)
    print("The result was %s"%(result))