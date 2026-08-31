class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)

        for k, v in enumerate(nums):
            d[v].append(k)
        
        for num in nums:
            diff = target - num
            if diff in d:
                if len(d[diff]) > 1:
                     return d[diff]
                else:
                    if d[num][0] != d[diff][0]:
                        return [d[num][0], d[diff][0]]