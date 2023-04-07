def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_diff = float('inf')
    closest_sum = float('inf')
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            cur_sum = arr[i] + arr[left] + arr[right]
            cur_diff = target_sum - cur_sum
            if cur_diff == 0:
                return target_sum
            if abs(cur_diff) <= smallest_diff:
                if abs(cur_diff) == smallest_diff:
                    closest_sum = min(closest_sum, cur_sum)
                else:
                    closest_sum = cur_sum
                smallest_diff = abs(cur_diff)

            if cur_diff > 0:
                left += 1
            else:
                right += -1

    return closest_sum
