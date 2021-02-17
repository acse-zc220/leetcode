#!/usr/bin/python

a={"123","123","1234"}
a.discard("123")
print(a)

class Solution(object):
	def intersection(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		lookup = set()
		for i in nums1:
			lookup.add(i)
			
		result = []
		for i in nums2:
			if i in lookup:
				result.append(i)
				lookup.discard(i)
				
		return result