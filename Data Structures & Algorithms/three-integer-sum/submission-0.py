class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # Sort the array first

        for i, val in enumerate(nums):
            # Step 4: Skip duplicate values for the first element
            if i > 0 and val == nums[i - 1]:
                continue
            
            # Use Two Pointers for the remaining array
            L, R = i + 1, len(nums) - 1
            while L < R:
                three_sum = val + nums[L] + nums[R]
                
                if three_sum > 0:
                    # Step 5 logic: Sum is too large, move right pointer left
                    R -= 1
                elif three_sum < 0:
                    # Step 1 logic: Sum is too small, move left pointer right
                    L += 1
                else:
                    # Steps 2 & 3 logic: Triplet found! Save it and shrink window
                    res.append([val, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    
                    # Skip duplicate values for the inner left pointer to avoid identical triplets
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        return res
