import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    return heapq.nsmallest(1, arr)[0]

def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    smallest_4 = heapq.nsmallest(4, arr)
    smallest_4.sort()
    return smallest_4
    

def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    smallest_2 = heapq.nsmallest(2, arr)

    reversed_elements = sorted(smallest_2, reverse=True)

    return reversed_elements


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

