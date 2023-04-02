class Solution:
    def reverseVowels(self, s):
        s = list(s)
        vowels = list("aeiou")
        left, right = 0, len(s) - 1
        while left < right:
            left_is_vowel = s[left].lower() in vowels
            right_is_vowel = s[right].lower() in vowels
            if left_is_vowel and right_is_vowel:
                s[left], s[right] = s[right], s[left]
                left += 1
                right += -1
                continue
            if not left_is_vowel:
                left += 1
            if not right_is_vowel:
                right += -1
        return "".join(s)


if __name__ == "__main__":
    solution = Solution()

    s1 = "hello"
    expected_output1 = "holle"
    actual_output1 = solution.reverseVowels(s1)
    print("Test Case 1: ", expected_output1 == actual_output1)

    s2 = "DesignGUrus"
    expected_output2 = "DusUgnGires"
    actual_output2 = solution.reverseVowels(s2)
    print("Test Case 2: ", expected_output2 == actual_output2)

    s3 = "AEIOU"
    expected_output3 = "UOIEA"
    actual_output3 = solution.reverseVowels(s3)
    print("Test Case 3: ", expected_output3 == actual_output3)

    s4 = "aA"
    expected_output4 = "Aa"
    actual_output4 = solution.reverseVowels(s4)
    print("Test Case 4: ", expected_output4 == actual_output4)

    s5 = ""
    expected_output5 = ""
    actual_output5 = solution.reverseVowels(s5)
    print("Test Case 5: ", expected_output5 == actual_output5)
