class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        maps = {}
        for i in range(2, 8):
            maps[str(i)] = [chr(91 + 3*i + j) for j in range(3)]
        maps[str(7)].append('s')
        maps[str(8)] = ["t", "u", "v"]
        maps[str(9)] = ["w", "x", "y", "z"]
        
        result = [""]
        for c in digits:
            new = [[tmp + alp for tmp in result] for alp in maps[c]]
            result = []
            for lst in new:
                result.extend(lst)
        
        return result
                

