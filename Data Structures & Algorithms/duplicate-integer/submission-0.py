class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val = set()
        # length = len(nums)
        for num in nums:

            if num in val:
                return True
            
            val.add(num)
        
        return False

