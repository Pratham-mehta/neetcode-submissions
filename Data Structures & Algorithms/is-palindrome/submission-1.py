class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            # Step 3: Skip non-alphanumeric characters from the left
            while L < R and not self.alphaNum(s[L]):
                L += 1
            
            # Step 3: Skip non-alphanumeric characters from the right
            while L < R and not self.alphaNum(s[R]):
                R -= 1
                
            # Step 1 & 2: Compare characters (ignoring case)
            if s[L].lower() != s[R].lower():
                return False
                
            L += 1
            R -= 1
            
        # Step 4: Pointers met, it's a valid palindrome
        return True
        
    def alphaNum(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
