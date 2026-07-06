# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Algorithm to Solve this
# 1. Initialize 2 pointers like Prev and Curr
# 2. Traverse the LL
# 3. Save the Next Node : So inside the Loop, lookout for the next node and save it in temp
    # temp = curr.next (Storing the Address Reference)
# 4. Reverse the Pointer to Backwards
# 5. Update Head and Tail Address
# 6. Return Head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            temp = curr.next

            # Reverse the pointer
            curr.next = prev

            # Update the Head and Tail
            prev = curr
            curr = temp

        return prev

        











        