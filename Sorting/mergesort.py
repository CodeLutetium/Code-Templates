def merge_sort(arr, key):
    if len(arr) == 1:
        return key, arr
    
    # Find mid of array
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    key, left = merge_sort(left, key)
    key, right = merge_sort(right, key)

    return merge(left, right, key)

# np library req.
import numpy as np
def merge(left, right, key):
    out = np.zeros(len(left) + len(right), dtype=int)
    idx = l_idx = r_idx = 0
    
    while l_idx < len(left) and r_idx < len(right):
        # Compare elements
        key += 1
        # Case 1: element on left is smaller
        if left[l_idx] < right[r_idx]:
            out[idx] = left[l_idx]
            idx += 1
            l_idx += 1

        # Case 2: element on right is smaller
        elif left[l_idx] > right[r_idx]:
            out[idx] = right[r_idx]
            idx += 1
            r_idx += 1

        # Case 3: both elements are equal
        else: 
            out[idx] = out[idx+1] = left[l_idx]
            idx += 2
            l_idx += 1
            r_idx += 1

    # Check if both arrays are empty
    if l_idx == len(left):
        while r_idx < len(right):
            out[idx] = right[r_idx]
            idx += 1
            r_idx += 1

    elif r_idx == len(right):
        while l_idx < len(left):
            out[idx] = left[l_idx]
            idx += 1
            l_idx += 1

    return key, out