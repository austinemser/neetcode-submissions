class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left < right:
            nL = numbers[left]
            nR = numbers[right]

            if nL + nR == target:
                return [left+1, right+1]

            if nL + nR > target:
                right -= 1
                continue

            if nL + nR < target:
                left += 1

        