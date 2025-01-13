class Solution:
    def minimumLength(self, s: str) -> int:
        c_count = [0] * 26
        sol = 0

        for c in s:
            c_count[ord(c)-ord('a')] += 1

        for cnt in c_count:
            if cnt == 0:
                continue
            elif cnt % 2 == 0:
                sol += 2
            else:
                sol += 1

        return sol