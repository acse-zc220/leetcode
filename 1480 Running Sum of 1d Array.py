#!/usr/bin/env python3

class Solution(object):
	def runningSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		newnums = []
		curr_sum = 0
		for num in nums:
			curr_sum += num
			newnums.append(curr_sum)
		return newnums