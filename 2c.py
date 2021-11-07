def print_only_even_numbers(numbers: list) -> None:
    for number in numbers:
        if not number % 2:
            print(number)


test_list = [10,5,23,12,532,12,153]

print_only_even_numbers(test_list)