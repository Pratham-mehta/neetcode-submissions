class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        L = 0
        max_len = 0
    
        # Step 2: Expand the window
        for R in range(len(s)):
        
            # Step 3: If we hit a duplicate, shrink the window from the left 
            # until the duplicate is removed from our set.
            while s[R] in char_set:
                char_set.remove(s[L])
                L += 1
            
            # Add the new unique character and record the size
            char_set.add(s[R])
            max_len = max(max_len, R - L + 1)
        
        return max_len