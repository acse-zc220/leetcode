#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
	def removeElements(self, head, val):
		"""
		:type head: ListNode
		:type val: int
		:rtype: ListNode
		"""
		
		dummy = ListNode(float('-inf'))
		dummy.next = head
		previous, current =dummy, dummy.next
		
		while current:
			if current.val == val:
				previous.next = current.next
			else:
				previous = current
			current = current.next
			
		return dummy.next