
def bubbleSortPass(arr, start, end):

    if start == end:
        return
    

    if arr[start] > arr[start + 1]:
        arr[start], arr[start + 1] = arr[start + 1], arr[start]
    

    bubbleSortPass(arr, start + 1, end)


def bubbleSortRecursive(arr, n):

    if n == 1:
        return

    bubbleSortPass(arr, 0, n - 1)
    

    bubbleSortRecursive(arr, n - 1)


array = [64, 34, 25, 12, 22, 11, 90]
bubbleSortRecursive(array, len(array))
print("Sorted array:", array)
