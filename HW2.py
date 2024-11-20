def largest_pair_sum(arr):

    if len(arr) < 2:
        return -1

    max1 = max2 = float('-inf')

    for num in arr:
        if num > max1:
            max1, max2 = num, max1
        elif num > max2:
            max2 = num

    return max1 + max2

