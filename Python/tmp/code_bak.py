def sum_num(arr):
    if arr == []:
        return 0

    return arr[0] + sum_num(arr[1:])


sums = sum_num([1, 2, 3])
print(sums)


def count_number(arr):
    if arr == []:
        return 0
    return 1 + count_number(arr[1:])


numbers = count_number([1, 2, "x", 6])
print(numbers)


def max_item(arr):
    if arr == []:
        return 0
    return arr[0] if arr[0] > max_item(arr[1:]) else max_item(arr[1:])


max_num = max_item([1, 10, 3, 4, 8, 19, 2, 7])
print(max_num)


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        small_list = [i for i in arr[1:] if i <= pivot]
        great_list = [i for i in arr[1:] if i > pivot]

        return quicksort(small_list) + [pivot] + quicksort(great_list)


quick_sort = quicksort([1, 4, 9, 3, 22, 89, 43, 67, 7])
print(quick_sort)
