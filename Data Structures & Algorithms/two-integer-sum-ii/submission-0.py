class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        L = 0
        R = len(numbers) - 1
        
        while L < R:
            current_sum = numbers[L] + numbers[R]
            
            if current_sum > target:
                # Steps 1 & 2: Sum is too large, move right pointer left
                R -= 1
            elif current_sum < target:
                # Sum is too small, move left pointer right
                L += 1
            else:
                # Step 3: Target found! Return 1-indexed positions
                return [L + 1, R + 1]
                
        return []
