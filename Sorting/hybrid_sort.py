# Params: 
# arr: array 
# s: threshold for inserstion sort (see readme)
# key: initial number of key comparisons
def hybrid_sort(arr, s, key):
    if len(arr) < s:
        return insertion_sort(arr, key)

    # Find mid of array
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_keys, left = hybrid_sort(left, s, key)
    right_keys, right = hybrid_sort(right, s, key)

    key += left_keys
    key += right_keys

    merge_keys, arr = merge(left, right, key)
    
    return key, arr


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


def insertion_sort(arr, key):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            key += 1
            # Swap if next element is smaller than prev
            if arr[j] < arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

    return key, arr
