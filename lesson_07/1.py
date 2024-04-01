# Быстрая сортировка
def quick_sort(array):
    if len(array) <= 1:  # Базовый случай: когда останется один элемент
        return array
    else:
        first_element = array[0]
    less = [i for i in array[1:] if i <= first_element]  # Рекурсивный случай: проход без первого элемента
    more = [i for i in array[1:] if i > first_element]
    return quick_sort(less) + [first_element] + quick_sort(more)


print(quick_sort([4, 52, 17, 5, 28, 7, 10, 0, 49]))
