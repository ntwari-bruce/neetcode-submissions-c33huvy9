class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # a naive solution of sorting frequencies and count
        freq = {}
        for num in nums:
            freq[num] =  1 + freq.get(num, 0)
        
        arr = []
        for num, count in freq.items():
            arr.append([count, num])
        
        # sort them in ascending order
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res

        