class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        longest = 1
        lastNum = nums[0]
        history = []
        for i in range(1, len(nums)):
            if lastNum == nums[i] - 1:
                longest += 1
            elif lastNum != nums[i]:
                history.append(longest)
                longest = 1
            lastNum = nums[i]

        history.append(longest)

        return sorted(history, reverse=True)[0]