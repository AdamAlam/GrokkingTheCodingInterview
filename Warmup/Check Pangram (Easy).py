class Solution:
    def checkIfPangram(self, sentence):
        check_set = set()
        for char in sentence.lower():
            if char.isAlpha():
                check_set.add(char)

        return len(check_set) == 26
