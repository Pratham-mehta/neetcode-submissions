class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        L, R = 0, len(height) - 1
        
        while L < R:
            # Step 1, 2, 3: Calculate area of the current container
            width = R - L
            water_level = min(height[L], height[R])
            current_area = width * water_level
            max_area = max(max_area, current_area)
            
            # Step 1, 2, 3: Move the pointer pointing to the shorter line
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
                
        return max_area