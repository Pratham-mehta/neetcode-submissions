# Ideas:
# Initialize empty stack
# Initialize the hashmap with a tracker values like:
    # '(', ')', '{', '}', '[' and ']'.
# Loop the whole string 
#   check the condition if the top of the stack is same 
#       as the tracker, then pop it or else return 
#           False
#  At the end of the loop, append the values, if all 
#       the condition fails

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        tracker = {")":"(", "]":"[","}":"{"}

        for char in s:
            if char in tracker:
                if stack and stack[-1] == tracker[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False
                
        