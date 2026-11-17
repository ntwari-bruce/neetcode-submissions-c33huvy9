class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_bar = 0
        right_bar = len(heights) - 1
        max_area = 0

        while left_bar < right_bar:
            length = right_bar - left_bar
            width = min(heights[left_bar], heights[right_bar])
            area = length * width
            max_area = max(max_area, area)
            if heights[left_bar] < heights[right_bar]:
                left_bar += 1
            elif heights[left_bar] > heights[right_bar]:
                right_bar -= 1
            else:
                left_bar += 1
                right_bar -= 1
        
        return max_area

        