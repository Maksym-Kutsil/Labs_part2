def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        pivot_index = n // 2
        if n % 2 == 0:
            pivot_index -= 1
        pivot = arr[pivot_index]

    larger = []
    lower = []

    for i, el in enumerate(arr):
        if i != pivot_index:
            if el > pivot:
                larger.append(el)
            else:
                lower.append(el)
    return quick_sort(larger) + [pivot] + quick_sort(lower)


def find_kth_largest_el(arr, k):
    sorted_arr = quick_sort(arr)
    return (f"{k} найбільший елемент : {sorted_arr[k - 1]}, "
            f"індекс елементу в масиві : {arr.index(sorted_arr[k - 1])}")



