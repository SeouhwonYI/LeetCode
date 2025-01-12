class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        # 무조건 하나 따로 남음.
        if n % 2 != 0:
            return False

        open_count = 0
        for i in range(n):
            # open or closed(switchable)
            if s[i] == '(' or locked[i] == '0':
                open_count += 1
            # closed(locked)
            else:
                open_count -= 1
            # open이 많은 건 뒤에서 닫을 수 있지만, 
            # closed가 switchable 포함 계산해도 많으면 방법이 없음
            if open_count < 0:
                return False

        # 뒤에서부터
        close_count = 0
        for i in range(n - 1, -1, -1):
            # 뒤에서는 closed가 앞에서의 open 같은 느낌
            if s[i] == ')' or locked[i] == '0':
                close_count += 1
            else:
                close_count -= 1
            if close_count < 0:
                return False

        return True