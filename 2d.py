def print_every_second_number(numbers: list) -> None:
    for idx, number in enumerate(numbers):
        if not ((idx+1) % 2) :
            print(number)


test_list = [10,5,23,12,532,12,153,511]

print_every_second_number(test_list)