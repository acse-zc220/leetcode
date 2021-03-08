#!/usr/bin/env python3

class Solution(object):
	def thirdMax(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums = sorted(list(set(nums)))
		
		if len(nums) < 3:
			return max(nums)
		else:
			return nums[-3]