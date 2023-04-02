import math


class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        left, right = 2, x // 2  # initialize pointers to 2, and half of x
        while left <= right:
            pivot = left + (right - left) // 2  # find midpoint element of the two pointers
            num = pivot * pivot  # check the square
            if num > x:  # if the square is greater than the target, decrease the right pointer
                right = pivot - 1
            elif num < x:  # if the square is less than the target, increase the left pointer
                left = pivot + 1
            else:  # the square is equal to the target, return the pivot point
                return pivot
        return right
