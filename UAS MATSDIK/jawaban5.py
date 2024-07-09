def insertion_sort(arr):
    """
    Fungsi untuk mengurutkan array menggunakan insertion sort.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def is_sorted(arr):
    """
    Fungsi untuk memeriksa apakah array sudah terurut.
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Base Case: Memeriksa list dengan satu elemen
base_case = [1]
print(f"Base case sorted: {is_sorted(insertion_sort(base_case))}")

# Inductive Step: Memeriksa beberapa list dengan n elemen
test_cases = [
    [1, 2, 3, 4, 5],          # sorted list
    [5, 4, 3, 2, 1],          # reverse sorted list
    [3, 1, 4, 1, 5, 9, 2, 6], # random list
    [],                       # empty list
    [7]                       # single element list
]

for case in test_cases:
    sorted_case = insertion_sort(case.copy())
    print(f"Original: {case}")
    print(f"Sorted: {sorted_case}")
    print(f"Is sorted: {is_sorted(sorted_case)}\n")
