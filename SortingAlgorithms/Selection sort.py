# *** Сортировка выбором ***
# Следующее решение «в лоб» — каждый раз искать минимальный элемент и ставить его в начало.
# Звучит уже интереснее.

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
for i in range(len(array)):
    idx_min = i
    for j in range(i+1, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:
        array[i], array[idx_min] = array[idx_min], array[i]
print(array)
# На каждом шаге мы имеем отсортированную (слева) и неотсортированную часть (справа).
# Ищется минимальный элемент в неотсортированной части и меняется местами с элементом
# в начале неотсортированной части.
# И так продолжается, пока не закончится внешний цикл.


# Модификация описанного алгоритма для сортировки по убыванию.
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
for i in range(len(array)):
    idx_max = i
    for j in range(i+1, len(array)):
        if array[j] > array[idx_max]:
            idx_max = j
    if i != idx_max:
        array[i], array[idx_max] = array[idx_max], array[i]
print(array)