class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 1. Initialize empty stack
        stack = []
        # Since it is a list, parse through each of it 
        for c in tokens:
            if c =="+":
                stack.append(stack.pop()+stack.pop())
            # Order matters for Subtraction and Division since 2nd Operator 
            # is given more preference
            elif c=="-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c=="*":
                stack.append(stack.pop()*stack.pop())
            elif c=="/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
            
        return stack[0]