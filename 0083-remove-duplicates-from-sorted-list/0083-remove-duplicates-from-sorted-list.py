# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        while slow and slow.next:
            if slow.val == slow.next.val:
                slow.next = slow.next.next
            else:
                slow = slow.next
        return head