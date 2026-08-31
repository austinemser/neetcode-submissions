class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        answer = 1
        current = 1
        if len(s) == 0:
            return 0
        for i in range(1,len(s)):
            # if char not in s[l:r] answer = r - l
            # else
            # while char in s[l:r] && l<r
            # left++
            if s[i] not in s[left:i]:
                current = i - left + 1
            else:
                while s[i] in s[left:i]:
                    left+=1
                current = i - left + 1

            answer = max(answer, current)
            # print(i, left, s[i], s[left:i], current, answer)
        return answer