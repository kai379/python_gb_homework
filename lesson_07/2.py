# Сортировка слиянием

# Дробление
def merge_sort(array_of_num):
    if len(array_of_num) == 1:
        return array_of_num
    middle = len(array_of_num) // 2
    left = merge_sort(array_of_num[:middle])
    right = merge_sort(array_of_num[middle:])

    i = j = 0
    sort_array = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sort_array.append(left[i])
            i += 1
        else:
            sort_array.append(right[j])
            j += 1

    while i < len(left):
        sort_array.append(left[i])
        i += 1

    while j < len(right):
        sort_array.append(right[j])
        j += 1

    return sort_array


array = [5, 15, 2, 87, 62, 10, 4, 25, 18, 91, 0, 3]
print(merge_sort(array))
