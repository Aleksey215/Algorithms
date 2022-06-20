def recursive_binary_search(arr, target):
    # Задаем середину массива
    mid = len(arr) // 2
    # Если длина массива равна 1, то
    if len(arr) == 1:
        # возвращаем индекс среднего элемента
        return mid
    # а если средний элемент равен искомому, то
    elif arr[mid] == target:
        # возвращаем индекс среднего элемента
        return mid
    # иначе
    else:
        # если средний элемент меньше искомого, то
        if arr[mid] < target:
            # делаем рекурсивный вызов для левой половины исходного массива
            return recursive_binary_search(arr[mid:], target) + mid
        # иначе
        else:
            # рекурсивно вызываем поиск для правой половины
            return recursive_binary_search(arr[:mid], target)


arr = [10, 20, 30, 40, 50]
print(recursive_binary_search(arr, 20))