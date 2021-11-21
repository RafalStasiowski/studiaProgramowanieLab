def zad6(lista1: list, lista2: list) -> list:
    return lista1 + list(set(lista2) - set(lista1))

first_list = [1, 2, 3, 5]
second_list = [2, 5, 7, 9]

print(zad6(first_list, second_list))