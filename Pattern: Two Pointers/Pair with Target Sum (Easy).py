def pair_with_target_sum(arr, target_sum):  # array IS sorted, so we can use two pointer for O(N) time complexity
    l, r = 0, len(arr) - 1
    while l < r:
        cur_sum = arr[l] + arr[r]
        if cur_sum > target_sum:
            r += -1
        elif cur_sum < target_sum:
            l += 1
        else:
            return [l, r]
    return [-1, -1]
