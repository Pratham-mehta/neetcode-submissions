class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        best_start = None
        for num in num_set:
            if num-1 not in num_set:
                length = 1
                while num+length in num_set:
                    length += 1
                if length > longest:
                    longest = length
                    best_start = num
        
        return list(range(best_start, best_start + longest))