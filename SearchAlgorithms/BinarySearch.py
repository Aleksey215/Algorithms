from random import randint


# *** Двоичный поиск ***
# Алгоритм двоичного поиска является более совершенным, чем линейный поиск,
# однако он накладывает на структуру сильное ограничение — она должна быть отсортирована.

# Допустим, что у нас стоит такая же задача — найти индекс определенного элемента в массиве.
# В связи с тем, что алгоритм может искать только в отсортированном массиве,
# используем генератор последовательных чисел range.
# Суть двоичного поиска сводится к тому, что на каждой итерации размер исследуемого массива уменьшается в 2 раза.


def binary_search(arr, elem, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if arr[middle] == elem:
        return middle
    elif elem < arr[middle]:
        return binary_search(arr, elem, left, middle - 1)
    else:
        return binary_search(arr, elem, middle + 1, right)


element = int(input("Enter element: "))
array = [i for i in range(1, 100)]
print(array)
print(binary_search(array, element, 0, 98))

# # Математически доказывается, что сложность такого алгоритма O(log(n)),
# # а как вы должны помнить из начала этого модуля — логарифмическая сложность намного лучше, чем линейная.
# # Ура! Мы получили очень эффективный алгоритм поиска. Только вот сортировать нужно…

a = [i for i in range(1, 10)]


# Альтернативный способ
def binary_search_2(arr, item):
    low = arr[0]
    high = arr[-1]
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == item:
            return middle
        elif arr[middle] > item:
            high = middle - 1
        else:
            low = middle + 1
    return f"Элемента {item} нет в списке"


print(binary_search_2(a, 7))
print(a)