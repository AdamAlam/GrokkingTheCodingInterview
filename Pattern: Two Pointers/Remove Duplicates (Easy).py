def remove_duplicates(arr):  # the array is sorted, so we can do this in constant space O(1)
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            arr.pop(i + 1)
            continue
        i += 1
    return len(arr)
