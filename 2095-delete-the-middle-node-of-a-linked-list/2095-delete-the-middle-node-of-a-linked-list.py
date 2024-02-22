# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = ListNode(0,head)
        slow = temp
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        return temp.next
            
