#!/usr/bin/env python3

class Solution(object):
	def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		length = len(nums)
		sum1 = 0
		for i in range(length+1):
			sum1 =sum1+i
			
		for i in range(0,length):
			sum1 = sum1-nums[i]
			
		return sum1