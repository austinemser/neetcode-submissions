class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix = [1] * n
        postfix = [1] * n

        prefix[0] = nums[0]
        for i in range(n-1):
            prefix[i+1] = prefix[i] * nums[i+1]

        postfix[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]

        answer = [1] * n
        for i in range(n):
            left = 1 if i == 0 else prefix[i-1]
            right = 1 if i==n-1 else postfix[i+1]
            answer[i] = left * right
        
        return answer