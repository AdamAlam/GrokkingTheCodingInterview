class Solution:
    # This algorithm uses one string to increment the count and one to decrement. If the words are anagrams, then the
    #     frequency of all character should be 0 after one pass.
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        char_frequency = {}
        for i in range(len(s)):
            if s[i] in char_frequency:
                char_frequency[s[i]] += 1
            else:
                char_frequency[s[i]] = 1

            if t[i] in char_frequency:
                char_frequency[t[i]] += -1
            else:
                char_frequency[t[i]] = -1

        return max(char_frequency.values()) == 0
