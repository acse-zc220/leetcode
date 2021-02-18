#!/usr/bin/env python3
class Solution(object):
	def intersect(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		
		
		lookup = dict()
		for i in nums1:
			if i not in lookup:
				lookup[i] = 0
			lookup[i] +=1
			
		result = []
		for i in nums2:
			if i in lookup and lookup[i]>0:
				result.append(i)
				lookup[i] -= 1
				
		return result