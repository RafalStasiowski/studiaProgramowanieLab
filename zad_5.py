def zad5(lista: list, number: int) -> bool:
    return True if number in lista else False

test_list = [10,5,23,12,532,12,153,511]

print(zad5(test_list, 10))
print(zad5(test_list, 7))
