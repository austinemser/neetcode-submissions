class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:  
                d[num] = 1
        
        sorted_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True)) 
        list_keys = list(sorted_dict.keys())

        arr = []
        for i in range(k):
            arr.append(list_keys[i])

        return arr