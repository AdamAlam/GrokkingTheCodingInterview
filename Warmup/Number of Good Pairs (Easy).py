class Solution:
    def numGoodPairs(self, nums):
        pairCount = 0
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1  # If num is in frequency map, increment it, otherwise set it to 0
            pairCount += freq[num] - 1
        return pairCount
