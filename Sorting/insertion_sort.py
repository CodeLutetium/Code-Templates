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