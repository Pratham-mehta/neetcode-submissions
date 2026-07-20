class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: If s1 is larger than s2, it's physically impossible.
        if len(s1) > len(s2):
            return False
            
        # Since we only have lowercase English letters, an array of size 26 is faster than a dict
        count_s1 = [0] * 26
        window_count = [0] * 26
        
        # Pre-compute the target frequencies for s1
        for c in s1:
            count_s1[ord(c) - ord('a')] += 1
            
        L = 0
        # Step 2: Expand the window across s2
        for R in range(len(s2)):
            
            # Add the new character to our window's frequency map
            window_count[ord(s2[R]) - ord('a')] += 1
            
            # Step 3: Shrink if the physical size exceeds len(s1)
            if R - L + 1 > len(s1):
                window_count[ord(s2[L]) - ord('a')] -= 1
                L += 1
                
            # Step 4: Record/Check if the window is exactly the right size
            if R - L + 1 == len(s1):
                # If the frequency maps match, we found a permutation!
                if count_s1 == window_count:
                    return True
                    
        return False