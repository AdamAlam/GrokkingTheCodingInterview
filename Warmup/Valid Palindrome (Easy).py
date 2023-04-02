class Solution:
    def is_palindrome(self, s):
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            if s[right].isalpha() and s[left].isalpha():
                if s[right] != s[left]:
                    return False
                else:
                    left += 1
                    right += -1
                    continue
            if not s[left].isalpha():
                left += 1
            if not s[right].isalpha():
                right += -1
        return True
