def max_subarray_sum(arr):

    max_ending_here = 0  
    max_so_far = float('-inf')  
    
    for num in arr:

        max_ending_here = max(num, max_ending_here + num)

        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far


arr1 = [2, -1, -3, 4, -1, 2, 1, -5, 4]
arr2 = [1, 2, 3, -2, 5]

print("Maximum Subarray Sum for arr1:", max_subarray_sum(arr1))  # Output: 6
print("Maximum Subarray Sum for arr2:", max_subarray_sum(arr2))  # Output: 9
