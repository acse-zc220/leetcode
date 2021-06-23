#!/usr/bin/env python3

class Solution(object):
	def findErrorNums(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		sum_unique = sum(set(nums))
		dup = sum(nums)- sum_unique
		miss = (len(nums)+1)*len(nums)//2 - sum_unique
		return[dup,miss]
	