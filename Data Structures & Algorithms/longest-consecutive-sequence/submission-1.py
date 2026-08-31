class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        numsSet = sorted(set(nums))
        longest = 1
        lastNum = numsSet[0]
        history = []
        for i in range(1, len(numsSet)):
            if lastNum == numsSet[i] - 1:
                longest += 1
            else:
                history.append(longest)
                longest = 1
            lastNum = numsSet[i]

        history.append(longest)

        return max(history)