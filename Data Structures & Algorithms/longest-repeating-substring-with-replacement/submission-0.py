class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L = 0
        max_len = 0
        
        # Expand the window
        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            
            # Calculate current window size
            window_len = R - L + 1
            
            # Step 3: Shrink if replacements needed > k
            # (window length) - (count of most frequent character)
            while window_len - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1
                window_len = R - L + 1  # Update window length after shrinking
                
            # Record valid window
            max_len = max(max_len, window_len)
            
        return max_len