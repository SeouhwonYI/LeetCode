class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(word1: str, word2: str) -> bool:
            n1, n2 = len(word1), len(word2)
            if n1 > n2:
                return False
            return word2[:n1] == word1 and word2[-n1:] == word1

        cnt = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    cnt += 1

        return cnt