# Anagram => exact same characters as another 

# Sorting both of the Strings
# check if the sorted strings are equal

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False