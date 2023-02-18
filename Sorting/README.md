# Sorting
## Contents
1. Insertion sort (Python)
2. Merge sort (Python)
3. Hybrid sort (Python)

## Notes
Insertion sort, merge sort, and hybrid sort contains a component `key` which takes in the initial number of key comparisons. The return value of these 3 sorting functions is a pair of `key` and sorted `arr`.

### Hybrid sort
Hybrid sort is the implementation of a [merge-insertion sort](https://en.wikipedia.org/wiki/Merge-insertion_sort). A small integer `s` is set as a threshold for the size of subarrays. Once the size of a subarray in a recursive call of Mergesort is less than or equal to `s`, the algorithm will switch to Insertion Sort, which is efficient for small-sized input.

