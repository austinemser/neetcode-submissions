class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if(len(s) != len(t)):
            return False

        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        for c2 in t:
            if c2 in d:
                d[c2] -= 1
                if d[c2] < 0:
                    return False
            else:
                return False

        return True