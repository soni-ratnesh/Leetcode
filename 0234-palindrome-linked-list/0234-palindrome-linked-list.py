# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return None
        if head.next is None:
            return True
        
        slow, fast = head, head
        prev=None
        length = 1
        while fast.next and fast.next.next:
            fast = fast.next.next

            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

            length += 2
        if fast.next:
            length+=1

        if length%2:
            right = slow.next
            left = prev
        else:
            right = slow.next
            slow.next = prev
            left = slow
        
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        
        