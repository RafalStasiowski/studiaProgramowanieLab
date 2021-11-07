def return_numbers_multiplied_by_2(numbers: list) -> list:
    return_list = list()
    for number in numbers:
        return_list.append(number*2)
    return return_list


def return_numbers_multiplied_by_2_lista_skladana(numbers: list) -> list:
    return [number * 2 for number in numbers]

lista_testowa = [10,5,2,4,7]

print(return_numbers_multiplied_by_2(lista_testowa))
print(return_numbers_multiplied_by_2_lista_skladana(lista_testowa))