def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j +1], arr[j]
                swapped = True
                if not swapped:
                    break
    return arr
example_list = [5, 3, 8, 4, 2]
sorted_list = bubble_sort(example_list)
print("Sorted List:", sorted_list)