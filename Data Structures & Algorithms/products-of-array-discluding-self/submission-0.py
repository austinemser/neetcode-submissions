class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * (len(nums))
        for i in range(len(nums)):
            num = 1
            for j in range(len(nums)):
                if(j == i):
                    continue
                num = num * nums[j]
            prefix[i] = num

        return prefix