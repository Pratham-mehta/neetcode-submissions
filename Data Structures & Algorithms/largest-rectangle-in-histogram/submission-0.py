class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                prev_start, prev_height = stack.pop()
                width = i - prev_start
                max_area = max(max_area, prev_height * width)
                start = prev_start  # absorb this bar's leftward reach
            
            stack.append((start, h))

        for start, h in stack:
            width = len(heights) - start
            max_area = max(max_area, h * width)

        return max_area
