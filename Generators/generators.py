# generates the numbers which are even or divisible by 2
def generate_even_numbers(num_list):
    for num in num_list:
        if num % 2 == 0:
            yield num


if __name__ == '__main__':
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
    geneated_num = generate_even_numbers(num_list)

    print(next(geneated_num)) # gives output 2
    print(next(geneated_num)) # gives output 4


    #shorter version for generator
    even_nums = (num for num in num_list if num % 2 == 0)
    print(next(even_nums))  # gives output 2
    print(next(even_nums)) # gives output 4