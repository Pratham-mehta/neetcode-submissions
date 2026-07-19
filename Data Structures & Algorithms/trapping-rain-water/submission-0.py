class Solution:
    def trap(self, height: list[int]) -> int:
        # Edge Case: If the array is empty, we can't trap any water. 
        # This also prevents an IndexError when initializing the R pointer.
        if not height:
            return 0
            
        L, R = 0, len(height) - 1
        max_L, max_R = height[L], height[R]
        res = 0
        
        while L < R:
            # Step 3, 4: The left side is strictly the bottleneck. 
            # We don't care how tall the middle gets, we KNOW water here is capped by max_L.
            if max_L < max_R:
                L += 1
                # Update the left wall memory if we step on a taller block
                max_L = max(max_L, height[L])
                # Add trapped water (if we are on a peak, max_L - height[L] will just be 0)
                res += max_L - height[L]
                
            # Step 1, 2: The right side is the bottleneck (or they are tied).
            # Water here is completely capped by max_R.
            else:
                R -= 1
                # Update the right wall memory if we step on a taller block
                max_R = max(max_R, height[R])
                # Add trapped water
                res += max_R - height[R]
                
        return res