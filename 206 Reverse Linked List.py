# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		#create dummy, dummy.next = None
		#staring from node.val=1
		#dummy.next head.next = head, dummy.next
		dummy = ListNode(float("-inf"))
		while head:
			dummy.next, head.next, head=head, dummy.next, head.next
		return dummy.next