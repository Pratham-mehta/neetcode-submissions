class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # Step 1: Initialize the set (also de-duplicates)
        longest = 0

        for num in num_set:  # Step 2: Scan every distinct number
            # Step 3: Only start counting from a true sequence start
            if num - 1 not in num_set:
                length = 1
                # Step 4: Count forward while the next number exists
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest