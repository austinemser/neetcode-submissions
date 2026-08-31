class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        d2 = {}
        if(len(s) != len(t)):
            return False

        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1

            if t[i] in d2:
                d2[t[i]] += 1
            else:
                d2[t[i]] = 1
                
        return d2 == d

        # for c in s:
        #     if c in d:
        #         d[c] += 1
        #     else:
        #         d[c] = 1

        # for c2 in t:
        #     if c2 in d:
        #         d[c2] -= 1
        #         if d[c2] < 0:
        #             return False
        #     else:
        #         return False

        # return True