class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ["a", "e", "i", "o", "u"]
        cnt = 0
        lst = []
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                cnt += 1
            lst.append(cnt)
        lst.append(0)
        
        sol = []
        for query in queries:
            sol.append(lst[query[1]]-lst[query[0]-1])
        return sol

