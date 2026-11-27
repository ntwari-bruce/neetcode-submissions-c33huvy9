import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    min_heap = []
    result = []
    for item in heap:
        heapq.heappush(min_heap, item)
    
    while min_heap:
        result.append(heapq.heappop(min_heap))
    
    return result


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
