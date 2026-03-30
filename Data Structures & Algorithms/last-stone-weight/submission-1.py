class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # solve this using heaps
        minHeap = []
        for stone in stones:
            minHeap.append(-stone)
        
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            x = heapq.heappop(minHeap)
            y = heapq.heappop(minHeap)

            if x == y:
                continue
            else:
                y = -(y)
                x = -(x)

                new_stone = x - y
                heapq.heappush(minHeap, -new_stone)
        
        return -(minHeap[0]) if minHeap else 0

        