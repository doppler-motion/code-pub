# 快速排序
def quick_sort(array, left, right):
    if left > right:
        return

    low = left
    high = right
    basenum = array[low]
    while low < high:
        while low < high and array[high] >= basenum:
            high -= 1
        while low < high and array[low] < basenum:
            low += 1
        if low < high:
            array[low], array[high] = array[high], array[low]
    array[left] = array[low]
    array[low] = basenum
    quick_sort(array, left, low - 1)
    quick_sort(array, low + 1, right)


if __name__ == "__main__":
    arr_list = [1, 2, 34, 78, 90, 21, 45, 38, 298]
    print("快速排序前数组：", arr_list)
    quick_sort(arr_list, 0, len(arr_list) - 1)
    print("快速排序后数组：", arr_list)
