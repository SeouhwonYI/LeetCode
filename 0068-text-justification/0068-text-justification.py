class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # line: words, width: length of words
        res = []
        line, width = [], 0

        for w in words:
            if width + len(w) + len(line) > maxWidth:
                # maxWidth - width: affordable space number / give blank 1 2 3 -> 1 2 3 -> 1
                for i in range(maxWidth - width): line[i % (len(line) - 1 or 1)] += ' '
                res.append(''.join(line))
                line, width = [], 0
            line += [w]
            width += len(w)
        
        # last line : just one blank between words
        res.append(' '.join(line).ljust(maxWidth))
        return res
            

