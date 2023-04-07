def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        count += triplet_with_smaller_sum_helper(arr, target - arr[i], i)
    return count


def triplet_with_smaller_sum_helper(arr, target, left):
    middle, right = left + 1, len(arr) - 1
    pair_count = 0
    while middle < right:
        if arr[middle] + arr[right] < target:
            pair_count += right - middle
            middle += 1
        else:
            right += -1
    return pair_count


def triplet_with_smaller_sum_brute_force(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                cur_sum = arr[i] + arr[j] + arr[k]
                if cur_sum < target:
                    count += 1
                if k == j + 1 and cur_sum >= target:
                    return count

    return count
