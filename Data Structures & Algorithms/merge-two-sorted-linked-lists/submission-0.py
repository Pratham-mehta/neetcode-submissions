# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode(-1)
        while list1 and list2:
            # compare between list1 val vs list2 val
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            # Update the tail pointer to the next 
            tail = tail.next

        # check the remaining elements if either list 1 or List 2 is exhausted
        tail.next = list1 or list2

        return dummy.next