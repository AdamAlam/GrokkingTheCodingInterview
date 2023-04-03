class Solution:
    def shortestDistance(self, words, word1, word2):
        minDistance = len(words)
        pos1, pos2 = -1, -1
        for i, word in enumerate(words):
            if word == word1:
                pos1 = i
            elif word == word2:
                pos2 = i
            if -1 not in [pos1, pos2]:
                minDistance = min(minDistance, abs(pos2 - pos1))
        return minDistance
